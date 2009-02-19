#!/bin/bash

./manage.py addfeed http://www.sunlightfoundation.com/feeds/latest/ sunlightfoundation
./manage.py addfeed "http://dev.opencongress.org/bill/readthebill.rss?sort=gpo&show_resolutions=false" rushedbills
./manage.py updatefeeds

./manage.py loaddata data/orgs.json