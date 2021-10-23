resource "google_project_service" "services" {
  for_each = toset(var.services)
  project = google_project.stenio-techpuzzle-iac.id
  service = each.value
  disable_dependent_services = true
}
