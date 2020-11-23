def get_misc_docs():
    payload = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content":
            {
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
                                        "text": "Cisco Webex IaaS Firewall",
                                        "weight": "Lighter",
                                        "color": "Accent"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "weight": "Bolder",
                                        "text": "ASA Firewall Notification",
                                        "horizontalAlignment": "Left",
                                        "color": "Light",
                                        "size": "Medium",
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
                                "width": 40,
                                "items": [
                                    {
                                        "type": "TextBlock",
                                        "text": "Firewall:",
                                        "weight": "Bolder",
                                        "color": "Light",
                                        "spacing": "Small"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "text": "DC/stack:",
                                        "weight": "Bolder",
                                        "color": "Light",
                                        "spacing": "Small"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "text": "CPU utilization (%):",
                                        "weight": "Bolder",
                                        "color": "Light",
                                        "spacing": "Small"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "text": "Memory utilization(%):",
                                        "weight": "Bolder",
                                        "color": "Light",
                                        "spacing": "Small"
                                    }
                                ]
                            },
                            {
                                "type": "Column",
                                "width": 60,
                                "items": [
                                    {
                                        "type": "TextBlock",
                                        "text": "{{ info['cluster'] }}",
                                        "weight": "Lighter",
                                        "color": "Light",
                                        "spacing": "Small"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "text": "{{ info['cpu'] }}",
                                        "weight": "Lighter",
                                        "color": "Light",
                                        "spacing": "Small"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "text": "{{ info['memory] }}",
                                        "weight": "Lighter",
                                        "color": "Light",
                                        "spacing": "Small"
                                    },
                                    {
                                        "type": "TextBlock",
                                        "text": "{{ info['rx/tx'] }}",
                                        "weight": "Lighter",
                                        "color": "Light",
                                        "spacing": "Small"
                                    }
                                ],
                                "horizontalAlignment": "Left"
                            }
                        ],
                        "spacing": "Padding",
                        "horizontalAlignment": "Left"
                    },
                    {
                        "type": "Container",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "{{ info['info'] }}",
                            },
                            {
                                "type": "TextBlock",
                                "text": "[Click here to view graphs]({{ info['api_url'] }})"
                            }
                        ],
                        "style": "emphasis"
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2"
            }
    }
    return payload
