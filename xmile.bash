#!/bin/bash

#ARCHITECT="/Applications/Stella Architect.app"
#XMUTIL="XMUtil"
XMUTIL="/Users/bschoenberg/code/personal/xmutil/DerivedData/XMUtil/Build/Products/Debug/XMUtil"
ARCHITECT="/Users/bschoenberg/code/dev_mac/StellaQt/DerivedData/StellaQt/Build/Products/Debug/Stella Architect.app"
DIR="./tests"

for input_dir in $DIR
do
	echo "Generate xmile files into: $input_dir"

	find $input_dir -name '*.mdl' | sed 's/\.mdl$//' | while read f; do

	 	echo "Converting $f.mdl"
	    "$XMUTIL" "$f.mdl"
	    if [ -f "$f.xmile" ]; then
	    	cp "$f.xmile" "$f.stmx"

	    	echo "Opening in Architect $f.stmx"
	    	open -W -a "$ARCHITECT" "$f.stmx" --args -r -s -q
	    else
	    	echo "XMUtil hit an error"
	    	sleep 10
	    fi
	done
done