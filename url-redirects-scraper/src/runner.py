thonimport requests
import json
from .redirector import follow_redirects
from .utils import load_urls_from_file

def process_urls(urls):
    result = []
    for url in urls:
        data = follow_redirects(url)
        result.append(data)
    return result

def main():
    urls = load_urls_from_file('data/urls.txt')
    result = process_urls(urls)
    with open('output.json', 'w') as outfile:
        json.dump(result, outfile, indent=4)

if __name__ == '__main__':
    main()