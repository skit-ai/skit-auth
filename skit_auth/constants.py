"""
Common constants used by the package.

We maintain this file to make sure that we don't have inconsistencies in the
constants used. It is common to notice spelling mistakes associated with strings
additionally, we don't get IDE's to automatically suggest values.

consider:

```python
a_dict["key"]
```

and 

```
a_dict[const.KEY]
```
In the latter, a mature IDE will suggest the KEY constant, reducing time and ensuring consistency.
"""

EMAIL = "email"
PASSWORD = "password"
ACCESS_TOKEN = "access_token"
ORG_ID = "organisation_id"
AUTHORIZATION = "Authorization"
HTTP_SUCCESS = 200
ROUTE_OAUTH = "/oauth/"
ROUTE_CHANGE_ORG = "/change-org/"
DEFAULT_API_GATEWAY_URL = "https://apigateway.vernacular.ai"
