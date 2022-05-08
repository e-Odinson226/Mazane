import requests as req
re = req.request('GET', 'https://stackoverflow.com/questions/69503329/pip-is-not-working-for-python-3-10-on-ubuntu')
#---------------Driver---------------
try:
    print(re.status_code)
except:
    raise Exception