from flask import Flask
from flask import render_template
app = Flask(__name__)

from src.Managers.ReposManager import ReposManager
from src.Repositories.GithubApiRepository import GithubApiRepository

from pprint import pprint

@app.route("/")
def hello():

    # Manage the repos through the manager
    #
    # The repos manager can work with any repository
    # that implements the Repository Interface which gives
    # us the freedom to swap the repositories at any given moment
    reposManager = ReposManager(GithubApiRepository())
    repos = reposManager.getAllVladetdRepos()
    pprint(repos)

    return render_template('index.html', repos=repos)
