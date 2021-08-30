import re

HEADER_SUB = r'^(#{1,6}) (.*)'
BOLD_SUB = r'__(.*?)__'
ITALIC_SUB = r'_(.*?)_'
LIST_ITEM_SUB = r'^\* (.*)'

def format_header(line):
    def replacement(match):
        hashes, text = match.groups()
        num = len(hashes)
        return f'<h{num}>{text}</h{num}>'
    return re.sub(HEADER_SUB, replacement, line)


def format_bold(element):
    return re.sub(BOLD_SUB, r'<strong>\1</strong>', element)

def format_italic(element):
    return re.sub(ITALIC_SUB, r'<em>\1</em>', element)


def format_list_item(line):
    return re.sub(LIST_ITEM_SUB, r'<li>\1</li>', line)


def format_paragraph(line):
    if not re.match('<h|<ul|<p|<li', line):
        line = f'<p>{line}</p>'
    return line


def convert_line(line):
    line = format_header(line)
    line = format_list_item(line)
    line = format_paragraph(line)
    line = format_bold(line)
    line = format_italic(line)
    return line


def group_list_items(old_lines):
    in_list = False
    new_lines = []
    for line in old_lines:
        if line.startswith('<li>'):
            if not in_list:
                new_lines.append('<ul>')
            in_list = True
        else:
            if in_list:
                new_lines.append('</ul>')
            in_list = False
        new_lines.append(line)
    if in_list:
        new_lines.append('</ul>')
    return new_lines


def parse0(markdown):
    markdown_lines = markdown.splitlines()
    html_lines = group_list_items(convert_line(line) for line in markdown_lines)
    return ''.join(html_lines)

def parse(s):
    # Emphasis
    s = re.sub(r"__(.+)__", r"<strong>\1</strong>", s)
    s = re.sub(r"_(.+)_", r"<em>\1</em>", s)

    # Headers
    for i in range(1, 7):
        s = re.sub(rf"^{'#' * i} (.+)$", rf"<h{i}>\1</h{i}>", s, flags=re.MULTILINE)

    # Lists
    s = re.sub(r"^\* (.+)$", r"<li>\1</li>", s, flags=re.MULTILINE)
    s = re.sub(r"(<li>.+</li>)", r"<ul>\1</ul>", s, flags=re.DOTALL)

    # Paragraphs & Formatting
    s = re.sub(r"^(?!<h|<ul|<p|<li)(.+)$", r"<p>\1</p>", s, flags=re.MULTILINE)
    s = re.sub(r"\n", "", s)

    return s