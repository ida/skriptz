import glob
import os

def getMails(mails_file_path):
    """ Expects mails_file_path to a mails-file.
        Returns file-content as a string.
    """
    with open(mails_file_path) as fil:
       mails = fil.read()
    return mails

def getMailStartPosis(path):
    """ Expects path to a mails-file.
        Returns starting-line-numbers of each mail.
    """
    startposis = []
    lines = getMails(path).split('\n')
    headlines = ['From ', 'Return-Path: ', 'X-Original-To: ']
    headline_pos = 0
    headline = headlines[headline_pos]
    i = -1

    while i < len(lines)-1:
        i += 1
        line = lines[i]

        if line.startswith(headline):
            headline_pos += 1
            headline = headlines[headline_pos]

        if headline_pos == len(headlines) - 1:
            startposis.append(i-1) # gotcha
            headline_pos = 0
            headline = headlines[headline_pos]

    return startposis

def getBodyStartPosis(mails_file_path):
    """ Expects mails_file_path to a mails-file.
        Returns starting-line-numbers of each mail's body.
    """
    body_startposis = []
    lines = getMails(mails_file_path).split('\n')
    mail_startposis = getMailStartPosis(mails_file_path)

    i = mail_startposis.pop(0) - 1

    while i < len(lines)-1:
        i += 1
        line = lines[i]
        if line == '': # First empyt line after header -> We are in body.
            body_startposis.append(i+2) # gotcha
            if len(mail_startposis) > 0:
                i = mail_startposis.pop(0) - 1 # move on into next header
            else:
                break

    return body_startposis

def getBodies(mails_file_path):
    """ Expects mails_file_path to a mails-file.
        Returns body-strings as a flat list.
    """
    fromm = ''
    subject = ''
    bodies = []
    lines = getMails(mails_file_path).split('\n')
    mail_startposis = getMailStartPosis(mails_file_path)
    body_startposis = getBodyStartPosis(mails_file_path)
    i = -1
    while i < len(body_startposis)-1:
        i += 1
        body_start = body_startposis[i]
        if i+1 > len(body_startposis)-1:
            body_end = len(lines)-2 # Omit last empyt line: The deli between mails doesn't belong to body.
        else:
            body_end = mail_startposis[i+1]
        body = lines[body_start:body_end]
        bodies.append(body)
    return bodies

def formatMails(mails_file_path):
    """ Expects mails_file_path to a mails-file.
        Returns mails in this format:
        [(from + '\n' + subject + \n + body), ]
    """
    fromm = ''
    subject = ''
    mails = []
    head_startposis = getMailStartPosis(mails_file_path)
    body_startposis = getBodyStartPosis(mails_file_path)
    lines = getMails(mails_file_path).split('\n')
    i = head_startposis.pop(0)-1
    while i < len(lines)-1:
        i += 1
        line = lines[i]

        if line.startswith('Return-path: '):
            fromm = (line.split(' ')[1])[1:-1]

        if line.startswith('Subject: '):
            subject = ' '.join(line.split(' ')[1:])

            i = body_startposis.pop(0) -1
            if len(head_startposis) > 0:
                body_end = head_startposis.pop(0) -1
            else:
                body_end = len(lines) -2 # regard last empty line, not part of body, is deli between mails

            body = '\n'.join(lines[i:body_end]) # gotcha
            mail = [fromm, subject, body]
            mails.append(mail)
            i = body_end

    return mails

def recomposeMails(mails_file_path):
    """ Expects mails_file_path to a mails-file.
        Returns mail as string with 'From', 'Subject' and body.
    """
    numails = []
    mails = formatMails(mails_file_path)
    for mail in mails:
        numail = 'From ' + mail[0] + '\nSubject: ' + mail[1] + '\n' + mail[2]
        numails.append(numail)
    return numails

def splitMails(mails_file_path, mails_dir_path):
    """ Expects mails_file_path to a mails-file and
        a path to a directory, where each mail will be
        dropped as a single mail-file.
    """
    mails = recomposeMails(mails_file_path)
    for i, mail in enumerate(mails):
        with open(mails_dir_path + '/' + str(i) + '.mail', 'w') as fin:
            fin.write(mail)
    print 'splitted mails'

def pushMails(mails_dir_path):
    """ Expects path to a directory holding mails
        as single files, drops them into te defined
        Plonesite-folder, using mailtoplone.base.scripts.dropemail
    """
    if not mails_dir_path.endswith('/'): mails_dir_path += '/'
    mail_paths = glob.glob(mails_dir_path + '*')
    for mail_path in mail_paths:
        print 'push'
        print mail_path
        os.system('/home/ida/repos/mailtoplone.base/mailtoplone/base/scripts/dropemail -u http://admin:admin@localhost:8080/Plone/forumail -f ' + mail_path)

def main(mails_file_path, mails_dir_path):
#    splitMails(mails_file_path, mails_dir_path)
    pushMails(mails_dir_path)

if __name__ == '__main__':
    main('/var/mail/ida', '/home/ida/tmp/mails')

