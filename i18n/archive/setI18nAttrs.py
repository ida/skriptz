# !/usr/bin/python
import os
import shutil
from bs4 import BeautifulSoup
wanted_file_types = ['.pt', '.cpt', '.zpt']
domain = 'amp.translations'
for root, dirs, files in os.walk("."):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        splitted_name = os.path.splitext(file_name)
        if len(splitted_name) > 0:
            suff = splitted_name[1]
            if suff in wanted_file_types:
                food = open(file_path)
                soup = BeautifulSoup(food, 'html.parser')
                tags = soup.find_all()
                for tag in tags:
                    HAS_i18n_ATT = False
                    need_i18n_att = []
                    dont_need_i18n_att = []
                    attis = tag.attrs
                    # For each att in tag:
                    for atti in attis:
                        
                        # Collect title-, alt- or value-att:
                        if (atti == 'title') or (atti == 'alt') or (atti == 'value'):
                        
                            # Att has a val:
                            if tag[atti] != '':
                                
                                # Val is not a var, otherwise ignore:
                                if tag[atti][0] != '$':
                                    
                                    # Collect:
                                    need_i18n_att.append(atti)

                        # Overriden by tal-att or i18n-att already set?
                        # Collect to ignore them later:
                        if atti == ('i18n:attributes' or 'tal:attributes'):
                                        atts = tag[atti]
                                        atts = atts.split(';')
                                        for att in atts:
                                            att = att.strip()
                                            att = att.split(' ')[0]
                                            # Collect:
                                            dont_need_i18n_att.append(att)
                        if atti == 'i18n:attributes':
                            HAS_i18n_ATT = True

                        # End of 'for att in attis',
                    
                    # back to tag:

                    ################################
                    ################################
                    
                    
                    ################################
                    # Compare if needed, collect and set i18n:attribute:
                    value = ''
                    
                    # Compare:
                    for need in need_i18n_att:
                            
                            # Really needed?
                            if need not in dont_need_i18n_att:
                                
                                # Collect val-str:
                                value += ' ' + need + ';'
                    
                    # Collected val-str is not empty, 
                    # we have sth to set later on:
                    if value != '':

                        # Already has i18n-att: 
                        if HAS_i18n_ATT:
                            # Add val to existing val:
                            value = value + tag['i18n:attributes'] 
                        
                        # No i18n-att:
                        else:
                            value = value.strip()
                            # Set att initially:
                            tag['i18n:attributes'] = value 
                
                # EO for each tag    
                
                # Prepare soup and overwrite template with cooked i18n-hooks:
                soup = soup.prettify().encode('ascii', 'xmlcharrefreplace')
                result = open(file_path + '.tmp', 'w')
                result.write(str(soup))
                result.close()
		shutil.move(file_path + '.tmp', file_path)
