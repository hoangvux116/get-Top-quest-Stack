import requests
import json
import log
import argparse
logger = log.get_logger(__name__)


def top_question(N, LABEL):
    URL = 'https://api.stackexchange.com//2.2/questions?pagesize={}&order=desc&sort=votes&tagged={}&site=stackoverflow'  # NOQA
    ses = requests.Session()
    resp = ses.get(URL.format(N, LABEL))
    if resp.status_code == 200:
        contents = json.loads(resp.text)['items']
        count = 0
        if not contents:
            print('Need to input valid Number and Label - '
                  'format int and str-str')
        else:
            for idx, data in enumerate(contents):
                count += 1
                print('Question {}: '.format(count) + contents[idx]['title']
                      + (' - Asker: ') + contents[idx]['owner']['display_name']
                      + '\n' + '--> Link: ' + contents[idx]['link'])


def main():
    parse = argparse.ArgumentParser(
        description="Get top question in stackoverflow.con")
    parse.add_argument('N', type=int, help='Number of Question')
    parse.add_argument('LABEL', type=str,
                       help='Input your keyword with sympol \- as whitespace')
    input_data = parse.parse_args()
    print(top_question(input_data.N, input_data.LABEL))


if __name__ == "__main__":
    main()
