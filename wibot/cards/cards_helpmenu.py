def get_menu():

    payload = {
        "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
    			"type": "AdaptiveCard",
			    "body": [
			        {
			            "type": "ColumnSet",
			            "columns": [
			                {
			                    "type": "Column",
			                    "items": [
			                        {
			                            "type": "Image",
			                            "style": "Person",
			                            "url": "https://developer.webex.com/images/webex-teams-logo.png",
			                            "size": "Medium",
			                            "height": "50px"
			                        }
			                    ],
			                    "width": "auto"
			                },
			                {
			                    "type": "Column",
			                    "items": [
			                        {
			                            "type": "TextBlock",
			                            "text": "Cisco Webex Iaas Firewall",
			                            "weight": "Lighter",
			                            "color": "Accent"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "weight": "Bolder",
			                            "text": "Webex Security Bot Help Menu",
			                            "horizontalAlignment": "Left",
			                            "color": "Light",
			                            "size": "Large",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "weight": "Medium",
			                            "text": "Features Supoorted",
			                            "horizontalAlignment": "Left",
			                            "color": "Accent",
			                            "spacing": "Small"
			                        }
			                    ],
			                    "width": "stretch"
			                }
			            ]
			        },
			        {
			            "type": "ColumnSet",
			            "columns": [
			                {
			                    "type": "Column",
			                    "width": 35,
			                    "items": [
			                        {
			                            "type": "TextBlock",
			                            "text": "Command",
			                            "weight": "Light",
			                            "color": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "search acl",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "search acl106",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "search eureka",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "search ipi",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "search port_status",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "logs",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
		                        	{
			                            "type": "TextBlock",
			                            "text": "captures",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "cfgdiff ",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "codescan",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "contexts",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
		                        	{
			                            "type": "TextBlock",
			                            "text": "cpualert",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "dryrun",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "embaudit",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "enable_mmp",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
		                        	{
			                            "type": "TextBlock",
			                            "text": "feed-wl",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "fragment",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "health",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "intbuffer",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },

			                        {
			                            "type": "TextBlock",
			                            "text": "pwrscan",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "remove-feed",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        }
			                    ]
			                },
			                {
			                    "type": "Column",
			                    "width": 82,
			                    "items": [
			                        {
			                            "type": "TextBlock",
			                            "text": "Functionality",
			                            "weight": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search ACL",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search ACL106",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search if Eureka Ports are Open",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search for IPBlock in IP intelligence DB",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search for Embryonic Connection Logs",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search Port Status",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Check Captures",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "View Config Changes in the past 24hrs",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "View ASA Software Code Version",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "View Contexts",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        			                        {
			                            "type": "TextBlock",
			                            "text": "View devices:CPU > x% in the past 24hrs",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "**Dryrun Global Configuration Changes**",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        			                        {
			                            "type": "TextBlock",
			                            "text": "Embryonic Connection & PerHost Settings",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "**Trigger Global NS MMP Config Push**",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Add IP to Whitelist on FeedServer",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Fragment Stats on Core in LHR &SJC",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Firewall healthchecks",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "View Interface Buffer Status",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Check PSU and Fan Health",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Remove IP from Whitelist on Feedserver",
			                            "color": "Light",
			                            "weight": "Lighter",
			                            "spacing": "Small"
			                        }

			                    ]
			                }
			            ],
			            "spacing": "Padding",
			            "horizontalAlignment": "Center"
			        },
	                {
	                    "type": "TextBlock",
	                    "text": "[User Guide](https://wiki.cisco.com/display/AS13445/Usage+Guide)"
	                },
			    ],
			    "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
			    "version": "1.2"
			    }
		    }
    return payload