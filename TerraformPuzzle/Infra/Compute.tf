resource "google_compute_disk" "disk" {
  name  = "my-instance"
  zone  = "us-central1-a"
  # project = data.google_project.stenio-techpuzzle-iac.id
  physical_block_size_bytes = 4096
  size = 10
  image = "debian-10"
  type = "pd-balanced"
}


resource "google_compute_instance" "default" {
  name         = "my-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  # project = data.google_project.stenio-techpuzzle-iac.id

  shielded_instance_config {
      enable_integrity_monitoring = true
      enable_secure_boot = true
      enable_vtpm = true
  }
  network_interface {
    subnetwork = google_compute_subnetwork.us-central1.id
  }

  boot_disk {
    source = google_compute_disk.disk.id
  }

  allow_stopping_for_update = true

  service_account {
    scopes = var.svc_acc_scopes
  }
}