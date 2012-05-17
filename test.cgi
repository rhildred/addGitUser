#!/bin/sh
echo "Content-type: text/html"
echo ""

# our html code
echo "<html>"
echo "<head><title>My FOX page</title></head>"
echo "<body>"
echo "<h1>Welcome to my FOX Board web page</h1>"
echo "Hello World ! <br/>"
echo "<pre>"
env
echo "</pre>"
echo "</body>"
echo "</html>"