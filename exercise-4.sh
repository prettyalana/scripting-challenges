#!/bin/bash

curl https://api.coinpaprika.com/v1/tickers | jq -r 'sort_by(.volume_24h) | reverse | .[] | "\(.symbol) \(.quotes.USD.volume_24h)"' | uniq | head -n 10