def get_gen_msg():

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
			                            "text": "Webex Security Bot Cards Release",
			                            "horizontalAlignment": "Left",
			                            "color": "Light",
			                            "size": "Large",
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
			                            "text": "Release Date:",
			                            "color": "Light"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Product:",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Marvin's User Guide:",
			                            "weight": "Lighter",
			                            "color": "Light",
			                            "spacing": "Small"
			                        }
			                    ]
			                },
			                {
			                    "type": "Column",
			                    "width": 65,
			                    "items": [
			                        {
			                            "type": "TextBlock",
			                            "text": "Oct 15, 2020",
			                            "color": "Light"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Webex Teams Bot",
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
			            "text": "We're making it easier for you to interact with Marvin ",
			        },
			        {
			            "type": "TextBlock",
			            "text": "Bot Resources:",
                        "color": "Light",
                        "weight": "Lighter",
                    	"spacing": "Small"
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