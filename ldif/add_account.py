import argparse
from string import Template
import subprocess


template_user_add = Template("""
# ${ACCOUNT}, People, tanaka.lab
dn: uid=${ACCOUNT},ou=people,dc=tanaka,dc=lab
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
uid: ${ACCOUNT}
sn: ${SN}
givenName: ${GN}
cn: ${GN} ${SN}
displayName: ${GN} ${SN}
uidNumber: ${UID}
gidNumber: ${UID}
loginShell: /bin/zsh
homeDirectory: /home/${ACCOUNT}
shadowExpire: -1
shadowFlag: 0
shadowWarning: 7
shadowMin: 8
shadowMax: 999999
shadowLastChange: 10877
mail: ${EMAILADDRESS}

dn: cn=${ACCOUNT},ou=groups,dc=tanaka,dc=lab
objectClass: posixGroup
cn: ${ACCOUNT}
gidNumber: ${UID}
""")

template_modify_passwd = Template("""
dn: uid=${ACCOUNT},ou=people,dc=tanaka,dc=lab
changetype: modify
replace: userPassword
userPassword: ${PASSWD}
""")


def main(user, uid, sn, gn, email):
    content_user_add = template_user_add.safe_substitute(
        ACCOUNT=user,
        UID=uid,
        SN=sn,
        GN=gn,
        EMAILADDRESS=email,
    )
    fname_user_add = f'user-add.{user}.ldif'
    with open(fname_user_add, 'w') as f:
        f.write(content_user_add)

    # add user
    subprocess.run([
        'ldapadd',
        '-h', 'localhost',
        '-x',
        '-D', 'cn=admin,dc=tanaka,dc=lab',
        '-w', 'admin',  # bind password
        '-f', fname_user_add
    ])
    subprocess.run(['rm', fname_user_add])

    # set up password for user
    r = subprocess.run(
        ['slappasswd', '-s', user],
        encoding='utf-8',
        stdout=subprocess.PIPE,
    )
    passwd = r.stdout.strip('\n')
    content_modify = template_modify_passwd.safe_substitute(
        ACCOUNT=user,
        PASSWD=passwd,
    )
    fname_modify = f'modify.{user}.ldif'
    with open(fname_modify, 'w') as f:
        f.write(content_modify)
    subprocess.run([
        'ldapmodify',
        '-h', 'localhost',
        '-x',
        '-D', 'cn=admin,dc=tanaka,dc=lab',
        '-w', 'admin',  # bind password
        '-f', fname_modify,
    ])
    subprocess.run(['rm', fname_modify])

    # home directory
    user_dir = f"/home/{user}"
    subprocess.run(['mkdir', user_dir])
    subprocess.run(['chown', '-R', f'{user}:{user}', user_dir])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add user on LDAP")
    parser.add_argument('user', help='adding user name')
    args = parser.parse_args()
    user = args.user

    with open('ldap-source.dat', 'r') as f:
        lines = f.readlines()

    for line in lines:
        contents = line.strip('\n').split(' ')
        if contents[0] == user:
            assert len(contents) == 5
            uid, sn, gn, email = contents[1:]
            main(user, uid, sn, gn, email)
            break
