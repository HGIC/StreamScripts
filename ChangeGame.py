import json
import requests
import sys
import getopt

oauth = '' # Enter access token that is generated from twitchtokengenerator.com between the apostrophes 


def main(argv):
    gamename = ' '
    try:
      opts, args = getopt.getopt(argv,"g:")
    except getopt.GetoptError:
      print ('Failed')
      sys.exit(2)
      
    # Get Twitch ID
    headers = {
        'Authorization': 'Bearer ' + oauth,
    }
    response = requests.get('https://api.twitch.tv/helix/users', headers=headers)
    data = response.json()
    jsondump = json.dumps(data)
    jsondata = json.loads(jsondump)
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
