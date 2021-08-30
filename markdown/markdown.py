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

def group_list(lines):
    lines = re.sub(r"^\* (.+)$", r"<li>\1</li>", lines, flags=re.MULTILINE)
    lines = re.sub(r"(<li>.+</li>)", r"<ul>\1</ul>", lines, flags=re.DOTALL)
    return lines


def parse(markdown):
    markdown_lines = markdown.splitlines()
    html_lines = (convert_line(line) for line in markdown_lines)
    return group_list(''.join(html_lines))
