#!/usr/bin/python
import os
os.chdir("src")
for fl in filter(lambda f: os.path.isfile(f), os.listdir("./")):
	print("Compiling: " + fl)
	os.system("lessc " + fl + " > ../css/" + fl[:-5] + ".css")
