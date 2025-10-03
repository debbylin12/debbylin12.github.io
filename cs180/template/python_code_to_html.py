### Convert python code into html format with in colorful format
## Make sure to install pygments before running this script
# pip3 install pygments
import sys
import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if not os.path.isfile(arg):
                print(f"Invalid file path: '{arg}', skip.")
                continue
            if not arg.lower().endswith('.py'):
                print(f"Input file is not a python file: '{arg}', skip.")
                continue
            
            print(f"Valid input file, now processing: '{arg}'...")
            try:
                with open(arg, "r") as file:
                    code = file.read()
            except FileNotFoundError:
                print(f"Error: The file '{arg}' was not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

            formatter = HtmlFormatter(full=True, style="friendly")  # try 'monokai', 'friendly', 'colorful', etc.
            html = highlight(code, PythonLexer(), formatter)

            out_file = os.path.splitext(arg)[0] + '.html'
            with open(out_file, "w") as f:
                f.write(html)
            print(f"Done processing: '{arg}'.")
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()