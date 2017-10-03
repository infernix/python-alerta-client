import sys

import click


@click.command('perm', short_help='Add role-permission lookup')
@click.option('--role', help='role name')
@click.option('--scope', 'scopes', multiple=True, help='list of permissions for role')
@click.option('--delete', '-D', metavar='ID', help='delete role')
@click.pass_obj
def cli(obj, role, scopes, delete):
    """Add or delete role-to-permission lookup entry."""
    client = obj['client']
    if delete:
        if role or scopes:
            raise click.UsageError('Option "--delete" is mutually exclusive.')
        client.delete_perm(delete)
    else:
        if not role:
            raise click.UsageError('Missing option "--role".')
        if not scopes:
            raise click.UsageError('Missing option "--scope".')
        try:
            perm = client.create_perm(role, scopes)
        except Exception as e:
            click.echo('ERROR: {}'.format(e))
            sys.exit(1)
        click.echo(perm.id)
