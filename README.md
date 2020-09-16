The bot has integrations with NetDB, FW devices(read-only),Solar winds, STAP, IaaS engine,Centralized Logging Platform, F5 IPI database and F5 feed server. 
# WebExTeamsBot, a.k.a Marvin

This package makes creating [Webex Teams](https://www.webex.com/products/teams/index.html) bots in Python super simple.  


> This package is based on the previous [ciscosparkbot](https://github.com/imapex/ciscosparkbot) project.  This version will both move to new Webex Teams branding as well as add new functionality.  If you've used `ciscosparkbot` you will find this package very similar and familiar.  

# Prerequisites

If you don't already have a [Webex Teams](https://www.webex.com/products/teams/index.html) account, go ahead and [register](https://www.webex.com/pricing/free-trial.html) for one.  They are free.

1. You'll need to start by adding your bot to the Webex Teams website.

    [https://developer.webex.com/my-apps](https://developer.webex.com/my-apps)

1. Click **Create a New App**



2. Click **Create a Bot**.



3. Fill out all the details about your bot.  You'll need to set a name, username, icon (either upload one or choose a sample), and provide a description.



4. Click **Add Bot**.

 On the Congratulations screen, make sure to copy the *Bot's Access Token*, you will need this in a second.


# Installation

> Python 3.6+ is recommended.  Python 2.7 should also work.  

1. Create a virtualenv and install the module

    ```
    python3.6 -m venv venv
    source venv/bin/activate
    pip install webexteamsbot
    ```
# Design
 ![use-bot](https://github.com/ak-b/TeamsBot/blob/master/images/Security_Bot_Arch1.png)
  
# Use-Cases
 ![use-bot](https://github.com/ak-b/TeamsBot/blob/master/images/bot_use_cases.png)
 
# Walkthrough
 ![use-bot](https://github.com/ak-b/TeamsBot/blob/master/images/Storyboard*Worflow.png)
  
# Features
  ![use-bot](https://github.com/ak-b/TeamsBot/blob/master/images/bot_features.png)

# Usage

1. The easiest way to use this module is to set a few environment variables

    > Note: See [ngrok](#ngrok) for details on setting up an easy HTTP tunnel for development.

    ```
    export TEAMS_BOT_URL=<url for the location the bot is hosted>
    export TEAMS_BOT_TOKEN=<your bots token>
    export TEAMS_BOT_EMAIL=<marvinh@webex.bot>
    export TEAMS_BOT_APP_NAME=<Marvin>
    ```

1. A basic bot requires very little code to get going.  

    ```python
    import os
    from webexteamsbot import TeamsBot

    # Retrieve required details from environment variables
    bot_email = os.getenv("TEAMS_BOT_EMAIL")
    teams_token = os.getenv("TEAMS_BOT_TOKEN")
    bot_url = os.getenv("TEAMS_BOT_URL")
    bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")

    # Create a Bot Object
    bot = TeamsBot(
        bot_app_name,
        teams_bot_token=teams_token,
        teams_bot_url=bot_url,
        teams_bot_email=bot_email,
    )


    # A simple command that returns a basic string that will be sent as a reply
    def do_something(incoming_msg):
        """
        Sample function to do some action.
        :param incoming_msg: The incoming message object from Teams
        :return: A text or markdown based reply
        """
        return "i did what you said - {}".format(incoming_msg.text)


    # Add new commands to the box.
    bot.add_command("/dosomething", "help for do something", do_something)


    if __name__ == "__main__":
        # Run Bot
        bot.run(host="0.0.0.0", port=5000)
    ```

1. A [sample script](https://github.com/ak-b/TeamsBot/blob/master/skills.py) that shows more advanced bot features and customization is also provided in the repo.  


# ngrok

[ngrok](http://ngrok.com) will make easy for you to develop your code with a live bot.

You can find installation instructions here: [https://ngrok.com/download](https://ngrok.com/download)

1. After you've installed `ngrok`, in another window start the service

    ```
    ngrok http 5000
    ```

2. You should see a screen that looks like this:

    ```
    ngrok by @inconshreveable                                                                                                                                 (Ctrl+C to quit)

    Session Status                online
    Session Expires               4 hours, 40 minutes
    Version                       2.3.34
    Region                        United States (us) 
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://d042f48b.ngrok.io -> http://
    Forwarding                    https://d042f48b.ngrok.io -> http:/

    Connections                   ttl     opn     rt1     rt5     p50
                                  76      0       0.00    0.00    1.5

    HTTP Requests
    -------------

    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
    POST /                         200 OK
```

3. Make sure and update your environment with this url:

    ```
    export TEAMS_BOT_URL=<>

    ```

4. Now launch your bot!!

    ```
    python sample.py
    ```

## Local Development

If you have an idea for a feature you would like to see, we gladly accept pull requests.  To get started developing, simply run the following..

```
git clone https://github.com/ak-b/TeamsBot.git
cd TeamsBot
pip3 install -r requirements_dev.txt
python setup.py develop
```



This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.

