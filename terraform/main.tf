resource "aws_resourceexplorer2_index" "test_apne2" {
  type = "LOCAL"
  provider = aws.test-apne2
}

resource "aws_resourceexplorer2_index" "test_use1" {
  type = "LOCAL"
  provider = aws.test-use1
}

resource "aws_resourceexplorer2_view" "test_apne2" {
  name = "default-view"
  default_view = true

  included_property {
    name = "tags"
  }

  depends_on = [aws_resourceexplorer2_index.test_apne2]
  
  provider = aws.test-apne2
}

resource "aws_resourceexplorer2_view" "test_use1" {
  name = "default-view"
  default_view = true

  included_property {
    name = "tags"
  }

  depends_on = [aws_resourceexplorer2_index.test_use1]

  provider = aws.test-use1
}
