import re


def main():
    print(parse(input("HTML: ")))

def parse(l):
    # Check if the HTML code contains a YouTube embed link using regular expressions
    if you_link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", l):
        # If a match is found, extract the video ID and construct a shortened YouTube URL
        return f"https://youtu.be/{you_link.group(2)}"
    # If no match is found, return None
    return None


if __name__ == "__main__":
    main()