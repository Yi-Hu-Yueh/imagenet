# -*- coding: utf-8 -*-
import requests
import re
from xml.dom.minidom import Document
import os
from os import listdir
from os.path import isfile, isdir, join
from PIL import Image
import shutil
import sys
import argparse

exception_images=[]
exception_url=[]
def download(url, filename):
	print ("downloading with requests: " + filename)
	try:
		r = requests.get(url)
		with open(filename, "wb") as code:
			code.write(r.content)
	except Exception:
		print("************ downloading Exception: " + filename)
		exception_url.append(url)
		exception_images.append(filename)
		pass

if __name__ == '__main__':
	mypath = "n04120489"
	files = listdir(mypath)
	mainnames = []
	for f in files:
		fullpath = join(mypath, f)
		# 判斷 fullpath 是檔案還是目錄
		if isfile(fullpath):
			# print("檔案：", f)
			mainname = f.split('.', -1)[0]
			mainnames.append(mainname)
	lines = open('image_url.txt', encoding='UTF-8')
	for line in lines:
		# line_list = filter(None, line.split(" "))
		line_list = re.split(r'\t+', line)
		# print("line_list[0]: " + line_list[0])
		if line_list[0] in mainnames:
			url = line_list[1]
			# temp = re.split(r'[/]', url)[-1]
			# filename = os.path.join("images", temp)
			filename =  "images"+"/"+line_list[0]
			print(filename)
			filename = filename.strip('\n')
			download(url, filename+".jpg")
			# raise ValueError('A very specific bad thing happened.')

	print("line_list[0]: " )