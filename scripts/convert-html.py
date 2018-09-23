#!/usr/bin/python3
import sys
"""
---
title: "First post again"
date: 2018-09-21T17:21:15-04:00
draft: false
categories:
- meta
tags: 
- meta
---
"""


filename = sys.stdin.readline().strip()
f = open(filename)
for line in f.readlines():
    line = line.strip()
    
    if line[0:4]=="<!--":
        print( "---")
    elif line[:3]=="-->":
        print("draft: false")
        print("---")
        print("<!DOCTYPE html>")
    elif line[0:3]==".. ":
        (left,right) = line.split(":")
        
        key=left[3:]
        key = key.strip()
        right=right.strip()
        
        if key=="date" or key=="title":
            print(key+': "'+right+'"')
        elif key=="tags":
            print("tags:")
            for t in right.split(","):
                t.strip()
                print("- "+t)
    elif line[0:3]==">{%":
        (x1,x2,lang,x3) = line.split()
        print("{{< highlight " + lang + " >}}")
    elif line[0:2]=="{%":
        print("{{< / highlight >}}")
            
    else:
        print(line)
        
    
