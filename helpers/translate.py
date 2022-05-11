"""Translate helpers."""
from googletrans import Translator
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import sys

from httpcore import ReadTimeout

src_lang = "en"
dest_lang = "ru"

file_path = 'tmp.po'
is_windows = sys.platform.startswith('win32')


def write_new(text: str):
    """Write new text with correct encoding."""
    if is_windows:
        text.encode("utf8")
    new_file.write(text)


if __name__ == "__main__":
    translator = Translator()

    print("started")
    # Create temp file
    fh, abs_path = mkstemp()
    new_file = fdopen(fh, 'w')
    old_file = open(file_path)

    line_to_translate = None
    for line in old_file:
        if line.startswith('msgid'):
            line_to_translate = line[7:-2]
            write_new(line)
        elif line.startswith('msgstr'):
            current_line = line[8:-2]
            if len(current_line) > 0 or line_to_translate is None or len(line_to_translate) == 0:
                write_new(line)
                continue
            print(f"translating: {line_to_translate}")
            try:
                translated_line = translator.translate(line_to_translate, src=src_lang, dest=dest_lang).text
            except ReadTimeout:
                break
            write_new(f"msgstr \"{translated_line}\"\n")
            line_to_translate = None
        else:
            line_to_translate = None
            write_new(line)

    old_file.close()
    new_file.close()

    # Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)
