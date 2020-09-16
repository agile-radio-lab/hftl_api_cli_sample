__author__ = "Igor Kim"
__credits__ = ["Igor Kim"]
__maintainer__ = "Igor Kim"
__email__ = "igor.kim@htwk-leipzig.de"
__status__ = "Development"
__date__ = "11/2019"
__license__ = "MIT"

import requests
import argparse

DEFAULT_API_URL = "https://rest.radiolab-dev0.beagile.one/"

parser = argparse.ArgumentParser(description='Update HfTL API session')
parser.add_argument('--token', type=str, required=True, help='API Token')
parser.add_argument('--sid', type=str, required=True, help='SessionID')
parser.add_argument('--api-url', type=str,
                    default=DEFAULT_API_URL, help='API URL')
parser.add_argument('--desc', type=str, help='API URL')

args = parser.parse_args()


def pop_immutable(obj):
    keys = ["_id", "createdAt", "modifiedAt"]
    for k in keys:
        if not k in obj:
            continue
        obj.pop(k)


def main():
    headers = {'content-type': 'application/json', "X-API-Key": args.token}
    session_url = "%s/sessions/%s" % (args.api_url, args.sid)
    print("Connecting to %s...\n" % args.api_url)

    resp = requests.get(session_url, headers=headers)
    if resp.status_code == 401:
        print("Invalid token, issue your token:\n\thttps://rest-api-web-auth.now.sh")
        return
    if resp.status_code == 404:
        print("Session %s not found" % args.sid)
        return
    print("Session found, changing description...")
    sess = resp.json()
    pop_immutable(sess)
    sess["description"] = args.desc

    resp = requests.put(session_url, headers=headers, json=sess)
    if resp.status_code == 200:
        print("Success [%d]" % resp.status_code)
    else:
        print("Failed! Response [%d]" % resp.status_code)


if __name__ == "__main__":
    main()
