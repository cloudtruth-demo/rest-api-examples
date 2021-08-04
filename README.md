# CloudTruth Rest API examples
This repo contains demo RESTful API code that interacts with CloudTruth.

Create an [API access token](https://docs.cloudtruth.com/organization-management/access-tokens) for authentication.

## [CloudTruth_rest_methods](https://github.com/cloudtruth-demo/rest-api-examples/blob/main/python/CloudTruth_rest_methods.py)
This script is a stand alone python example shows hot to create a function that will pass a token, API url, method type and task data.  The only built in call will list CloudTruth environments.

### Usage
python CloudTruth_rest_methods.py --token YOUR_API_TOKEN --environment

| switch                   | Description                     |
|--------------------------|---------------------------------|
|  -h, --help              | show this help message and exit |
|  -t TOKEN, --token TOKEN | Specify the API Token           |
|  -e, --environments      | Get environments                |

## [CloudTruth_Base Class](https://github.com/cloudtruth-demo/rest-api-examples/tree/main/python/CloudTruth_OOP)
This is an example that uses a base class [CloudTruth_api.py](https://github.com/cloudtruth-demo/rest-api-examples/blob/main/python/CloudTruth_OOP/CloudTruth_api.py) for CloudTruth REST methods.

[CloudTruth_get_objects.py](https://github.com/cloudtruth-demo/rest-api-examples/blob/main/python/CloudTruth_OOP/CloudTruth_get_objects.py) imports the Cloudtruth_api class and prompts the user for options that will invoke CloudTruth GET methods to list details of your organization.

### Usage
 python CloudTruth_get_objects.py --token YOUR_API_TOKEN --environment

| switch                   | Description                     |
|--------------------------|---------------------------------|
|  -h, --help              | show this help message and exit |
|  -t TOKEN, --token TOKEN | Specify the API Token           |
|  -a, --audit             | Get Audit                       |
|  -as, --auditsum         | Get Audit summary               |
|  -e, --environments      | Get environments                |
|  -z, --aws               | Get AWS Integrations            |
|  -g, --github            | Explore Integrations            |
|  -x, --explore           | Get GitHub Integrations         |
|  -i, --invitations       | Get Invitations                 |
|  -m, --memberships       | Get Memberships                 |
|  -o, --organizations     | Get Orgnizations                |
|  -p, --projects          | Get Projects                    |
|  -s, --apiaccounts       | Get API access tokens accounts  |
|  -u, --users             | Get users                       |
