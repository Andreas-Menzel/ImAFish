# ImAFish

ImAFish is a simple python script to help hackers fill their phishing databases.

## Usage

Here is just a simple example:

```
python ImAFish.py --url https://example.com/ \
    --runs 10 \
    --delay 1 \
    --param_random_elem username#Alice#Bob#Carol#Dan \
    --param_random_str password#8#32#abcdefghijklmnopqrstuvwxyz1234567890 \
    --param_random_file_elem name#commom_names.txt \
    --param country#DE
```

For more information use `--help`.
