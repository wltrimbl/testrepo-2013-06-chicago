#!/bin/bash

if [[ ! -e Waroftheworlds.txt ]] 
   then
   curl http://www.gutenberg.org/cache/epub/36/pg36.txt > Waroftheworlds.txt
   else 
   echo "Waroftheworlds.txt already exists, refusing to overwrite."
   fi
