# Take a given list of egg-names,
# crawl and collect download-numbers of pepy.tech for each,
# compute the downloads-sum of all eggs and write it into a
# file named 'pepy_stats.html', it should look like:
#
# some-egg: 14k
# another-egg: 3k
# _______________
# total: 17k

# Exchange these list-items with the eggs you want to be counted, then
# run this script of the commandline `python this_script.py`:
egg_names = ["adi.bookmark","adi.dropdownmenu","adi.simplestructure","adi.simplesite",
"adi.trash","adi.revertorder","adi.workingcopyflag","adi.commons","adi.suite",
"adi.enabletopics","adi.samplecontent","adi.init","adi.fullscreen",
"adi.playlist","adi.slickstyle","adi.ttw_styles","adi.devgen"]


import datetime
import os


stats = [] #  [ "egg_name", downloads_amount, 'another-egg', their_downloads_amount, ... ]



def getDownloadsAmount(text):

    # we know number of downloads is before third-last
    # ending-tag (+1 for last empty array-item from splitting):
    downloads_string = text.split('>')[-4].split('<')[0] # --> e.g. '42k'
    downloads_amount_in_kilo = int(downloads_string.split('k')[0].strip())
    downloads_amount = downloads_amount_in_kilo * 1000
    downloads_prettified = format(downloads_amount_in_kilo, ',').replace(',', '')
    return downloads_amount
            
            
def getEggPageHtml(egg_name):
    egg_name = egg_name.replace('.', '-')
    egg_name = egg_name.replace('_', '-')
    url_begin = 'https://pepy.tech/badge/'
    url = url_begin + egg_name

    if not os.path.exists(egg_name): # debug
        os.system('wget ' + url)

    with open(egg_name) as fil:

        text = fil.read()

    return text


def isOdd(number):
    return number % 2 != 0



def collectStats():

    for i, egg_name in enumerate(egg_names):

        html = getEggPageHtml(egg_name)

        downloads_amount = getDownloadsAmount(html)

        stats.append(egg_name); stats.append(downloads_amount)


def sortStats():
    newStats = []
    newStats.append(stats[0])
    newStats.append(stats[1])
    for i, item in enumerate(stats):
        egg_name = item
        if isOdd(i):
            downloads_amount = item
            # if item's dwnlds are more than first of newStats:
            if downloads_amount >= newStats[1]:
                print 'is >yy'
                print i

def main():
    
    collectStats()
    sortStats()

        #os.system('rm ' + egg_name) # debug
    exit() # debug
    # sort stats:
    content = 'Python packages and their download numbers taken from <a href="https://pepy.tech" title="Get download numbers of Python packages">pepy.tech</a><table>'
    for i, item in enumerate(stats):

        content += '<tr><td><a title="To the description on pypi" href="https://pypi.org/project/' + key + '">' + key + '</a></td><td>' + str(stats[key]) + '</td></tr>'
    total_downloads_amount = format(total_downloads_amount, ',')
    content += '<tr><td>Total</td><td>' + str(total_downloads_amount_in_kilo) + ' 000</td>'
    content += '</table>'
    content += 'These stats were generated using <a title="The script for generating download statistics" href="https://github.com/ida/skriptz/blob/master/py/getPePyStats.py">https://github.com/ida/skriptz/blob/master/py/getPePyStats.py</a>'
    content += '<br>Generated on: ' + str(datetime.datetime.now())[:16]

    with open('pepy_stats.html', 'w') as fil:
        fil.write(content)

if __name__ == '__main__':
    main()
