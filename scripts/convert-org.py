from fuzzyparsers import parse_date
import sys
import datetime
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
    
    if line=="#+BEGIN_COMMENT":
        print( "---")
    elif line=="#+END_COMMENT":
        print("draft: false")
        print("---")
    elif line[0:3]==".. ":
        try:
            (left,right) = line.split(": ")
        except:
            left=""
            right=""
        
        key=left[3:]
        key = key.strip()
        right=right.strip()
        
        if key=="title":
            print(key+': "'+right+'"')
        elif key=="date":
            import datetime
            right = right[0:20]
            d = parse_date(right)
            #ds = f'date: {d.year}-{d.month:2d}-{d.day}'
            ds = "date: %4d-%02d-%02d"%(d.year,d.month,d.day)
            print(ds)
            #print(f'date: {d.year}-{d.month:2}-{d.day:2}T12:00:00-4:00')
        elif key=="tags":
            print("tags:")
            for t in right.split(","):
                t.strip()
                print("- "+t)
        elif key=="category:":
            print("categories:")
            for t in right.split(","):
                t.strip()
                print("- "+t)
    elif line[0:11]=="#+BEGIN_SRC":
        try:
            (x1,lang) = line.split(' ' ,2)
        except:
            lang='python'
            
        langs={'python':"python","C++":'c',"c++":'c',"clojure":"clojure"}
        if lang in langs.keys():
            lang=langs[lang]
        print(line)
        print("{{< highlight \"" + lang + "\" >}}")

    elif line=="#+END_SRC":
        print("{{< / highlight >}}")
        print(line)
        

    elif line=="*" or line=="**" or line=="***" or \
         line[:14]=="#+BEGIN_EXPORT" or line[:12]=="#+END_EXPORT":
        continue
    elif "../.." in line:
        line = line.replace("../..","file:")
        print(line)
    else:
        print(line)
        
    
