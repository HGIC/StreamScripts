# Config portion
import socket
import sys
import getopt


def main(argv):
    texttotype = ' '
    try:
      opts, args = getopt.getopt(argv,"t:u:")
    except getopt.GetoptError:
      print ('Failed')
      sys.exit(2)
      
    for opt, arg in opts:
      if opt in ("-t"):
        texttotype = arg
      else
        sys.exit(2)
    
    NICK = ""  # your twitch username, lowercase
    PASS = ""  #Enter access token that is generated from twitchtokengenerator.com
    
    HOST = "irc.chat.twitch.tv"  # the twitch irc server
    PORT = 6667  # always use port 6667
    CHAN = "#"  # your twitch channel name must include #

    
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes('PASS ' + PASS + '\r\n', 'utf-8'))
    s.send(bytes('NICK ' + NICK + '\r\n', 'utf-8'))
    s.send(bytes('JOIN ' + CHAN + '\r\n', 'utf-8'))

    s.send(bytes('PRIVMSG ' + CHAN + ' :' + texttotype + '\r\n', 'utf-8'))


if __name__ == "__main__":
    main(sys.argv[1:])