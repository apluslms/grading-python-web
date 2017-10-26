Python grading environment for web content.

* Firefox and Selenium

    Includes Firefox browser that Selenium can control.
    MUST use xvfb-run to emulate screen:

    e.g. `sudo-capture xvfb-run python3 my_selenium_tests.py`

Installed Python packages are listed in requirements.txt.
In addition, following scripts are provided in path.

* `validate_html [files]`

    Validates that the files are valid HTML5.
    Prints the line number and exits with
    non zero if problems are detected.
