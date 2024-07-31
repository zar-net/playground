#!/bin/bash

usage() {
    echo "Usage: $0 -c|-nt inputfile"
    exit 1
}

if [ "$#" -ne 2 ]; then
    usage
fi

option=$1
inputfile=$2

if [ ! -f "$inputfile" ]; then
    echo "Input file not found!"
    exit 1
fi

if [ "$option" == "-c" ]; then
    echo "Username,RID,LM Hash,NT Hash" > output.csv
    awk -F':' '{print $1","$2","$3","$4}' "$inputfile" >> output.csv
    echo "CSV file created: output.csv"
elif [ "$option" == "-nt" ]; then
    awk -F':' '{print $1","$4}' "$inputfile"
else
    usage
fi
