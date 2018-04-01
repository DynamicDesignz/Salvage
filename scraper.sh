#!/bin/bash

set -euo pipefail
# Extracting criteria to a single link and parsing it to __urls file.
criteria=$(gawk -F: '
BEGIN{  
        criteria_string = ""
        criteria = "TYPE MAKE MODEL VERSION ADDITIONAL"
        number = split(criteria, criteria_array, " ")
} 
{
    for (i = 1; i <= number; i++) {
        if (match($1, criteria_array[i])) {
            if (length($2) != 0) {
                if (criteria_array[i] == "ADDITIONAL") {
                    criteria_string=criteria_string"q-"$2"/"
                } 
                else criteria_string=criteria_string$2"/"
                }
        }
    }
}
END{print criteria_string}
' config)
criteria=${criteria::-1}    # Get rid of the last forward slash. Otherwise the link won't be recognized properly by Scrapy
url="https://www.otomoto.pl/$criteria"
echo $url > __urls

DATE=$(date +%Y-%m-%d)
mkdir -p $DATE
TIME=$(date +%H:%M)
scrapy crawl salvage -o $DATE/raw$TIME.csv
