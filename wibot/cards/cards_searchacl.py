def search_acl():

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
			                            "horizontalAlignment": "Left",
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
			                            "horizontalAlignment": "Left",
			                            "weight": "Lighter",
			                            "color": "Accent"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "weight": "Bolder",
			                            "text": "Search ACL policies",
			                            "horizontalAlignment": "Left",
			                            "color": "Light",
			                            "size": "Large",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Webex Internal DC/DC",
			                            "horizontalAlignment": "Left",
			                            "weight": "Lighter",
			                            "color": "Accent"
			                        },
			                        {
							            "type": "Input.Text",
							            "placeholder": "Enter Source IP",
							            "horizontalAlignment": "Left",
							            "style": "text",
							            "maxLength": 0,
							            "id": "TextFieldVal"
							        },
							        {
							            "type": "Input.Text",
							            "placeholder": "Enter Destination IP",
							            "horizontalAlignment": "Left",
							            "style": "text",
							            "maxLength": 0,
							            "id": "TextFieldVal2"
							        },
							        {
							            "type": "Input.Text",
							            "placeholder": "Enter Port",
							            "horizontalAlignment": "Left",
							            "style": "text",
							            "maxLength": 0,
							            "id": "TextFieldVal3"
							        },
							        {
							            "type": "Input.ChoiceSet",
							            "placeholder": "Protocol",
							            "id": "ColorChoiceVal",
							            "horizontalAlignment": "Left",
							            "value": "Protocol/s",
							            "choices": [
							                {
							                    "title": "Protocol",
							                    "value": "Core"
							                },
							                {
							                    "title": "TCP",
							                    "value": "tcp"
							                },
							                {
							                    "title": "UDP",
							                    "value": "udp"
							                }
							            ]
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