import request

r = request.get('https://xkcd.com/353/')

print(dir(r))