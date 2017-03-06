#!/usr/bin/env python2
import os.path

# Load config file.
config_file = open('config.cssopt', 'r')


# Create new css file.
optimized_css_file = open('optimized_css.css', 'w')


# Extract all paths from config.cssopt file.
def extract_all_paths():
    css_paths = config_file.read().rsplit(',')
    for i,s in enumerate(css_paths):
        css_paths[i] = s.strip()
    config_file.close()
    return css_paths


# Check does file exists.
def file_exists(path):
    return os.path.isfile(path)


# Compress whole css file into one line.
def optimize(css):
    return css.replace('\r', '')\
        .replace('\n', '')\
        .replace('\t', '')\
        .replace('\b', '')\
        .replace(' ', '')


# Put all css files into one.
def copy_css_files_into_one(paths):
    for css_path in paths:
        if not file_exists(css_path):
            print 'File', css_path, 'does not exists'
            continue
        print 'coping file:', css_path,'...'
        css_file = open(css_path, 'r')
        optimized_css_file.write(optimize(css_file.read()))
        css_file.close()
        print 'successfully!'
    optimized_css_file.close()


if file_exists('optimized_css.css'):
    optimized_css_file.truncate()
    print 'removed previously css...'

paths = extract_all_paths()
copy_css_files_into_one(paths)