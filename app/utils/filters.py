def format_date(date):
  return date.strftime('%m/%d/%y')
# The format_date() function expects to receive a datetime object and then use the strftime() method to convert it to a string. 
# The %m/%d/%y format code will result in something like "01/01/20". 
# For more information, refer to the Python documentation on strftime() and strptime() format codes.

from datetime import datetime
print(format_date(datetime.now()))

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]
# This code removes all extraneous information from a URL string, leaving only the domain name. 
# Note that the methods we use, like replace() and split(), behave exactly the same as they do in JavaScript.  

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word
