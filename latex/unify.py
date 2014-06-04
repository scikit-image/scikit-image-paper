import sys
import re

def execute_inputs(filename):
    pattern = r'\\input\{(.*)\}'
    output_lines = []
    with open(filename, 'r') as fin:
        for line in fin:
            match = re.match(pattern, line.lstrip().rstrip())
            if match:
                subfile = match.groups()[0]
                if not subfile.endswith('.tex'):
                    subfile = subfile + '.tex'
                output_lines.extend(execute_inputs(subfile))
            else:
                output_lines.append(line)
    return output_lines


if __name__ == '__main__':
    input_file = sys.argv[1]
    for line in execute_inputs(input_file):
        print(line.rstrip())
