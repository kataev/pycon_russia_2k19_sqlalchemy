import argparse
import sys


def diagram(output):
    import codecs

    try:
        import sadisplay
    except ImportError:
        return 'Install sadisplay, with "pip install sadisplay"'

    from .base import metadata

    desc = sadisplay.describe(metadata.tables.values())

    with codecs.open(output, 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))

    print(f'Now print "dot -Tpng {output} > schema.png"')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output')

    args = parser.parse_args()

    sys.exit(diagram(args.output))
