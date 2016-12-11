from flask import Flask, render_template, render_template, request, redirect, session
from HTMLParser import HTMLParser
import urllib2
import sys
from random import randint
app = Flask(__name__)

@app.route("/ninja/")
def ninja():
    return render_template("ninja.html", python_zen=python_zen)

@app.route("/ninja/<vararg>")
def handler_function(vararg):
  print vararg
  if vararg == "":
      vararg = "default"
  return render_template("ninja.html", color=vararg, python_zen=python_zen)

# @app.route("/users/<vararg>")
# def handler_function(vararg):
#   # here you can use the variable "vararg"
#   # if you want to see what our argument looks like
#   print vararg
#   # we could do other things with this information from this point on such as:
#   # use it to retrieve some records from the database
#   # render a particular template
#   return render_template("user.html", username=vararg)

@app.route("/")
def index():
    test_html = "<h1>Parse HTML</h1>"
    my_html = test_html
    # my_html=cleanupString(test_html)
    return render_template("start.html", python_zen=python_zen, my_html = test_html)

@app.route("/notes")
def notes():
    return render_template("notes.html", python_zen=python_zen)

python_zens = ["Beautiful is better than ugly.",
                "Explicit is better than implicit.",
                "Simple is better than complex.",
                "Complex is better than complicated.",
                "Flat is better than nested.",
                "Sparse is better than dense.",
                "Readability counts.",
                "Special cases aren't special enough to break the rules.",
                "Although practicality beats purity.",
                "Errors should never pass silently.",
                "(Errors should never pass silently.) Unless explicitly silenced.",
                "In the face of ambiguity, refuse the temptation to guess.",
                "There should be one-- and preferably only one --obvious way to do it.",
                "Although that way may not be obvious at first unless you're Dutch.",
                "Now is better than never.",
                "Although never is often better than *right* now.",
                "If the implementation is hard to explain, it's a bad idea.",
                "If the implementation is easy to explain, it may be a good idea.",
                "Namespaces are one honking great idea -- let's do more of those.",]
random_number = randint(0,len(python_zens)-1)
python_zen = python_zens[random_number]
# session['python'] = python_zen

# Trying to find a way to send html that is displayed as html
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')



class MLStripper(HTMLParser):
    #This strips html, but that isn't really what I'm looking for.
    def __init__(self):
        # initialize the base class
        HTMLParser.__init__(self)

    def read(self, data):
        # clear the current output before re-use
        self._lines = []
        # re-set the parser's state before re-use
        self.reset()
        self.feed(data)
        return ''.join(self._lines)

    def handle_data(self, d):
        self._lines.append(d)

def strip_tags(html):
    s = MLStripper()
    return s.read(html)

html = """Python's <code>easy_install</code>
 makes installing new packages extremely convenient.
 However, as far as I can tell, it doesn't implement
 the other common features of a dependency manager -
 listing and removing installed packages."""

# print strip_tags(html)

app.run(debug=True)
