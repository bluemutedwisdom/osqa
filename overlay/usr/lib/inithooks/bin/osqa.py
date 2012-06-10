#!/usr/bin/python
"""Set OSQA domain to serve

Option:
    --domain=   unless provided, will ask interactively
                DEFAULT=www.example.com
"""

import sys
import getopt

from dialog_wrapper import Dialog
from executil import system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

DEFAULT_DOMAIN="www.example.com"

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'domain='])
    except getopt.GetoptError, e:
        usage(e)

    domain = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--domain':
            domain = val

    if not domain:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        domain = d.get_input(
            "OSQA Domain",
            "Enter the domain to serve OSQA.",
            DEFAULT_DOMAIN)

    if domain == "DEFAULT":
        domain = DEFAULT_DOMAIN

    config = "/var/www/osqa/settings_local.py"
    system("sed -i \"s|APP_URL.*|APP_URL = 'http://%s'|\" %s" % (domain, config))

if __name__ == "__main__":
    main()

