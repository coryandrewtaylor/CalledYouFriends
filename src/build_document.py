import functools
import json
import os
import subprocess

import plac

from scripts import custom_markdown  # pylint: disable=import-error

FILE_KWARGS = dict(encoding='utf-8', errors='ignore')


def get_config(filepath):
    with open(filepath, 'r', **FILE_KWARGS) as _file_obj:
        _config = json.load(_file_obj)
    return _config


run_cmd = functools.partial(subprocess.run,
                            **dict(stdout=subprocess.PIPE, encoding='utf-8'))


@plac.annotations(
    config_file=plac.Annotation(
        help='Path to the build configuration file',
        kind='positional',
        type=str,
        metavar='config-file'))
def main(config_file='./config/build_config.json'):
    cfg = get_config(os.path.normpath(config_file))
    markdown_lookup = get_config(os.path.normpath(cfg['markdown_lookup']))

    doc = run_cmd(cfg['pandoc_command']).stdout
    doc = custom_markdown.convert(doc, lookup=markdown_lookup)

    output_file = os.path.normpath(cfg['output_file'])
    with open(output_file, 'w', **FILE_KWARGS) as output_fileobj:
        output_fileobj.write(doc)


if __name__ == '__main__':
    plac.call(main)
