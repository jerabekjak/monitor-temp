#!/usr/bin/python
import datetime

ff = open('sensors_output', 'r')
lines = ff.readlines()
n = len(lines)

nf = datetime.datetime.now()
outline = '{};'.format(nf.strftime('%Y-%m-%d %H:%M:%S'))

for i in range(n) :
    line = lines[i]
    if ('Core' in line):
        line_t = lines[i+1]
        t =  (line_t.replace('\n','').split(': '))
        outline += '{};'.format(t[1])
outline = outline[:-1]
print (outline)

