def alerts():
    payload = {
        "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "version": "1.0",
                "body": [
                    {
                        "type": "Container",
                        "horizontalAlignment": "Center",
                        "items": [
                            {
                                "type": "ColumnSet",
                                "columns": [
                                    {
                                        "type": "Column",
                                        "width": "stretch",
                                        "items": [
                                            {
                                                "type": "Image",
                                                "style": "Person",
                                                "url": "https://developer.webex.com/images/webex-teams-logo.png",
                                                "size": "Medium",
                                                "height": "50px"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "Cisco Webex IaaS Firewall",
                                                "horizontalAlignment": "Left",
                                                "weight": "Lighter",
                                                "color": "Accent"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "Firewall Monitoring Logs from CLP",
                                                "horizontalAlignment": "Left",
                                                "size": "Large",
                                                "color": "Medium",
                                                "weight": "Bolder"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "Message: ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "Logsource: ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },

                                            {
                                                "type": "TextBlock",
                                                "text": "Host:",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "Timestamp: ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },
                                        ],
                                        "horizontalAlignment": "Center",
                                        "verticalContentAlignment": "Center"
                                    }
                                ]
                            },
                            {
                                "type": "TextBlock",
                                "text": "[Click to View on Kibana](https://mtsj1sww001.webex.com/Orion/SummaryView.aspx?ViewID=476)"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Triggered by : CLP",
                                "weight": "Bolder",
                                "color": "Darker",
                                "spacing": "Small"
                            },
                        ],
                        "style": "accent"
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
        }
    }
    return payload