#!/usr/bin/env python

import os
import codecs
import jinja2
import shutil
import datetime
import markdown
import functools
import livereload
import collections
import feedgenerator


IN_DIR = 'content/'
OUT_DIR = 'deploy/'
THEME_DIR = 'theme/'
TEMPLATE_DIR = THEME_DIR + 'templates/'

TEMPLATES = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

SECTIONS = collections.OrderedDict()

open = functools.partial(codecs.open, encoding='utf8')


def read_sections():
    with open(IN_DIR + 'sections') as f:
        for section in f.read().splitlines():
            SECTIONS[section] = []


def read_pages():
    extensions = [
        'markdown.extensions.meta',
        'markdown.extensions.codehilite'
    ]

    md = markdown.Markdown(extensions=extensions)

    for section, pages in SECTIONS.items():
        section_dir = IN_DIR + section + '/'

        for filename in os.listdir(section_dir):
            with open(section_dir + filename) as f:
                content = md.convert(f.read())

            meta = {k: v[0] for k, v in md.Meta.items()}

            date = datetime.datetime.strptime(meta['date'], '%Y-%m-%d').date()

            pages.append({
                'href': section + '/' + filename.replace('.md', '/'),
                'index_meta': meta.get('index_meta'),
                'title': meta['title'],
                'date': date,
                'content': content
            })


def sort_pages():
    for section in SECTIONS:
        SECTIONS[section].sort(key=lambda p: p['date'], reverse=True)


def write_pages():
    page_template = TEMPLATES.get_template('page.html')

    for section, pages in SECTIONS.items():
        os.mkdir(OUT_DIR + section)

        for page in pages:
            out_fname = OUT_DIR + page['href']

            os.mkdir(out_fname)

            with open(out_fname + 'index.html', 'w') as out:
                out.write(page_template.render(**page))


def write_index():
    with open(OUT_DIR + 'index.html', 'w') as out:
        index_template = TEMPLATES.get_template('index.html')

        ctx = {
            'sections': SECTIONS,
            'about': markdown.markdown(open(IN_DIR + 'about.md').read())
        }

        out.write(index_template.render(ctx))


def write_feed():
    feed_args = {
        'title': 'adamzap.com',
        'link': 'http://adamzap.com/',
        'description': 'New content from adamzap.com',
    }

    feed = feedgenerator.Rss201rev2Feed(**feed_args)

    for page in sum(SECTIONS.values(), []):
        item_args = {
            'title': page['title'],
            'description': page['content'],
            'link': 'http://adamzap.com/' + page['href']
        }

        feed.add_item(**item_args)

    with open(OUT_DIR + 'feed.xml', 'w') as feed_file:
        feed.write(feed_file, 'ascii')


def build():
    try:
        shutil.rmtree(OUT_DIR)
    except OSError:
        pass

    os.mkdir(OUT_DIR)

    read_sections()
    read_pages()
    sort_pages()
    write_pages()
    write_index()
    write_feed()

    shutil.copytree(IN_DIR + 'media/', OUT_DIR + 'media/')
    shutil.copytree(THEME_DIR + 'static/', OUT_DIR + 'static/')


if __name__ == '__main__':
    server = livereload.Server()

    server.watch('content', build)
    server.watch('theme', build)

    server.serve(root='deploy', open_url=True)
