#!/bin/sh

docker build -t shaper_to_gt .
docker run -p 5000:5000 --rm -it shaper_to_gt