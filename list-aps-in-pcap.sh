#!/bin/bash
tcpdump -ennr $1 '(type mgt subtype beacon)' | grep BSSID | while read LINE; do
  BSSID=`echo $LINE | awk -F'BSSID:' '{print $2}' | awk -F'Beacon \(' '{print $2}' | awk -F '\)' '{print $1}'`;
  NAME=`echo $LINE | awk -F'BSSID:' '{print $2}' | awk '{print $1}'`;
  echo "$NAME = $BSSID";
done;

