from urllib.request import urlopen
f = urlopen("https://openssl.org")
print(f.read()[:100])