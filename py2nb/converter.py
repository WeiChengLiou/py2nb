from __future__ import absolute_import, division, print_function

import nbformat as nb


def convert(input_string, output_filename):
    """
    Convert a preprocessed string object into notebook file
    """
    # Read using v3
    input = nb.v3.reads_py(input_string)
    notebook = nb.convert(input, max(nb.versions))
    # Write using the most recent version
    with open(output_filename, 'w') as fout:
        nb.write(notebook, fout)
