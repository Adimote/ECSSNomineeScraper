__author__ = 'Andy'
import requests
from lxml import etree

cookies = {
    ## !!! YOUR COOKIES HERE !!!
}

for i in xrange(300):
    response = requests.get('https://society.ecs.soton.ac.uk/nominations/support/{}'.format(i), verify=False, cookies=cookies)
    tree = etree.fromstring(response.text, etree.HTMLParser())
    text = tree.xpath('/html/body/div[3]/h1')[0].text
    if text != "Support  for  ":
        print "{} : {}".format(i, text)
