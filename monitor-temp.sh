#!/bin/bash
echo 't1;t2;t3;t4' > temp.dat
while :
do
	sensors -u > sensors_output
	./monitor-temp.py >> temp.dat 
	sleep 30
done
