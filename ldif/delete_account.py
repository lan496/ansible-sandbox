import argparse
from string import Template
import subprocess


template_delete_user = Template("""
dn: uid=${ACCOUNT},ou=people,dc=tanaka,dc=lab
changetype: delete
""")

template_delete_from_group = Template("""
dn: cn=${ACCOUNT},ou=groups,dc=tanaka,dc=lab
changetype: delete
""")


def main(user):
    # delete user
    content_delete_user = template_delete_user.safe_substitute(
        ACCOUNT=user,
    )
    fname_delete_user = f"delete-user.{user}.ldif"
    with open(fname_delete_user, 'w') as f:
        f.write(content_delete_user)
    subprocess.run([
        'ldapmodify',
        '-h', 'localhost',
        '-x',
        '-D', "'cn=admin,dc=tanaka,dc=lab'",
        '-w', 'admin',
        '-f', fname_delete_user,
    ])
    subprocess.run(['rm', fname_delete_user])

    # delete from group
    content_delete_from_group = template_delete_from_group.safe_substitute(
        ACCOUNT=user,
    )
    fname_delete_from_group = f"delete-from-group.{user}.ldif"
    with open(fname_delete_from_group, 'w') as f:
        f.write(content_delete_from_group)
    subprocess.run([
        'ldapmodify',
        '-h', 'localhost',
        '-x',
        '-D', 'cn=admin,dc=tanaka,dc=lab',
        '-w', 'admin',
        '-f', fname_delete_from_group,
    ])
    subprocess.run(['rm', fname_delete_from_group])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Delete user on LDAP")
    parser.add_argument('user', help='deleting user name')
    args = parser.parse_args()
    user = args.user

    main(user)
