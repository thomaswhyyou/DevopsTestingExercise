# Find consecutive runs!

First, write a python function that accepts as an argument a list of integers.  It must
find in that list all runs of 3 consecutive numbers that increase or decrease by 1.  It
should return the list indices of the first element of each run.  If there are no consecutive
runs, this should return None

Example:  [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7] would return [0, 4, 6, 7]

# Move it to the web!

This is a simple flask project designed for you to insert the results of your
find consecutive runs project and build a small test suite

It requires docker and docker-compose for infrastructure.

Instructions for installing Docker can be found [here](https://docs.docker.com/installation/)

The first thing to figure out after installing docker is the url you can access it at.  If you
are running linux and installed it locally, that will be `localhost`.  Otherwise, if you followed
the directions, docker is running on a local virtual machine.  You can see info about that machine
with `docker-machine ls`.  This will tell you the URL for your machine (which will be named "default")

Once everything is installed, you can launch your webapp with `docker-compose up -d`.  
The app will be listening on port 5000 at the url docker is on.  For example, if the url is 
tcp://192.168.99.101:2376, you can acess the webapp at http://192.168.99.101:5000.  (This should
return "no list was provided")

You can post a list to that url to feed it to your function like so...
`curl -H "Content-Type: application/json" -X POST -d '{"list":"[1, 2, 3, 4]"}' http://192.168.99.101:5000/`

(if your function works, that should respond "[0, 1]")

Build your test suite in find_consecutive_runs_tests.py.  You can run your suite with
`docker-compose -f docker-compose-test.yml run test`.  This runs the tests
and the webapp in seperate docker containers.  From within your tests you can access
the web server at "web:5000" (instead of "localhost:5000" or whatever you use from your
machine).

Your tests should both test the correctness of your function (unit tests) as well as
the integration with the flask framework.  Feel free to use any third party libraries
you feel could be useful (install them in your docker container by adding them to requirements.txt and
running `docker-compose build`)

Please fork this repo and open a pull request with your changes.

Thanks!
