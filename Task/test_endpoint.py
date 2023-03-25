import urllib.request
contents = urllib.request.urlopen("http://127.0.0.1:8000/builds/?check-in=2022-12-07&check-out=2022-12-13&building=Tower1/").read()

assert b'[{"Number": 2, "Price": 3000.0, "Type": "S"}]' == contents
print('Test Passed!')