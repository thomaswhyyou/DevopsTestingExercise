import json

from flask import Flask, request, Response


app = Flask(__name__)


@app.route('/', methods=['GET', 'OPTIONS', 'POST'])
def return_consecutive_runs():

    try:
        data = json.loads(request.data)
        provided = data['list']
    except:
        return 'no list was provided'
    output = find_consecutive_runs(provided) or []
    return str(output)


def find_consecutive_runs(provided):
    # implement a function here that returns
    # the list of indices where consecutive runs
    # begin
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')
