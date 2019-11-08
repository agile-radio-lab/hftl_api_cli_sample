# HfTL API Session Update Script

## Requirements
### Manual installation
```
pip install -r requirements.txt
```

### Using virtual environment
[More on virtual environments](https://docs.python.org/3/tutorial/venv.html)

The following commands are working for Linux and macOS with installed Python and virtualenv.

In the project folder:
```bash
virtualenv venv
source venv/
pip install -r requirements.txt
```

## Usage
First, you need to issue a token using `auth.py` script.
```
python auth.py --user-id={your userID here} --password={your password here}
```
e.g. `python auth.py --user-id=user --password=my_password`

If input is correct, as output of the script you get a token:
```
Your token is 2543d70839f3a934728b488aaaa410fa
```

This token should be used for any further requests.

`set-description.py` requires your authentication token `token`, `sessionID` and the description `desc` you want to set to the session:
```
python set_description.py --token={token} --sid={sessionID} --desc={desc}
```

For example:
```
python set_description.py --token=2543d70839f3a934728b488aaaa410fa --sid=test_session --desc="new description"
```