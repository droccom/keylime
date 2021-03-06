#!/usr/bin/python3

'''
SPDX-License-Identifier: Apache-2.0
Copyright 2017 Massachusetts Institute of Technology.
'''

import sys

from keylime import registrar_common
from keylime import config
from keylime import keylime_logging
import keylime.cmd.migrations_apply

logger = keylime_logging.init_logging('registrar')

config = config.get_config()


def main(argv=sys.argv):
    # if we are configured to auto-migrate the DB, check if there are any migrations to perform
    if config.has_option('registrar', 'auto_migrate_db') and config.getboolean('registrar', 'auto_migrate_db'):
        keylime.cmd.migrations_apply.apply('registrar')

    registrar_common.start(
        config.get('registrar', 'registrar_ip'),
        config.getint('registrar', 'registrar_tls_port'),
        config.getint('registrar', 'registrar_port'))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)
