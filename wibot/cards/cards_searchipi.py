def search_ipi():

    payload = {
        "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
    			"type": "AdaptiveCard",
    		    "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
			    "version": "1.2",
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
			                            "text": "Search IP Reputation Database",
			                            "horizontalAlignment": "Left",
			                            "color": "Light",
			                            "size": "Large",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Search IPI",
			                            "weight": "Lighter",
			                            "color": "Accent"
			                        },
			                        {
							            "type": "Input.Text",
							            "placeholder": "Enter IP",
							            "style": "text",
							            "maxLength": 0,
							            "id": "TextFieldVal"
							        },
			                    ],
			                    "width": "stretch"
			                }
			            ]
			        },
			    ],
			    "actions": [
			        {
			            "type": "Action.Submit",
			            "title": "Submit",
			            "data": {
			                "formDemoAction": "Submit"
			            }
			        }
			    ]

			    }
		    }
    return payload