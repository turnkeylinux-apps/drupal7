#!/usr/bin/python
"""Set Drupal7 admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt

from dialog_wrapper import Dialog
from mysqlconf import MySQL

from executil import system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
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

    m = MySQL()
    m.execute('UPDATE drupal7.users SET mail=\"%s\" WHERE name=\"admin\";' % email)
    m.execute('UPDATE drupal7.users SET init=\"%s\" WHERE name=\"admin\";' % email)
    system("drush variable-set site_mail %s" % email)
    system("drush variable-set update_notify_emails %s" % email)

    system("drush user-password admin --password=%s" % password)

if __name__ == "__main__":
    main()

