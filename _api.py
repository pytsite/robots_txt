"""PytSite Robots Module API Functions.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router

__rules = {
    '*': [],
}


def disallow(path: str, user_agent: str = '*'):
    if user_agent not in __rules:
        __rules[user_agent] = []

    __rules[user_agent].append('Disallow: {}'.format(path))


def sitemap(url: str, user_agent: str = '*'):
    if user_agent not in __rules:
        __rules[user_agent] = []

    __rules[user_agent].append('Sitemap: {}'.format(_router.url(url)))


def get_rules() -> dict:
    return __rules
