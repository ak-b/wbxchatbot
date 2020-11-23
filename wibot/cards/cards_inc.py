def get_incident_triage_card():
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
                                                "text": "Firewall Incident Triage",
                                                "horizontalAlignment": "Left",
                                                "size": "Large",
                                                "color": "Medium",
                                                "weight": "Bolder"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": " ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": " ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },

                                            {
                                                "type": "TextBlock",
                                                "text": "Firewall Impacted: jfk01-edge0-asacl01.webex.com",
                                                "weight": "Bolder",
                                                "color": "Accent",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": " ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "DC/stack: JFK(NORAM) Edge ",
                                                "weight": "Bolder",
                                                "color": "Accent",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": " ",
                                                "weight": "Bolder",
                                                "color": "Light",
                                                "spacing": "Small"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": "Embryonic Connection Limit Breached",
                                                "weight": "Bolder",
                                                "color": "Darker",
                                                "spacing": "Medium"
                                            },
                                            {
                                                "type": "TextBlock",
                                                "text": " ",
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
                                "text": "[Firewall Health SummaryView](https://mtsj1sww001.webex.com/Orion/SummaryView.aspx?ViewID=237)\r",
                                "color": "Accent"
                            },
                            {
                                "type": "TextBlock",
                                "text": "[Click to View on Solarwinds](https://mtsj1sww001.webex.com/Orion/SummaryView.aspx?ViewID=476)"
                            },
                            {
                                "type": "TextBlock",
                                "text": " ",
                                "weight": "Bolder",
                                "color": "Light",
                                "spacing": "Small"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Triggered by : Solarwinds",
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