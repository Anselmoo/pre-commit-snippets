import json
import subprocess
import sys
import re


def extract_urls(data):
    if isinstance(data, dict):
        for value in data.values():
            yield from extract_urls(value)
    elif isinstance(data, list):
        for item in data:
            yield from extract_urls(item)
    elif isinstance(data, str):
        urls = re.findall(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            data,
        )
        for url in urls:
            yield url


def main():
    with open(sys.argv[1]) as f:
        data = json.load(f)

    urls = list(extract_urls(data))

    result = subprocess.run(["lychee", "--no-progress"] + urls)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
