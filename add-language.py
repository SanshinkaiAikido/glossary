#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

inputfile = open('aikido.xml', 'r')
outputfile = open('aikido.xml.new', 'w')
for line in inputfile:
    outputfile.write(line)
    if 'local lang="mk" ' in line:
	    outputfile.write(line.replace('"mk"', '"sr"'))

