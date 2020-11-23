def get_input():

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
			                            "text": "Firewall Health Checks",
			                            "horizontalAlignment": "Left",
			                            "color": "Light",
			                            "size": "Large",
			                            "spacing": "Small"
			                        },
			                        {
			                            "type": "TextBlock",
			                            "text": "Show Commands",
			                            "weight": "Lighter",
			                            "color": "Accent"
			                        },
			                        {
							            "type": "Input.Text",
							            "placeholder": "Enter Firewall Name",
							            "style": "text",
							            "maxLength": 0,
							            "id": "TextFieldVal"
							        },
							        {
							            "type": "Input.ChoiceSet",
							            "id": "ColorChoiceVal",
							            "value": "Context/s",
							            "choices": [
							                {
							                    "title": "Contexts",
							                    "value": "Core"
							                },
							                {
							                    "title": "Core",
							                    "value": "Core"
							                },
							                {
							                    "title": "Infra",
							                    "value": "Infra"
							                },
							                {
							                    "title": "Admin",
							                    "value": "Admin"
							                },
							                {
							                    "title": "dc-mgmt",
							                    "value": "dc-mgmt"
							                },
							                {
							                    "title": "Connect",
							                    "value": "Connect"
							                },
							                {
							                    "title": "Openstack",
							                    "value": "Openstack"
							                },
							                {
							                    "title": "GSS",
							                    "value": "GSS"
							                },
							                {
							                    "title": "WEBEX",
							                    "value": "WEBEX"
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