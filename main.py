import hashlib
import itertools
import json
import pathlib
import pprint
import urllib.request

import pytumblr


OUTDIR = pathlib.Path('./download')
BLOG = 'your-blog-name.tumblr.com'
API_KEY = 'your-api-key (aka. OAuth Consumer Key)'


def iter_photo_posts(step=10, max_pages=10):
    client = pytumblr.TumblrRestClient(API_KEY)

    for i in itertools.count():
        yield from client.posts(BLOG,
                                type='photo',
                                offset=i * step,
                                limit=(i + 1) * step)['posts']

        if max_pages <= i:
            break


def get_latest_timestamp():
    files = sorted(OUTDIR.iterdir())

    if len(files) == 0:
        return 0
    else:
        return int(files[-1].name.split('-')[0])



if __name__ == '__main__':
    latest_timestamp = get_latest_timestamp()

    for post in iter_photo_posts():
        timestamp = post['timestamp']

        if timestamp <= latest_timestamp:
            break

        for photo in post['photos']:
            print(photo['original_size']['url'])

            with urllib.request.urlopen(photo['original_size']['url']) as res:
                image = res.read()

            hash_ = hashlib.md5(image).hexdigest()
            with open(OUTDIR / '{}-{}.jpg'.format(timestamp, hash_), 'wb') as f:
                f.write(image)
