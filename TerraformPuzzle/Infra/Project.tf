

data "google_project" "stenio-techpuzzle-iac" {
  project_id = var.project
}

/**
data "google_billing_account" "acct" {
  display_name = "My Billing (stenio)"
  open         = true
}

resource "google_project" "stenio-techpuzzle-iac" {
  name       = "stenio-techpuzzle-iac"
  project_id = "stenio-techpuzzle-iac"
  billing_account = data.google_billing_account.acct.id
}
*/