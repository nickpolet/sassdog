import argparse
import ntpath
import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import scss
from csscompressor import compress

from colorama import init as colorama_init
from colorama import Fore, Back, Style
colorama_init()


class SassHandler(PatternMatchingEventHandler):

    patterns = []

    def process(self, event, compile=False):

        print(Fore.YELLOW + event.src_path + ' ' + event.event_type)

        if compile:
            try:
                compile_scss(event.src_path)
            except Exception as e:
                print(e)


    def on_modified(self, event):
        self.process(event, True)

    def on_created(self, event):
        self.process(event)


def compile_scss(src):

    if not ntpath.basename(src).startswith('_'):
        scss_compiled = scss.compiler.compile_file(src)
             
        css_filename = src.replace('.scss', '.css')

        css_file = open(css_filename, 'w')
        css_file.write(compress(scss_compiled))
        #css_file.write(scss_compiled)
        css_file.close()

        print(Fore.GREEN + css_filename + ' ' + 'compiled')


def compile_all_scss():

    for root, subFolders, files in os.walk('.', topdown=False):
        for file in files:

            if '.scss' in file:

                compile_scss(os.path.join(root, file))

def main():
    parser = argparse.ArgumentParser(description='Sassdog - Move to the directory you want to automatically compile scss or sass files and run "sassdog". Simple.')
    #parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                   help='an integer for the accumulator')

    parser.add_argument('--compile', action='store_true', help='Force sassdog to compile all .scss files before starting up')

    args = parser.parse_args()

    if args.compile:
        compile_all_scss()

    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = '.'
    observer = Observer()

    scss_handler = SassHandler()
    scss_handler.patterns = ["*.scss"]
    observer.schedule(scss_handler, path, recursive=True)

    observer.start()
    print(Fore.GREEN + 'sassdog running')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()


    observer.join()
    print(Fore.GREEN + '\nwoof')