# The changegame.py script is built to simply change the game you a twitch streamer. The script uses the Twitch API to 
# change the name of the game to whatever the user wants it to be. This script requires python to be installed on your machine.

# Change Log
# 5-5-2020 - Original Publication
# 5-7-2020 - Changes made to include the client ID of the OAuth Token as part of the authentication to get their twitch ID, the 
#            The section of code marked Get Client-ID of OAuth Token was added to retrieve the Client ID. Additional comments were
#            also added

# Libraries to import
import json
import requests
import sys
import getopt

# Twitch OAuth Code
oauth = '' # Enter access token that is generated from twitchtokengenerator.com

# Body of Script
def main(argv):
    gamename = ' '
    try:
      opts, args = getopt.getopt(argv,"g:")
    except getopt.GetoptError:
      print ('Failed')
      sys.exit(2)
      
    # Get Client-ID of OAuth Token
    idheaders = {
        'Authorization': 'OAuth ' + oauth,
    }
    idresponse = requests.get('https://id.twitch.tv/oauth2/validate', headers=idheaders)
    data = idresponse.json()
    idjsondump = json.dumps(data)
    idjsondata = json.loads(idjsondump)
    client_id = idjsondata['client_id']
    
    # Get Twitch ID Number
    headers = {
        'Authorization': 'Bearer ' + oauth,
        'Client-ID': client_id
    }
    response = requests.get('https://api.twitch.tv/helix/users', headers=headers)
    data = response.json()
    jsondump = json.dumps(data)
    jsondata = json.loads(jsondump)
    print(jsondata)
    id = jsondata['data'][0]['id']

    # Change Game
    for opt, arg in opts:
      if opt in ("-g"):
        gamename = arg
      else:
        sys.exit(0)
        
    gameheaders = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Authorization': 'OAuth ' + oauth,
        'Content-Type': 'application/json',
    }

    gamedata = '{"channel": {"game": "' + gamename + '", "channel_feed_enabled": true}}'

    response = requests.put("https://api.twitch.tv/v5/channels/{}".format(id), headers=gameheaders, data=gamedata)

if __name__ == "__main__":
    main(sys.argv[1:])
