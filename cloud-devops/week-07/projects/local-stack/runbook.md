# Reproducible local start — learner completion required

## Fill after implementation (L12)
Start directory: notes-repo/cloud-devops/week-07/projects/local-stack
Prerequisites: Docker daemon access, Compose with --wait, available host port, image/package download access, sufficient disk/RAM. No GPU/cloud account.
Target one command: `docker compose --env-file .env.example up --build --wait --wait-timeout 120`
Actual checked version / date / result:
Manual health/ready and sample upload/job commands:
Expected service list / ports / volume targets:
Stop preserving data: `docker compose --env-file .env.example down`
Debugging pointer and known limits:

## Fresh local clone trial — only after your intended changes are committed
From the notes repository root, inspect git status and the intended commit. Choose an unused destination name and an unused Compose project name. Do not remove an existing copy to make space for this check.

```bash
mkdir -p cloud-devops/week-07/artifacts
git clone --no-hardlinks . cloud-devops/week-07/artifacts/fresh-trial-01
cd cloud-devops/week-07/artifacts/fresh-trial-01/cloud-devops/week-07/projects/local-stack
API_PORT=8078 docker compose -p week7-fresh-trial-01 --env-file .env.example up --build --wait --wait-timeout 120
```

This local clone sees committed files only. --no-hardlinks makes Git object storage independent. The ignored artifacts folder holds generated copies, not teaching material. The unique -p project name isolates networks/volumes; changing the host port avoids colliding with the original stack. Verify 8078 is free first. Do not set container_name in your Compose file.

From this fresh project's directory, use curl to check /health and /ready on 8078, upload `@data/hello.txt` with the public key/type headers and poll the returned job. Use a Python environment only if you also want to run smoke.py; one-command Compose startup should not require a host venv. Probe vector via docker compose exec api as in L10. Then stop with the same -p and env-file arguments and down, without deleting volumes.

Evidence: source commit, exact command/directory, initial cache state, service status, completed job and remaining limitations. A clone on the same host is a clean-checkout test, not proof for all CPU architectures or an empty image cache.
