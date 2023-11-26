import boto3
import pandas as pd
import json

role_to_assume_arn = {
    "test": "arn:aws:iam::111111111111:role/admin-role",
    "dev": "arn:aws:iam::111111111111:role/admin-role",
}

# CSV 파일에서 ARN 및 태그 읽기
csv_file_path = "test.csv"
df = pd.read_csv(csv_file_path)

# 리전 리스트
regions = ["ap-northeast-2"]


# IAM Role을 Assume하고 resourcegroupstaggingapi 클라이언트 초기화
def initialize_resource_groups_tagging_api(role_to_assume_arn, region):
    # STS 클라이언트 초기화
    sts_client = boto3.client("sts")

    # AssumeRole 호출을 통해 임시 자격 증명 얻기
    assumed_role = sts_client.assume_role(
        RoleArn=role_to_assume_arn, RoleSessionName="AssumedRoleSession"
    )

    # Assume한 Role을 사용하여 resourcegroupstaggingapi 클라이언트 초기화
    resource_groups_tagging_api = boto3.client(
        "resourcegroupstaggingapi",
        aws_access_key_id=assumed_role["Credentials"]["AccessKeyId"],
        aws_secret_access_key=assumed_role["Credentials"]["SecretAccessKey"],
        aws_session_token=assumed_role["Credentials"]["SessionToken"],
        region_name=region,
    )

    return resource_groups_tagging_api


# 각 리전에 대해 반복
for region in regions:
    print(f"Processing resources in {region} region")

    # 각 행에 대해 ARN과 태그 읽어오기
    for index, row in df.iterrows():
        account = row["account"]
        arn = row["resource_arn"]
        tag_json = row["tag"]

        # IAM Role을 Assume하고 resourcegroupstaggingapi 클라이언트 초기화
        resource_groups_tagging_api = initialize_resource_groups_tagging_api(
            role_to_assume_arn=role_to_assume_arn[account], region=region
        )

        # JSON 형태의 문자열을 파싱하여 딕셔너리로 변환
        try:
            tags_dict = json.loads(tag_json.replace("'", '"'))
        except json.JSONDecodeError as e:
            print(
                f"Error decoding JSON for resource {arn} in {region} region: {str(e)}"
            )
            continue

        # 리소스에 태그 붙이기
        try:
            print("arn: ", arn)
            print("arn type: ", type(arn))
            print("tags_dict: ", tags_dict)
            resource_groups_tagging_api.tag_resources(
                ResourceARNList=[arn], Tags=tags_dict
            )
            print(f"Successfully tagged resource {arn} in {region} region")
        except Exception as e:
            print(f"Error tagging resource {arn} in {region} region: {str(e)}")
