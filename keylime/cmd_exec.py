'''
SPDX-License-Identifier: Apache-2.0
Copyright 2017 Massachusetts Institute of Technology.
'''

import os
import subprocess
import threading
import time

# shared lock to serialize access to tools
utilLock = threading.Lock()

EXIT_SUCESS = 0


def _execute(cmd, env=None, **kwargs):
    proc = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, **kwargs)
    out, err = proc.communicate()
    code = proc.returncode
    return out, err, code


def run(cmd, expectedcode=EXIT_SUCESS, raiseOnError=True, lock=True,
        outputpaths=None, env=os.environ, **kwargs):
    """Execute external command.

    :param cmd: a sequence of command arguments
    """
    global utilLock

    t0 = time.time()
    if lock:
        with utilLock:
            retout, reterr, code = _execute(cmd, env=env, **kwargs)
    else:
        retout, reterr, code = _execute(cmd, env=env, **kwargs)

    t1 = time.time()
    timing = {'t1': t1, 't0': t0}

    # Gather subprocess response data
    retout_list = retout.splitlines(keepends=True)
    reterr_list = reterr.splitlines(keepends=True)

    # Don't bother continuing if call failed and we're raising on error
    if code != expectedcode and raiseOnError:
        raise Exception("Command: %s returned %d, expected %d, output %s, stderr %s" %
                        (cmd, code, expectedcode, retout_list, reterr_list))

    # Prepare to return their file contents (if requested)
    fileouts = {}
    if isinstance(outputpaths, str):
        outputpaths = [outputpaths]
    if isinstance(outputpaths, list):
        for thispath in outputpaths:
            with open(thispath, "rb") as f:
                fileouts[thispath] = f.read()

    returnDict = {
        'retout': retout_list,
        'reterr': reterr_list,
        'code': code,
        'fileouts': fileouts,
        'timing': timing,
    }
    return returnDict
