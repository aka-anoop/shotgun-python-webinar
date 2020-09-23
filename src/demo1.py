"""
Simple demo of how to make connection to SG and retrieve user info
"""
import os
import click
import dotenv
import shotgun_api3

# Loads environment from .env file. If you encounter error below, check the README for instructions 
dotenv.load_dotenv('.env')
SG = shotgun_api3.Shotgun(
    os.environ['SERVER'],
    os.environ['SCRIPT_NAME'],
    os.environ['API_KEY']
)

@click.command()
@click.argument('username')
def main(username):
    """
    Retrieves a single user with a matching user name.
    """
    user_result = SG.find_one(
        "HumanUser", 
        [['login', 'is', username]],
        ['login', 'email', 'department.Department.code', 'department.Department.name']
        )
    for key, value in user_result.iteritems():
        print key, value

if __name__ == "__main__":
    main()