import os
from sphinx.cmd.build import build_main

def generate_readme():
    """
    Generate a README.md file from Sphinx documentation.
    
    This function:
    1. Creates necessary directory structure for Sphinx
    2. Generates a minimal conf.py with markdown builder configuration
    3. Creates an index.rst file with README content
    4. Builds the documentation using Sphinx
    5. Copies the generated markdown to README.md in the project root
    
    Requirements:
        - sphinx
        - sphinx-markdown-builder
    
    Returns:
        None. The function prints a confirmation message upon successful
        completion and writes the README.md file to the current directory.
    
    Example usage:
        >>> generate_readme()
        README.md successfully generated!
    """

    # Set up Sphinx configuration
    source_dir = 'docs_source'  # Directory containing your RST docs
    build_dir = 'docs_build'    # Temporary build directory

    # Create directories if they don't exist
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(build_dir, exist_ok=True)

    # Create minimal conf.py in source_dir
    with open(os.path.join(source_dir, 'conf.py'), 'w', encoding='UTF-8') as f:
        f.write("""
PROJECT = 'Your Project'
EXTENSIONS = ['sphinx_markdown_builder']
SOURCE_SUFFIX = '.rst'
MASTER_DOC = 'index'
""")

    # Create index.rst with your desired README content
    with open(os.path.join(source_dir, 'index.rst'), 'w', encoding='UTF-8') as f:
        f.write("""
Project Name
============

Description of your project here.

Features
--------

* Feature 1
* Feature 2

Installation
------------

.. code-block:: bash

    pip install your-package

Usage
-----

.. code-block:: python

    import your_package
    your_package.do_something()
""")

    # Build markdown output
    build_args = ['-b', 'markdown', source_dir, build_dir]
    build_main(build_args)

    # Copy the generated README.md to project root
    with open(os.path.join(build_dir, 'index.md'), 'r', encoding='UTF-8') as src:
        with open('README.md', 'w', encoding='UTF-8') as dest:
            dest.write(src.read())

    print("README.md successfully generated!")

if __name__ == "__main__":
    generate_readme()
