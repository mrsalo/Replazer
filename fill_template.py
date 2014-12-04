#!/usr/bin/env python

import sys
import re

def main():
    if not_2_arguments_provided():
        print_usage()
        exit(1)

    template_file = sys.argv[1]
    output_file = sys.argv[2]
    
    template_lines = get_lines_of(template_file)
    template_variables = get_variables_from(template_lines)
    print_user_message(template_variables)
    template_fillings = ask_user_for_fillings(template_variables)
    rendered_lines = render_lines_with(template_fillings, template_lines)

    write_lines(rendered_lines, output_file)

def not_2_arguments_provided():
    if not len(sys.argv) == 3:
        return True
    return False

def get_lines_of(template_file):
    with open(template_file) as f:
        return f.readlines()

def get_variables_from(template_lines):
    ret = set()
    for line in template_lines:
        matches = re.finditer(r'{{([^}]+)}}', line)
        for match in matches:
            ret.add(match.group(1).strip())

    return ret

def print_user_message(template_variables):
    print('I found ' + str(len(template_variables)) + ' variables in the template:')
    print(list(template_variables))
    print('Please give them a meaning:')

def ask_user_for_fillings(template_variables):
    filled_variables = {}
    for variable in template_variables:
        print(variable + ': ')
        try:
            meaning = raw_input().strip()
        except:
            print('\nk, thx, bye')
            exit(1)
        filled_variables[variable] = meaning
    return filled_variables

def render_lines_with(template_fillings, template_lines):
    output = []
    for line in template_lines:
        matches = re.finditer(r'{{([^}]+)}}', line)
        for match in matches:
            line = line.replace(match.group(0), template_fillings[match.group(1).strip()])
        output.append(line)
    return output

def write_lines(rendered_lines, output_file):
    with open(output_file, 'w') as f:
        f.writelines(rendered_lines)

def print_usage():
    print("Usage: " + sys.argv[0] + " template_name output_name")

if __name__ == "__main__":
    main()
