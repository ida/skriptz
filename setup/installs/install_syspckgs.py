import os
import sys

def installSysPckgs():
    """ Expects passing a comma-separated list of pckgs to install:
        $ python install_syspckgs.py vim,colordiff,git
    """
    pckgs = sys.argv[1].split(',')
    repfil = 'install_syspckgs_report.txt'
    tmpfil = 'install_syspckgs_latest.tmp'
    errfil = 'install_syspckgs_errors.txt'
    fils = [repfil, tmpfil, errfil]
    tmptxt = ''
    reptxt = ''
    errtxt = ''
    errors = 0

    # Provide report-files, respectively delete outdated files:
    for fil in fils:
        if os.path.exists(fil): os.system('rm ' + fil)
        else: os.system('touch ' + fil)

    # Iterate over pckgs:
    for pckg in pckgs:

        # Install pckg:
        os.system('sudo yum install -y ' + pckg + ' &> ' + tmpfil)

        # Get latest-report:
        with open(tmpfil) as fil: tmptxt = fil.read()

        # Get overall-report, add latest-report:
        with open(repfil) as fil: reptxt = fil.read() + '\n' + tmptxt
        
        # Write new overall-report:
        with open(repfil, 'w') as fil: fil.write(reptxt)

        # Install failed:
        if tmptxt.endswith('Error: Nothing to do\n'):

            errors += 1

            # Get error report, add latest report:
            with open(errfil) as fil: errtxt = fil.read() + '\n' + tmptxt

            # Write new error report:
            with open(errfil, 'w') as fil: fil.write(errtxt)

            # For first error, prepend linebreak to feedback-msgs:
            if errors == 1: print ""

            # Give error-feedback:
            print "    Couldn't install " + pckg + ", name not found.\n"

    # Give feedback for err-report-file, if errors occured:
    if errors > 0:
        print "    See ./" + errfil + " for further error-details.\n"

    # Otherwise stay silent, as no news are good news :-)

    # Lastly remove tmp-file:
    os.system('rm ' + tmpfil)

if __name__ == '__main__':
    installSysPckgs()

