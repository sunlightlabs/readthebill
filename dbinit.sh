#!/bin/bash

./manage.py addfeed http://www.sunlightfoundation.com/feeds/latest/ sunlightfoundation
./manage.py addfeed "http://dev.opencongress.org/bill/readthebill.rss?sort=gpo&show_resolutions=false" rushedbills
./manage.py addfeed "http://feeds.delicious.com/v2/rss/sunlight_foundation/bundle:readthebill?count=15" press
./manage.py updatefeeds

./manage.py loaddata data/orgs.json