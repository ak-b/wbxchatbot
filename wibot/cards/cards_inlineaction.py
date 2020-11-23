def get_in():

  payload = {
      "contentType": "application/vnd.microsoft.card.adaptive",
          "content":{
              "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
              "type": "AdaptiveCard",
              "version": "1.1",
              "body": [
                {
                  "type": "TextBlock",
                  "text": "Media supports **audio** and **video** content!",
                },
                {
                  "type": "TextBlock",
                  "text": "Video",
                  "horizontalAlignment": "center",
                  "spacing": "medium",
                  "size": "large"
                },
                {
                  "type": "Media",
                  "poster": "https://adaptivecards.io/content/poster-video.png",
                  "sources": [{
                    "mimeType": "video/mp4",
                    "url": "https://adaptivecardsblob.blob.core.windows.net/assets/AdaptiveCardsOverviewVideo.mp4"
                  }]
                },
                {
                  "type": "TextBlock",
                  "text": "Audio",
                  "horizontalAlignment": "center",
                  "size": "large"
                },
                {
                  "type": "Media",
                  "poster": "https://adaptivecards.io/content/poster-audio.jpg",
                  "sources": [{
                    "mimeType": "audio/mpeg",
                    "url": "https://adaptivecardsblob.blob.core.windows.net/assets/AdaptiveCardsOverviewVideo.mp3"
                  }]
                }
              ]
            }

          }

  return payload 
