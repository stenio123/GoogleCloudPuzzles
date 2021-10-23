resource "google_compute_subnetwork" "us-central1" {
  name          = "us-central1"
  #project      = data.google_project.stenio-techpuzzle-iac.id
  ip_cidr_range = "10.1.0.0/16"
  region        = "us-central1"
  network       = google_compute_network.my-vpc.id
  private_ip_google_access = false
  private_ipv6_google_access = "DISABLE_GOOGLE_ACCESS"
  purpose       = "PRIVATE"
}

resource "google_compute_network" "my-vpc" {
  name                    = "my-vpc"
  #project                 = data.google_project.stenio-techpuzzle-iac.id
  auto_create_subnetworks = false
  mtu =  1460
  routing_mode = "REGIONAL"
}

resource "google_compute_firewall" "allow-ssh" {
  name    = "allow-ssh"
  #project = data.google_project.stenio-techpuzzle-iac.id
  network = google_compute_network.my-vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
  source_ranges = ["0.0.0.0/0"]
}