#/bin/bash
echo "---------------------------------------------------------------------------"
echo "Checking for AWS CLI..."
echo "---------------------------------------------------------------------------"
if ! command -v aws &> /dev/null
then
  echo "Downloading awscli..."
  curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
  if [ $? -eq 0 ]; then
    echo "AWS CLI bundle downloaded successfully..."
  fi
  echo "Checking for unzip command..."
  if ! command -v unzip &> /dev/null
  then
    echo "Installing unzip..."
    sudo apt-get install unzip
    if [ $? -eq 0 ]; then
      echo "unzip installed successfully..."
    fi
  fi
  echo "Unzipping awscli package..."
  unzip awscli-bundle.zip
  sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
fi
aws configure 
aws ec2 describe-tags --filters "Name=resource-id,Values=`ec2metadata --instance-id`"
