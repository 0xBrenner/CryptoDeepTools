#!/usr/bin/python

import sys
from lib.brainwallet import private_key, public_key
# from lib.secp256k1 import secp256k1

if __name__ == "__main__":
    
    phrase = str(sys.argv[1])
  
    print(str( "pass phrase: " + phrase))
    print(str( "private key: " + private_key(phrase)))
    print(str( "BTC address: " + public_key(phrase)))
