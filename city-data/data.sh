#!/bin/bash 


DELIMITER=","

for i in $(cut -f1 -d "${DELIMITER}" city-data.csv ); 
do 
    grep "${i}" weather-cities.csv | cut -f1  -f3-9 -d "${DELIMITER}"; 
done