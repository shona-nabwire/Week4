import click
import json
import urllib3
import requests

newsapikey = '98c49d6124d547ed8e42a05b2915f26a'

@click.command()
def news_search():
    sourceslist = ['ABC News', 'Associated Press', 'BBC News', 'Mirror', 'NBC News']
    print('\n'.join(sourceslist))

    sourcechoice = input('Please enter a newsource from the previous list: ')
    news_source = sourcechoice.lower()
    news_source = sourcechoice.replace(' ','-')
    url = 'https://newsapi.org/v2/top-headlines?sources=' + news_source + '&apiKey=98c49d6124d547ed8e42a05b2915f26a'
    openurl = urllib3.PoolManager()
    response = openurl.request('GET',url)
    headlinesdata = json.loads(response.data.decode('utf-8'))
    list1 = headlinesdata['articles']
    for item in list1[0:10]:
        click.echo('\n')
        click.echo(item['title'])
        click.echo('\n')
        click.echo(item['description']) 
        click.echo('\n')
        click.echo(item['url'])

if __name__ == '__main__':
    news_search()