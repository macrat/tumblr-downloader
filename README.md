Tumblr downloader
=================

A tool for download photos from Tumblr.

Usage
-----
1. Get API Key at [Applications](https://www.tumblr.com/oauth/apps)

2. Write configuration into the script.

Please fill BLOG, API\_KEY of [main.py](./main.py)

3. Install dependencies.

``` shell
$ pip -r requirements.txt
```

4. Run!

``` shell
$ python main.py
```

In the first execution time, this script will download photos from maximum 100 posts.
After that, it will download only newly posted photos.
