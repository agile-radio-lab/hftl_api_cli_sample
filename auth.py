__author__ = "Igor Kim"
__credits__ = ["Igor Kim"]
__maintainer__ = "Igor Kim"
__email__ = "kim@hft-leipzig.de"
__status__ = "Development"
__date__ = "11/2019"
__license__ = "MIT"

import requests
import argparse

DEFAULT_API_URL = "https://api.otc.roundeasy.ru/"

parser = argparse.ArgumentParser(description='Update HfTL API session')
parser.add_argument('--api-url', type=str,
                    default=DEFAULT_API_URL, help='API URL')
parser.add_argument('--user-id', type=str, help='User ID')
parser.add_argument('--password', type=str, help='Password')

args = parser.parse_args()


def main():
    headers = {'content-type': 'application/json'}
    auth_url = "%s/auth" % (args.api_url)
    print("Connecting to %s...\n" % args.api_url)

    resp = requests.post(auth_url, headers=headers, json={
                         "userID": args.user_id, "password": args.password})
    if resp.status_code == 200:
        token = resp.json()
        print("Success [%d]" % resp.status_code)
        print("Your token is %s" % token["token"])
    else:
        print("Failed! Response [%d]" % resp.status_code)


if __name__ == "__main__":
    main()
