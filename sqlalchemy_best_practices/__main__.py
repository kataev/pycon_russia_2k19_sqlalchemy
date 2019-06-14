import click

from sqlalchemy_best_practices.db.base import metadata


@click.group(short_help='Commands for work with db')
def db():
    pass


@db.command(short_help='Create table')
def create_all():
    click.echo('creating')
    metadata.create_all()
    click.echo('complete!')


@db.command(short_help='Drop tables')
def drop_all():
    click.confirm('it really need?', abort=True)
    click.echo('dropping')
    metadata.drop_all()
    click.echo('complete!')


if __name__ == '__main__':
    db()
