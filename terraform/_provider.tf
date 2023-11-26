provider "aws" {
  region = "ap-northeast-2"
  alias  = "test-apne2"
}

provider "aws" {
  region = "us-east-1"
  alias  = "test-use1"
}
