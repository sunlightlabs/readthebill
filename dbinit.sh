#!/bin/bash

./manage.py addfeed http://www.sunlightfoundation.com/feeds/latest/ sunlightfoundation
./manage.py addfeed http://www.thenextright.com/fbfeed thenextright
./manage.py addfeed http://www.cnewmark.com/rss.xml craignewmark
./manage.py addfeed http://pogoblog.typepad.com/pogo/index.rdf pogo
./manage.py addfeed http://personaldemocracy.com/node/feed pdf
./manage.py addfeed http://www.ombwatch.org/blog/all/all/all/feed ombwatch
./manage.py addfeed http://www.mediaaccess.org/rss/ mediaaccess
./manage.py addfeed http://www.fas.org/blog/secrecy/feed secrecynews
./manage.py addfeed http://www.eff.org/rss/updates.xml eff
./manage.py addfeed http://www.opensecrets.org/news/rss.xml crp
./manage.py addfeed http://blog.cdt.org/feed/ cdt

./manage.py addfeed "http://dev.opencongress.org/bill/readthebill.rss?sort=gpo&show_resolutions=false" rushedbills
./manage.py addfeed "http://feeds.delicious.com/v2/rss/sunlight_foundation/readthebill?count=15" press

./manage.py updatefeeds

./manage.py loaddata data/orgs.json