import requests
import json

def search_github(query):
  # Send a request to the GitHub API to search for repositories
  r = requests.get(f'https://api.github.com/search/repositories?q={query}')

  # Get the list of repositories
  repositories = r.json()['items']

  repo_data = []

  #  extract the relevant data from repo
  for repo in repositories:
    name = repo['name']
    description = repo['description']
    url = repo['html_url']
    data = {'name': name, 'description': description, 'url': url}
    repo_data.append(data)

  # Convert the repo data to JSON data formatting
  repo_data_json = json.dumps(repo_data, indent=2)

  return repo_data_json

def print_github_data(github_data_json):
  # Parse the JSON data into a Python object
  github_data = json.loads(github_data_json)

  # print it in a nice format
  for repo in github_data:
    print(f'Name: {repo["name"]}')
    print(f'Description: {repo["description"]}')
    print(f'URL: {repo["url"]}')

def main():
  query = input('Enter a search query: ')
  github_data_json = search_github(query)
  print_github_data(github_data_json)

if __name__ == '__main__':
  main()
