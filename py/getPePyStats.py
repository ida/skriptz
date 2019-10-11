# Take a given list of egg-names,
# crawl and collect download-numbers of pepy.tech for each,
# compute the downloads-sum of all eggs and write it into a
# file named 'result.txt', it should look like:
#
# some-egg: 14k
# another-egg: 3k
# _______________
# total: 17k

# Exchange these list-items with the eggs you want to be counted, then
# run this script of the commandline `python this_script.py`:
egg_names = ["adi.dropdownmenu","adi.simplestructure","adi.simplesite",
"adi.trash","adi.revertorder","adi.workingcopyflag","adi.commons","adi.suite",
"adi.enabletopics","adi.samplecontent","adi.init","adi.fullscreen",
"adi.playlist","adi.slickstyle","adi.ttw_styles","adi.devgen"]


from os import system as exe

stats = {} #  { "egg_name": "downloads_amount_prettyfied" , }

url_begin = 'https://pepy.tech/badge/'


def main():

    total_downloads_amount = 0
    total_downloads_amount_in_kilo = 0

    for i, egg_name in enumerate(egg_names):

        egg_name = egg_name.replace('.', '-')
        egg_name = egg_name.replace('_', '-')
        url = url_begin + egg_name

        exe('wget ' + url)

        with open(egg_name) as fil:

            text = fil.read()

            # we know number of downloads is before third-last
            # ending-tag (+1 for last empty array-item from splitting):
            downloads_string = text.split('>')[-4].split('<')[0] # --> e.g. '42k'
            downloads_amount_in_kilo = int(downloads_string.split('k')[0].strip())
            downloads_amount = downloads_amount_in_kilo * 1000
            downloads_prettified = format(downloads_amount_in_kilo, ',').replace(',', '')
            total_downloads_amount_in_kilo += downloads_amount_in_kilo
            total_downloads_amount += downloads_amount
            stats[egg_name] = downloads_string

        exe('rm ' + egg_name)

    content = ''
    for key in stats:
        content += key + ': ' + stats[key] + '\n'
    total_downloads_amount = format(total_downloads_amount, ',')
    content += '____________________\n\ntotal:   ' + str(total_downloads_amount_in_kilo) + ' k'
    with open('result.txt', 'w') as fil:
        fil.write(content)

if __name__ == '__main__':
    main()
