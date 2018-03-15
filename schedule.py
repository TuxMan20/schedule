#!/usr/bin/env python
#coding=utf-8

'''
Schedule Exporter
by TuxMan20
** Scans a web page for all of today's events
   and exports them to a .csv file on the desktop. **
'''

# import libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen
import unicodecsv as csv
import os.path

def main():
    # Replace or create a 'today.csv' file on the current user's desktop
    userhome = os.path.expanduser('~')
    csvfile= os.path.join(userhome, 'Desktop', 'today.csv')
    fptr = csv.writer(open(csvfile, "w"), encoding='utf-8')
    fptr.writerow(["Session", "Heure"]) # Write column headers as the first line

    # specify the url
    url = 'https://www.apple.com/today/store/unionsquare/'

    # query the website and return the html to the variable 'page'
    #page = requests.get(url) ##For Python3, you can use the 'requests' library
    page = urlopen(url)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Find all objects with a 'div' tag with 'data-label-day' of Today
    sessionToday = soup.find_all('div', attrs={'data-label-day':'Today'})

    for tags in sessionToday:
        sessionName = tags.find_all('a', attrs={'class': 'event-link'}) # Find session names
        sessionTime = tags.find_all('p', attrs={'class':'store-time typography-subbody'}) # Find session times
        for i in range(0, len(sessionName)):
            name = sessionName[i].text.strip() # Keeps the text and Strip whitespaces
            name = name.split('\n')[0] # Split the result at the first line jump and keep first half "[0]"
            #print(name, sessionTime[i].text) #Uncomment to see the output in stdout
            fptr.writerow([name, sessionTime[i].text])

if __name__ == "__main__":
    main()
