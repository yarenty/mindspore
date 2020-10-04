import sys
from time import sleep
from pathlib import Path
import pprint
import logging

import click
from halo import Halo
import coloredlogs

from minddocker.check import check_root_dir

@click.group(name='minddocker')
@click.option('--log-level', default="DEBUG", help="Log level for the app.")
def cli(log_level: str):
    """
    mind-docker 📦 is a packaging tool for ML models
    """
    logger = logging.getLogger(__name__)
    click.echo(f"Log level is set to - {log_level}")
    coloredlogs.install(level=log_level)

@cli.command()
@click.argument('path_to_md')
@Halo(text="", spinner="dots")
def verify(path_to_mlcube: str):
    """
    Verify mind-docker metadata
    """
    logging.info("Starting mind-docker metadata verification")
    metadata, verify_err = check_root_dir(
    Path(path_to_mlcube).resolve().as_posix())

    if verify_err:
        logging.error(f"Error verifying mind-docker metadata: {verify_err}")
        logging.error(f"mind-docker verification - FAILED!")
        raise click.Abort()

    logging.info('OK - VERIFIED')

if __name__ == "__main__":
    cli()
