This is a simple flask project designed for you to insert the results of your
find consecutive runs project and build an small test suite

It requires docker and docker-compose for infrastructure.

Once everything is installed, you can launch your webapp with docker-compose up -d.  
The app will be listening on port 5000 on the machine your docker daemon is on...
localhost if you're running linux and installed it locally, or the ip of the vm
that is installed on OSX or Windows.  Your installation method will have instructions
on how to get the ip.

CURL localhost:5000 should return "no list was provided" as is.

Posting a list as json should return the results from your function.

Build your test suite in find_consecutive_runs_tests.py.  You can run your suite with
`docker-compose -f docker-compose-test.yml run test`.  This runs the tests
and the webapp in seperate docker containers.  From within your tests you can access
the web server at "web:5000" (instead of "localhost:5000" or whatever you use from your
machine).

Your tests should both test the correctness of your function (unit tests) as well as
the integration with the flask framework.

Please fork this repo and open a pull request with your changes.

Thanks!
