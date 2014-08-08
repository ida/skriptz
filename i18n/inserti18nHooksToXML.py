#! /usr/env/python

# Parse an xml-file char for char and
# insert missing i18n-hooks.
# TODO: tal:content/replace-var-text ->assume i18n is done in delivering py-file
# TODO: nested tags with each holding text

import re

file_name = 'temp.pt'

extracted_domain = None
wanted_domain = 'my.domain'
msg_id = 0

hasDomain  = False
passedFirstTag = False
transMissing = False

# First, we look quickly, if an i18n:domain has been specified or not.
# If one is found, we assume it's at the right place (a parent element of
# the elements holding text to be translated):

with open(file_name) as fin:
    for line in fin:
        if line.find('i18n:domain') != -1:
            # Which domain is it?
            result = result = re.search('i18n:domain="(.*?)"', line)
            extracted_domain = result.group(1)
            if extracted_domain != wanted_domain:
                hasDomain = True
            print extracted_domain


with open(file_name) as fin, open(file_name + '.tmp', 'w') as fout:

    ln_nr = 0
    for line in fin:
        ln_nr += 1
        #print ln_nr


        nuline = ''
        indi = 0

        while( indi < len(line) ):


            text = '' # reset

            nuline += line[indi]


            ############################
            #    OPENING TAG STARTS    #
            ############################

            # We have an opening-tag and it's not an XML-comment:
            if line[indi] == '<' and line[indi+1] != ('/' or '!'):


                hasHook = False
                needHook = True
                indi += 1
                nuline += line[indi]

                # As long as tag doesn't close:
                while (line[indi] != '>'):


                    ##################################
                    #  Apply i18n:domain if missing  #
                    ##################################
                    if not hasDomain:
                        if indi+1 < len(line) and line[indi+1] == '>':

                            if passedFirstTag != True:

                                nuline += ' i18n:domain="' + wanted_domain + '"'

                            passedFirstTag = True


                    #####################
                    # LINEBREAK IN TAG  #
                    #####################
                    # Line ended and tag hasn't finished:
                    if indi+1 == len(line):
                        break
                    indi += 1
                    nuline += line[indi]


                    #########################################
                    # HAS i18n:translate or i18n:attribute  #
                    #########################################
                    # We have a hook:
                    if line[indi] == 'i' and line[indi+1] == '1' and line[indi+2] == '8':
                        hasHook = True
                        # Move to first apo:
                        while (line[indi] != '"'):
                            indi += 1
                            nuline += line[indi]

                        # No val is given, if followed directly by next apo:
                        if line[indi+1] == '"':
                            # Apply msg_id:
                            nuline += str(msg_id)
                            msg_id += 1
                        else:
                            needHook = False


                    ###########
                    # HAS TAL #
                    ###########
                    # Do we have a tal-expression?
                    if line[indi] == 't' and line[indi+1] == 'a' and line[indi+2] == 'l' and line[indi+3] == ':':

                        # Is it a i18n-relevant tal-statement?
                        # We consider 'content', 'replace', and 'attributes' as relevant,
                        # which leaves 'define', 'condition', 'repeat' and 'omit-tag' as neglectable:
                        if line[indi+4] == 'a':
                            needHook = False
                        if line[indi+4] == 'c' and line[indi+5] == 'o' and  line[indi+6] == 'n' and line[indi+7] == 't':
                            needHook = False
                        if line[indi+4] == 'r' and line[indi+5] == 'e' and  line[indi+6] == 'p' and line[indi+7] == 'l':
                            needHook = False


                #####################
                # OPENING TAG STOPS #
                #####################
                # While-loop ended, we're out of opening tag:
                if (line[indi] != '>'):
                    nuline += line[indi]


                #####################
                #   COLLECT TEXT    #
                #####################

                # Have a look, if there is actually some text following to translate:
                # Don't change index!
                andi = indi
                text = '' # reset

                while andi+1 < len(line) and line[andi+1] != '<':
                    andi += 1

                    # Remove superflous whitespace, max. one:
                    if line[andi] == ' ':
                        if andi+1<len(line) and line[andi+1] != ' ':
                            text += line[andi]
                    else:
                        text += line[andi]

                    # We have some text:
                    if text != '':
                        # If first char is whitespace, remove it:
                        if text[0] == ' ':
                            text = text[1:-1]
                        # If text is a linebreak, remove it:
                        if text == '\n':
                            text = ''
                        # We don't have text, set flag:
                        if text == '':
                            needHook = False
                        # We have text:
                        else:



                            # There was a i18n:domain specified already,
                            # are there i18n-hooks missing for strings?
                            if hasDomain and needHook:
                                missingTrans = True




################NEST###########################################################################
#check if another opening tag is following right away (nest) and if it also contains text:
                            while andi+1 < len(line) and line[andi+1] == '<':
                                andi += 1

                                if andi+1<len(line) and line[andi+1] == ('/'):
                                    pass#rint 'closing tag after opening, no nest'
                                else:

                                    # Remove superflous whitespace, max. one:
                                    if line[andi] == ' ':
                                        if andi+1<len(line) and line[andi+1] != ' ':
                                            text += line[andi]
                                    else:
                                        text += line[andi]

                                    # We have some text:
                                    if text != '':
                                        # If first char is whitespace, remove it:
                                        if text[0] == ' ':
                                            text = text[1:-1]
                                        # If text is a linebreak, remove it:
                                        if text == '\n':
                                            text = ''
                                        # Now, if there is still sth left:
                                        if text != '':

                                            pass#rint 'a tag with text is nested in a tag with text'

#############################################################################################

                #######################
                #   APPLY i18n HOOK   #
                #######################


                # DEV:
                if not hasDomain:

                    # Apply complete hook, in case needed:
                    # Check, if we have a nest and if the tag didn't contain text:
                    if text != '':
                        if (hasHook == False) and (needHook == True):
                            # Remove closing '>' of one char before current pos:
                            nuline = nuline[:-1]
                            #nuline += ' i18n:translate="' + str(msg_id) + '">'
                            nuline += ' i18n:translate="' + text + '">'
                            msg_id += 1
                            hasHook = True



            #######################
            # Next char for loop: #
            #######################
            indi += 1


        #################################################
        # Finally write composed nuline to workingcopy: #
        #################################################
        fout.write(nuline)

# TODO: has another domain than ours and strs missing trans
if hasDomain and missingTrans:
    print "There was a domain found, it's not ours and there are still strings missing a translation-hook."
