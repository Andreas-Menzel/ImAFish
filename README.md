# ImAFish

## ImAFish is a simple python script to help hackers fill their phishing databases.

ImAFish is a simple, fun python project to send http POST requests using pythons
requests library. It can be used to automatically and semi-randomly fill out
login forms of phishing sites.


## How can I use ImAFish?

1. Use your browsers inspector tool to get the `name`s of the input fields.
2. Execute the script and pass the url and parameters

The following example should explain the main principle:

Suppose we have a form and want to pass parameters in the following format:

- `usename`: select one of four pre-defined usenames
- `password`: generate a random password with length between 8 and 32
- `name`: select a name from the *commom_names.txt* file
- `country`: always use *DE*

We want to send 10 requests with a delay of 1 second.

```
python ImAFish.py --url https://example.com/ \
    --runs 10 \
    --delay 1 \
    --param_random_elem username#Alice#Bob#Carol#Dan \
    --param_random_str password#8#32#abcdefghijklmnopqrstuvwxyz1234567890 \
    --param_random_file_elem name#commom_names.txt \
    --param country#DE
```

### Parameters

```
usage: ImAFish [-h] [--url URL] [--runs RUNS] [--delay DELAY] [-v]
               [--param [PARAM ...]]
               [--param_random_str [PARAM_RANDOM_STR ...]]
               [--param_random_elem [PARAM_RANDOM_ELEM ...]]
               [--param_random_file_elem [PARAM_RANDOM_FILE_ELEM ...]]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             The URL.
  --runs RUNS           Number of runs.
  --delay DELAY         Delay in seconds between each run.
  -v, --verbose         Print more information
  --param [PARAM ...]   Fixed parameter.
  --param_random_str [PARAM_RANDOM_STR ...]
                        Random string parameter.
  --param_random_elem [PARAM_RANDOM_ELEM ...]
                        Random element parameter.
  --param_random_file_elem [PARAM_RANDOM_FILE_ELEM ...]
                        Random element from file parameter.

FIXED PARAMETER
Uses a fixed value for a parameter.
usage:		--param <name>#<value>
example:	--param user#superuser

RANDOM STRING PARAMETER
Generates a random string for a parameter.
usage:		--param_random_str <name>#<min_len>#<max_len>#<chars>
example:	--param_random_str password#8#12#abcdef123

RANDOM ELEMENT PARAMETER
Choses a random element from a list as the value for a parameter.
usage:		--param_random_elem <name>#<value0>#<value1>#...
example:	--param_random_elem website#example.com#example.net

RANDOM FILE ELEMENT PARAMETER
Choses a random element from a list of a file as the value for a parameter.
usage:		--param_random_file_elem <name>#<filename>
example:	--param_random_file_elem password#passList.txt
```


## Limitations

- **Multi-Step forms**

    Some (phishing) websites implement a two-step login. 1) Enter email and
    click 'continue'. 2) Enter password and click 'login'. This script does not
    use sessions or other means to fill out those multi-step forms. One could
    implement this feature with the [selenium](https://pypi.org/project/selenium/)
    module.

- **Not-A-Robot checks**

    This script can not solve CAPTCHAs. Most phising sites don't require this,
    however.

- **POST requests**

    Only http POST requests are supported (not GET).
