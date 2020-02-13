#!/usr/bin/env python3
import io
from tweetsplit.main import Tweetsplit


def retrieve_contents_from_input_file():
    with io.open("input.txt", "r") as fp:
        contents = fp.read()
    return contents


def save_contents_to_output_file(contents):
    with io.open("output.txt", "a") as fp:
        for content in contents:
            fp.write("%s\n" % content)


def run():
    text = retrieve_contents_from_input_file()
    tweetsplit = Tweetsplit(text=text)
    posts = tweetsplit.retrieve_posts()
    save_contents_to_output_file(contents=posts)


if __name__ == '__main__':
    run()
