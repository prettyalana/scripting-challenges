#!/bin/bash

filepath=$1
count=0
while true;
do
    stderr=$(mktemp)
    stdout=$(mktemp)

    "$filepath" >"$stdout" 2>"$stderr"

    exit_status=$?

    if [ $exit_status -eq 0 ];
    then 
        ((count+=1))
    else
        echo "It took $count runs to fail." 
        echo "Standard Output: "
        cat $stdout
        echo "Standard Error: "
        cat $stderr
        rm "$stdout" "$stderr"
        break
    fi 
done
