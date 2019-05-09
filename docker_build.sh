#!/bin/sh

set -x
pipenv lock -r > requirements.txt
latest_tag=$(git describe --tags)
image=registry-qa.webex.com/iaas-storage/wibot$latest_tag
docker build --build-arg PIP_USERNAME=$PIP_USERNAME --build-arg PIP_PASSWORD=$PIP_PASSWORD -t $image .
docker push $image
