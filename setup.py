import urllib.request
import argparse
import datetime
import os
import shutil
import io
from sys import exit

passthrough_output = False
day = 0

def fetch_current_year():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    return year

def script_argument_parser(year, day):
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
        default=day,
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
    while day is None or not day or 0:
        try:
            day = int(input("Input requested day: "))
            if day not in range(1, 25):
                print("Enter an integer between 1 and  25.")
        except ValueError:
            exit("Enter an integer between 1 and  25.")
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
        exit("Did you enter a valid cookie or set a valid AOC_COOKIE environment variable?")

class output_definer:
    def __init__(self, aoc_data, day) -> None:
        self.aoc_data = aoc_data
        while self.aoc_data.endswith('\n'):
            self.aoc_data = self.aoc_data[:-1]
        self.day = day

    def create_day(self):
        folder_name = "Day {}".format(self.day)
        project_folder = os.path.join(os.curdir, folder_name)
        folder_exists_check = os.path.exists(project_folder)
        try:
            if not folder_exists_check:
                os.mkdir(project_folder)
            return project_folder
        except ValueError:
            exit(ValueError)

    def write_data_to_file(self):
        project_folder = self.create_day()
        input_file_write_location = os.path.join(project_folder, "input_data.txt")
        input_file_exists_check = os.path.isfile(input_file_write_location)
        solution_file_read_location = os.path.join(os.curdir, 'templates', 'Solution.py')
        solution_file_write_location = os.path.join(project_folder, 'Solution.py')
        solution_file_exists_check = os.path.isfile(solution_file_write_location)
        solution_passthrough_file_read_location = os.path.join(os.curdir, 'templates', 'Solution_passthrough.py')
        solution_passthrough_file_write_location = os.path.join(project_folder, 'Solution.py')
        solution_passthrough_file_exists_check = os.path.isfile(solution_passthrough_file_write_location)

        def write_input_file():
            write_to_input_file = open(input_file_write_location, 'w')
            write_to_input_file.write(self.aoc_data)
            write_to_input_file.close()

        def write_solution_file():
            shutil.copy(solution_file_read_location, solution_file_write_location)

        def write_solution_passthrough_file():
            shutil.copy(solution_passthrough_file_read_location, solution_passthrough_file_write_location)

        if input_file_exists_check:
            prompt_overwrite_input_file = str(input("Overwrite input file? y/(n): ") or 'n')
            if prompt_overwrite_input_file == 'y':
                write_input_file()
        else:
            prompt_write_input_file = str(input("Write input file? y/(n): ") or 'n')
            if prompt_write_input_file == 'y':
                write_input_file()
        if solution_file_exists_check:
            prompt_overwrite_solution_file = str(input("Overwrite solution file? y/(n): ") or 'n')
            if prompt_overwrite_solution_file == 'y':
                write_solution_file()
        else:
            prompt_write_solution_file = str(input("Write solution file? y/(n): ") or 'n')
            if prompt_write_solution_file == 'y':
                prompt_write_solution_passthrough_file = str(input("Write solution passthrough file? y/(n): ") or 'n')
                if prompt_write_solution_passthrough_file == 'n':
                    print("You will need to set the input file yourself.")
                    write_solution_file()
                if solution_passthrough_file_exists_check:
                    prompt_overwrite_solution_passthrough_file = str(input("Overwrite solution passthrough file? y/(n): ") or 'n')
                    if prompt_overwrite_solution_passthrough_file == 'y':
                        write_solution_passthrough_file()
                elif not solution_passthrough_file_exists_check and prompt_write_solution_passthrough_file == 'y':
                    write_solution_passthrough_file()

    def passthrough_data(self):
        aoc_data_stream = io.StringIO(self.aoc_data)
        return aoc_data_stream

def check_cookie_existence():
    env_vars = os.environ
    if 'AOC_COOKIE' in env_vars:
        cookie = os.getenv('AOC_COOKIE')
    else:
        print("Cookie environment variable not found! Requesting input for session cookie.")
        session_cookie = None
        cookie = set_cookie_environment_variable(session_cookie)
    return cookie

def set_cookie_environment_variable(cookie):
    while cookie is None or not cookie:
        cookie = input("Enter session cookie: ")
    if cookie:
        try:
            session_cookie = "session={}".format(cookie)
            os.environ['AOC_COOKIE'] = session_cookie
            os.environ.setdefault('AOC_COOKIE', {session_cookie})
            session_cookie = os.getenv('AOC_COOKIE')
            return session_cookie
        except ValueError or KeyError as Env_Var_Error:
            exit(Env_Var_Error)
    else:
        exit("Something went wrong.")

def main(passthrough_output, day):
    current_year = fetch_current_year()
    script_args = script_argument_parser(current_year, day)
    day = script_args[1]
    aoc_data = fetch_aoc_data(script_args)
    aoc_output_object = output_definer(aoc_data, day)
    if passthrough_output:
        output = aoc_output_object.passthrough_data()
        return output
    elif not passthrough_output:
        aoc_output_object.write_data_to_file()


if __name__ == "__main__":
    main(passthrough_output, day)
