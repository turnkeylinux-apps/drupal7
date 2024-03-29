#!/usr/bin/python3
"""Set Drupal7 admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
from libinithooks import inithooks_cache
import subprocess

from libinithooks.dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Drupal7 Password",
            "Enter new password for the Drupal7 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Drupal7 Email",
            "Enter email address for the Drupal7 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    m = MySQL()
    m.execute('UPDATE drupal7.users SET mail=%s WHERE name=\"admin\";', (email, ))
    m.execute('UPDATE drupal7.users SET init=%s WHERE name=\"admin\";', (email, ))

    # this would work with "normal" 'drush', but why not use 'turnkey-drush'!?
    d7_dir = '/var/www/drupal7'
    tkl_drush = "/usr/local/bin/turnkey-drush"
    subprocess.run([tkl_drush, "variable-set", "site_mail", email], cwd=d7_dir)
    subprocess.run([tkl_drush, "variable-set", "update_notify_emails", email], cwd=d7_dir)
    subprocess.run([tkl_drush, "user-password", "admin", f"--password={password}"], cwd=d7_dir)

if __name__ == "__main__":
    main()

