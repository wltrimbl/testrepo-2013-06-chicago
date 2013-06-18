#!/bin/bash
# This script downloads a table representing group memberships of certain terrorists.  
# See the blog post by   http://kieranhealy.org/blog/archives/2013/06/09/using-metadata-to-find-paul-revere/   
# and the github repository with the R script at 
# https://github.com/kjhealy/revere
if [[ ! -e PaulRevereAppD.csv ]] 
    then
    curl https://raw.github.com/kjhealy/revere/master/data/PaulRevereAppD.csv > PaulRevereAppD.csv 
    else
    echo "PaulRevereAppD.csv already exists, refusing to overwrite."
    fi

