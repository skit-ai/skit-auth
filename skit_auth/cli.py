import argparse

from skit_auth import auth
from skit_auth import constants as const


def build_cli():
    parser = argparse.ArgumentParser(description="skit.ai's authorization library.")
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
        "--password", type=str, required=True, help="The password of the user or IAM."
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
    if args.org_id:
        print(auth.get_org_token(args.url, args.email, args.password, args.org_id))
    else:
        print(auth.get_default_token(args.url, args.email, args.password))
