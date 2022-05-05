~~~

sudo yum install -y python3

sudo pip3 install --user boto3

~~~


Create a file named inventory_aws_ec2.yml in the project directory.

copy the below code in it 

~~~

plugin: aws_ec2
regions:
  - "us-east-1"
keyed_groups:
  - key: tags.Name
  - key: tags.task
filters:
  instance-state-name : running
compose:
  ansible_host: public_ip_address

~~~
Ping the target nodes with dynamic inventory

ansible-inventory --graph -i inventory_aws_ec2.yml

replace ansible.cfg inventory with inventory_aws_ec2.yml

ansible-playbook playbook.yml
