"""
Configuration utilities.
"""

__all__ = ['options']

import os.path
import json
import codecs

import conf
paper_conf  = conf.paper_conf


def get_config():
    config = cfg2dict(proc_conf)
    config.update(cfg2dict(toc_conf))
    return config


def cfg2dict(filename, quiet=False):
    """Return the content of a JSON config file as a dictionary.

    """
    if not os.path.exists(filename):
        if not quiet:
            print '*** Warning: %s does not exist.' % filename
        return {}

    return json.loads(codecs.open(filename, 'r', 'utf-8').read())


def dict2cfg(d, filename):
    """Write dictionary out to config file.

    """
    json.dump(d, codecs.open(filename, 'w', 'utf-8'), ensure_ascii=False)


def mkdir_p(dir):
    if os.path.isdir(dir):
        return
    os.makedirs(dir)

options = cfg2dict(paper_conf)
