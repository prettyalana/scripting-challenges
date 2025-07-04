#!/bin/bash

file=$1
paths=$(find . -name "$file")
count=$(find . -name "$file" | wc -l | xargs)
if [ "$count" -gt 1 ];
then 
    echo "Found $count matches."
    echo "$paths"
elif [ "$count" -eq 1 ];
then
    echo "Found $count match."
    echo "$paths"
else 
    echo "Found $count matches."
fi