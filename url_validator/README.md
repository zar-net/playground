# URL Checker with Redirect and New Version Detection

This script checks the status of URLs from a provided list and determines if they are alive, dead, or have been redirected. Additionally, it searches for a new version of the content if no redirect exists.

## Features

- Checks if URLs are alive or dead.
- Detects if URLs have been redirected.
- Searches for a new version of the content if no redirect exists.
- Outputs results in a CSV file with status and URL.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```

## Usage
Prepare Input Files:
1. Create a text file containing a list of URLs, one per line, e.g., urls.txt.
2. Create a text file containing a list of terms to check for, one per line, e.g., terms.txt.

### Run the Script

```
python url_checker_with_new_version.py -URL urls.txt -T terms.txt -O output.csv
```

#### Command Line Arguments
-URL: Path to the text file containing URLs.

-T: Path to the text file containing terms to check in the content.

-O: Path to the output CSV file.

#### Output
The script generates a CSV file with the following columns:

Status: Indicates the status of the URL:

"+" if the URL is alive and does not contain any specified terms.

"-" if the URL is dead or contains any specified terms.

"->" {redirected_url} if the URL redirects to another URL.
  
New Version -> {new_url} if a new version of the content is found.

URL: The original URL.

#### Example
Suppose you have the following urls.txt:

```
http://example.com
http://example.org
http://example.net
```

And the following terms.txt:

```
content not available
page not found
```

Running the script:
```
python url_checker_with_new_version.py -URL urls.txt -T terms.txt -O output.csv
```

Might produce an output.csv file with content similar to:

```
Status,URL
+,http://example.com
>> -> http://example.org,new http://example.org
-,http://example.net
``
