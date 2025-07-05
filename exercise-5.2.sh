#!/bin/bash


cat apache_access | awk '{print $10}' | sort -nr | head -n 5
