import argparse
import getpass
import os

from skit_auth import __version__, auth
from skit_auth import constants as const
from skit_auth import utils

VERSION = __version__


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        values = os.environ.get("SKIT_API_GATEWAY_PASSWORD") or getpass.getpass()
        setattr(namespace, self.dest, values)


def build_cli():
    parser = argparse.ArgumentParser(
        description=f"skit-auth {VERSION}.\n\nskit.ai's authorization library."
    )
    parser.add_argument(
        "-v", "--verbose", action="count", help="Increase verbosity.", default=0
    )
    parser.add_argument(
        "--url",
        type=str,
        help=f"The URL of the API Gateway. [Default={const.DEFAULT_API_GATEWAY_URL}]",
        default=const.DEFAULT_API_GATEWAY_URL,
    )
    parser.add_argument(
        "--email", type=str, required=True, help="The email address of the user or IAM."
    )
    parser.add_argument(
        "-p",
        "--password",
        type=str,
        help="The password of the user or IAM."
        " We can also read it from the SKIT_API_GATEWAY_PASSWORD environment variable."
        " *DON'T* provide a value e.g. -p <password> or --password <password> will fail.",
        action=Password,
        dest="password",
        nargs=0,
        default=os.environ.get("SKIT_API_GATEWAY_PASSWORD"),
    )
    parser.add_argument(
        "--org-id", type=int, required=False, help="The ID of the organization."
    )
    return parser


def main() -> None:
    """
    Main entry point for the CLI.

    We try to read token from the pipes.
    """
    cli = build_cli()
    args = cli.parse_args()
    utils.configure_logger(args.verbose)

    if not isinstance(args.password, str) or args.password == "":
        raise argparse.ArgumentTypeError(
            "You must provide a password. Use -p or --password."
        )
    if args.org_id:
        print(auth.get_org_token(args.url, args.email, args.password, args.org_id))
    else:
        print(auth.get_default_token(args.url, args.email, args.password))
