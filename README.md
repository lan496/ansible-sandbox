## Installation

set up virtualbox
```shell
sudo apt install virtualbox
# https://www.vagrantup.com/downloads
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vagrant
```

set up vagrant
```shell
vagrant init ubuntu/focal64
vagrant up
vagrant ssh-config
```

```shell
python -m pip install -r requirements.txt
pre-commit install
```

```shell
ansible-galaxy install nvidia.nvidia_driver
```

## Usage

0. Create a provision user: `ansible`
at remote nodes
```shell
adduser ansible
usermod -aG sudo ansible
```

1. Connect to remote nodes
at control node
```shell
ssh-copy-id -i ~/.ssh/id_****.pub ansible@<hostname>
# checking
ansible <pattern> -i <inventory> -m ping
```


## Developments

### Create custom role under `roles/`
```shell
cookiecutter -o roles cookiecutter-ansible-role
```

## Misc

```shell
ansible-playbook -i inventory.yml playbook.yml --ask-become-pass [-e build_hosts=****]
```
