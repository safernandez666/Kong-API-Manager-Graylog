#!/usr/bin/env python3
import json
import sys

# Function that prints text to standard error
def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Main function
if __name__ == "__main__":

    # Print out all input arguments.
    sys.stdout.write("All Arguments Passed In: " + ' '.join(sys.argv[1:]) + "\n")

    # Turn stdin.readlines() array into a string
    std_in_string = ''.join(sys.stdin.readlines())

    # Load JSON
    event_data = json.loads(std_in_string)

    # Extract some values from the JSON.
    sys.stdout.write("Values from JSON: \n")
    sys.stdout.write("Event Source: " + event_data["event_source"] + "\n")

    # Extract Message Backlog field from JSON.
    sys.stdout.write("\nBacklog:\n")
    for message in event_data["backlog"]:
        for field in message.keys():
            sys.stdout.write("Field: " + field + "\t")
            sys.stdout.write("Value: " + str(message[field]) + "\n")

    # Write to stderr if desired
    # print_stderr("Test return through standard error")

    # Return an exit value. Zero is success, non-zero indicates failure.
    exit(0)