import urllib.request
import argparse
import datetime
import os
import shutil

def fetch_current_year():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    return year

def script_argument_parser(year):
    parser = argparse.ArgumentParser(
        description='Fetch Advent Of Code input data according to entered day and year.\n'
        'A valid Advent Of Code session cookie needs to be set as environment variable.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-c',
        '--cookie',
        required=False,
        dest='cookie',
        default=None,
        help='Overwrite your session cookie for the Advent Of Code website (default: None)',
        type=str
    )
    parser.add_argument(
        '-y',
        '--year',
        required=False,
        dest='year',
        default=year,
        help='Enter the preferred year (default: Current year)',
        type=str
    )
    parser.add_argument(
        '-d',
        '--day',
        required=False,
        dest='day',
        default=None,
        help='Enter the preferred day (default: None)',
        type=str
    )
    inputted_args = parser.parse_args()
    year = inputted_args.year
    day = inputted_args.day
    inputted_cookie = inputted_args.cookie
    if inputted_cookie is None:
        cookie = check_cookie_existence()
    else:
        cookie = "session={}".format(inputted_cookie)
    if day is None:
        day = input("Input requested day: ")
    return year, day, cookie

def fetch_aoc_data(script_arguments):
    year, day, cookie = script_arguments
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
           'Cookie': cookie}
    url = "https://adventofcode.com/{}/day/{}/input".format(year, day)
    try:
        req = urllib.request.Request(url, headers=hdr)
        http_response = urllib.request.urlopen(req)
        http_result = http_response.read().decode('utf-8')
        return http_result
    except urllib.error.HTTPError as http_error:
        print(http_error)
        print("Did you enter a valid cookie or set a valid AOC_COOKIE environment variable?")

class output_definer:
    def write_data_to_file(aoc_data, day):
        if aoc_data.endswith('\n'):
            print("Removing trailing newline.")
            aoc_data = aoc_data[:-1]
        folder_name = "Day {}".format(day)
        project_folder = os.path.join(os.curdir, folder_name)
        folder_exists_check = os.path.exists(project_folder)
        input_file_write_location = os.path.join(project_folder, "input_data.txt")
        input_file_exists_check = os.path.isfile(input_file_write_location)
        solution_file_write_location = os.path.join(os.curdir, 'templates', 'Solution.py')
        solution_file_exists_check = os.path.isfile(solution_file_write_location)

        def write_input_file():
            write_to_input_file = open(input_file_write_location, 'w')
            write_to_input_file.write(aoc_data)
            write_to_input_file.close()

        def write_solution_file():
            shutil.copy(solution_file_write_location, project_folder)

        if folder_exists_check:
            if input_file_exists_check:
                overwrite_input_file = str(input("Overwrite input file? y/(n): ") or 'n')
                if overwrite_input_file == 'y':
                    write_input_file()
            if solution_file_exists_check:
                overwrite_solution_file = str(input("Overwrite solution file? y/(n): ") or 'n')
                if overwrite_solution_file == 'y':
                    write_solution_file()
        elif not folder_exists_check:
            os.mkdir(project_folder)

    def passthrough_data(aoc_data):
        pass

def check_cookie_existence():
    env_vars = os.environ
    if 'AOC_COOKIE' in env_vars:
        cookie = os.environ['AOC_COOKIE']
    else:
        print("Cookie environment variable not found! Requesting input for session cookie.")
        session_cookie = None
        cookie = set_cookie_environment_variable(session_cookie)
    return cookie

def set_cookie_environment_variable(cookie):
    while cookie is None:
        cookie = input("Enter session cookie: ")
    if cookie:
        session_cookie = "session={}".format(cookie)
        os.environ['AOC_COOKIE'] = session_cookie
        set_cookie = os.environ['AOC_COOKIE']
        return set_cookie
    else:
        print("Something went wrong.")

def main():
    current_year = fetch_current_year()
    script_args = script_argument_parser(current_year)
    aoc_data = fetch_aoc_data(script_args)
    output_definer.write_data_to_file(aoc_data, script_args[1])

if __name__ == "__main__":
    main()
