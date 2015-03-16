__author__ = 'Andy'
import requests
from lxml import etree

cookies = {
    #!!!!! YOU NEED TO FILL THESE IN !!!!!
    # They Can all be grabbed from chrome if you click on the record button in 'network' and refresh.
    'myecs': '<USERNAME>',
    'ecs_intra_session': '<ECS SESSION TOKEN>',
    'CAKEPHP': '<CAKEPHPTOKEN>',
    'seen_cookie_notice': '1'
}

for i in xrange(300):
    response = requests.get('https://society.ecs.soton.ac.uk/nominations/support/{}'.format(i), verify=False, cookies=cookies)
    tree = etree.fromstring(response.text, etree.HTMLParser())
    text = tree.xpath('/html/body/div[3]/h1')[0].text
    if text != "Support  for  ":
        print "{} : {}".format(i, text)