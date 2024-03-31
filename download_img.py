
import requests
import subprocess

f1 = open('data.tsv', 'r')


for line in f1:
  # <link rel="image_src" href="
  link = line.split('\t')[2][28:-1]
  print(link)
  filename = 'img/' + link.split('/')[-2] + '.jpg'
  command = ['wget', '-O', filename, link, '-c']
  subprocess.run(command)

