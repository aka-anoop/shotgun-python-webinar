"""
Sample code for uploading a movie as a Version linked to specific task
"""
import os
import sys
import click
import dotenv
import shotgun_api3
ca_certs = "venv/lib/python2.7/site-packages/shotgun_api3/lib/httplib2/python2/cacerts.txt"

dotenv.load_dotenv('.env')
SG = shotgun_api3.Shotgun(
    os.environ['SERVER'],
    os.environ['SCRIPT_NAME'],
    os.environ['API_KEY'],
    ca_certs=ca_certs
)

@click.command()
@click.argument('movie', type=click.Path(exists=True))
@click.option('-login', default="anoop")
def main(movie, login):
    user_result = SG.find_one(
        "HumanUser", 
        [['login', 'is', login]], 
        []
        )
    tasks_result = SG.find(
        "Task",
        [['task_assignees', 'in', user_result]],
        ['content', 'entity.Asset.code', 'project']
    )
    prompt_message = ""
    for i in range(0, len(tasks_result)):
        prompt_message += "\n" + str(i+1) + ":" + tasks_result[i]['entity.Asset.code'] + "-" + tasks_result[i]['content']    
    
    click.echo(prompt_message)
    choice = click.prompt("Select the Task you want to upload the movie to", type=int)
    if choice not in range(1, len(tasks_result) + 1):
        click.echo("Wrong task id selected!")
        sys.exit(1)

    display_name = click.prompt("Enter display name of the version", type=str)

    task = tasks_result[choice - 1]
    data = {"sg_task": task, 'project': task['project'], 'code': display_name}
    new_version = SG.create(
        "Version",
        data,
    )
    click.echo("Uploading {mov} to Shotgun.".format(mov=movie))
    SG.upload(
        "Version",
        new_version['id'],
        movie,
        field_name="sg_uploaded_movie",
        display_name=display_name
    )
    click.echo("Successfully uploaded {mov} to Shotgun.".format(mov=movie))

if __name__ == "__main__":
    main()