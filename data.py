
import requests
import re

f1 = open('data.tsv', 'w')

for _ in range(200):
  html = requests.get('https://ebird.org/species/surprise-me')
  # print(html.text)

  # 	<link rel="canonical" href="https://ebird.org/species/bawhor2" />
  # <meta property="og:title" content="Black-and-white-casqued Hornbill - eBird" />
  # <link rel="image_src" href="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/240370931/900" type="image/jpeg" />
  link = re.findall(r'https://ebird.org/species/[a-z0-9]+', html.text)
  print(link[0])
  name = re.findall(r'meta property="og:title" content="[A-Za-z-\' ]+', html.text)
  # print(name[0])
  img = re.findall(r'<link rel="image_src" href="https://cdn.download.ams.birds.cornell.edu/api/v1/asset/[0-9/]+', html.text)
  # print(img[0])
  f1.write(link[0] + '\t' + name[0] + '\t' + img[0] + '\n')

f1.close()