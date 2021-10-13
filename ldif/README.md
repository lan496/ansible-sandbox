## Installation

1. Copy this directory at `/root/ldif`

2. Install OpenLDAP
```shell
apt install slapd ldap-utils nslcd
dpkg-reconfigure slapd
```

3. Configure `/etc/ldap/ldap.conf`
```shell
cp ldap.conf /etc/ldap/ldap.conf
```

check DIT (Directory Information Tree) for `dc=tanaka,dc=lab`:
```shell
ldapsearch -x -LLL -H ldap:/// -b dc=tanaka,dc=lab dn 
```

4. Configure `/etc/ldap.conf`
for example, append the followings:
```
base dc=tanaka,dc=lab
uri ldap://10.232.30.169  # gpu
```

5. Configure LDAP server
Add config for `admin`
```shell
ldapwhoami -x -D cn=admin,dc=tanaka,dc=lab -W 
```
We assume to set password as `admin`

Add nodes for people and groups
```shell
ldapadd -x -D cn=admin,dc=tanaka,dc=lab -w admin -f add_content.ldif
```

## Add user
1. check available UID
```shell
# check UID=10000 (password=admin)
ldapsearch -x -D "cn=admin,dc=tanaka,dc=lab" -b "dc=tanaka,dc=lab" "uidNumber=10000" -w admin
```

2. modify `ldap-source.dat`

3. run `add_account.py`
```shell
python3 add_account.py <user>
```

## Delete user
```shell
python3 delete_account.py <user>
```

## References
- https://ubuntu.com/server/docs/service-ldap
