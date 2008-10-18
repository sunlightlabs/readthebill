#!/bin/bash

./manage.py addfeed http://www.sunlightfoundation.com/feeds/latest/ sunlightfoundation
./manage.py addfeed http://feeds.feedburner.com/OpenLeft-FrontPage openleft
./manage.py addfeed http://thenextright.com/fbfeed thenextright
./manage.py updatefeeds

./manage.py loaddata data/orgs.json