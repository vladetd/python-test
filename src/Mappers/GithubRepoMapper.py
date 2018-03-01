import requests

class GithubRepoMapper:
    def map(self, entity):
        return {
            'id' : entity['id'],
            'name' : entity['name'],
            'url' : entity['html_url'],
            'avatar': self.getAvatar(entity['owner']['avatar_url'])
        }

    def getAvatar(self, url):
        result = requests.head(url)
        if result.status_code == requests.codes.ok:
            return url
        else:
            return None
