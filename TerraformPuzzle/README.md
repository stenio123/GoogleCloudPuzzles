# Puzzle 2: 2021 - 10 -15
## Cloud Asset Inventory | Terraform

### Challenge:

Create a Terraform code to match the provided Cloud Asset Inventory file:
- Compute instances
- IAM accounts
- Network
- Project
- Services (API)

## Authentication
Instructions on how to authenticate can be found in the [provider's docs](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#authentication)

## Deployment
0. Make sure your org gave your user suffient permissions to run this code! :-D

1. Create a Billing account and a new project, associated with the billing account

2. To Bootstrap API services permission, run 
```
cd bootstrap 
terraform init
terraform apply
gcloud config set project [YOU_PROJECT_NAME]
# Setting project in the environment due to potential bug https://github.com/hashicorp/terraform-provider-google/issues/10381
```

3. To deploy infrastructure, run
```
cd ../infra
terraform init
terraform apply
```

Enjoy!