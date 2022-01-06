# skit-auth

This is a simple authentication library for Skit's platform.

- Provides JWTs in exchange for IAM credentials.
- Provides specific tokens for organizations associated with Skit.


## Installation
The library uses `python=^3.9`.

```shell
pip install skit-auth
skit-auth -h
```

## Usage

```
❯ skit-auth -h
usage: skit-auth [-h] [--url URL] --email EMAIL --password PASSWORD [--org-id ORG_ID]

skit.ai's authorization library.

optional arguments:
  -h, --help           show this help message and exit
  --url URL            The URL of the API Gateway.
                       [Default=https://apigateway.vernacular.ai]
  --email EMAIL        The email address of the user or IAM.
  --password PASSWORD  The password of the user or IAM.
  --org-id ORG_ID      The ID of the organization.
```

The default url is the production api gateway endpoint.

## Example

Sharing a few invocation examples:

```shell
skit-auth --email iam@skit.ai --password "******"
```

This provides a JWT for skit.ai's organization. If a particular organization is required, we can use the `--org-id` flag.

```shell
skit-auth --email iam@skit.ai --password "******" --org-id 2
```
