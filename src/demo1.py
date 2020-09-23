"""
Simple demo of how to make connection to SG and retrieve user info
"""
import os
import dotenv
import shotgun_api3

dotenv.load_dotenv('.env')
SG = shotgun_api3.Shotgun(
    os.environ['SERVER'],
    os.environ['SCRIPT_NAME'],
    os.environ['API_KEY']
)

def main():
    result = SG.find_one("HumanUser", [['login', 'is', 'anoop']], ['login', 'email'])
    for key, value in result.iteritems():
        print key, value

if __name__ == "__main__":
    main()