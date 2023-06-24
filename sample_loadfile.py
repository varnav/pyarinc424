# Sample file conversion with mifapi
# Batch processing through async API
# https://github.com/varnav/mifapi
# Evgeny Varnavskiy 2020
# MIT License

import click as click

import pyarinc424 as a
from json import loads, dumps


@click.command()
@click.argument('infile', type=click.Path(exists=True))
@click.argument('outfile', type=click.Path(exists=False))
def main(infile, outfile):
    df = a.read_waypoints(infile)
    print(df)
    df.to_json(outfile, orient="records")
    result = df.iloc[5].to_json()
    parsed = loads(result)
    print(dumps(parsed, indent=4))


if __name__ == '__main__':
    main()
