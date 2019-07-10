# wibot

Webex IaaS bot

## Installation
<pre>
git clone https://wwwin-github.cisco.com/webex-iaas/wibot
cd wibot
pipenv --python 3.6
pipenv shell
pipenv install
python setup.py install
</pre>

## Run

Set the following to environment variables
<pre>
BOT_NAME=XYX
BOT_TOKEN=ABC
</pre>

To run the bot

<pre>
python -m wibot.wibot
</pre>

## Deployment

wibot needs to be deployed in AMS CaaS in-order to get access to SNOW
