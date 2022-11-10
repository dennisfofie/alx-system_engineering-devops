#!/usr/bin/env bash
for result in $(cat ./README.md)
	do
		echo "i am done in file"
		echo " "
		echo "$result"
	done

echo "end of for loop"
