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


def find_consecutive_runs(provided, target_run_length=3):
    # implement a function here that returns
    # the list of indices where consecutive runs
    # begin

    # Assume 'provided' is a list of integers per instruction.
    found_run_indices = []

    for start_idx, _ in enumerate(provided):
        end_idx = target_run_length + start_idx
        slice_to_evaluate = provided[start_idx:end_idx]

        # Not enough integers to make the target run length.
        if len(slice_to_evaluate) < target_run_length:
            break

        made_run_length = 0
        target_increment = None
        last_num = None
        for curr_num in slice_to_evaluate:
            # First number in slice to evaluate, move onto next number.
            if last_num is None:
                last_num = curr_num
                made_run_length += 1
                continue

            # Not consecutive regardless of the direction, move onto next slice.
            diff = curr_num - last_num
            if abs(diff) != 1:
                break

            # Identified increment and its direction for this slice.
            if target_increment is None:
                target_increment = diff

            if diff == target_increment:
                # Consecutive and consistent in its direction.
                made_run_length += 1
                last_num = curr_num
            else:
                # Consecutive but direction changed, move onto next slice.
                break

        if made_run_length == target_run_length:
            found_run_indices.append(start_idx)

    if found_run_indices:
        return found_run_indices

    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')
