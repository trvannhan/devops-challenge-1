## Part 1 – Manual Deployment

### Manual Deployment Steps and Automation Opportunities

The application was manually deployed on Ubuntu using the following steps:

| Manual Step | Can Be Automated? |
|---|---|
| Clone or update the source code using Git | Yes |
| Create a Python virtual environment (venv) | Yes |
| Install dependencies using pip | Yes |
| Start or restart the application | Yes |
| Verify the application using curl | Yes |
| Investigate deployment failures | Requires human intervention |

### Reflection

Manual deployment requires developers to execute multiple commands individually. This process is time-consuming and can lead to human errors.

By using a Bash deployment script, tasks such as updating source code, installing dependencies, restarting services, and performing health checks can be automated.

This makes deployment faster, more consistent, and easier to repeat.
## Part 2 – Git Workflow

### Objective
Use Git branches to manage source code changes without directly modifying the main branch.

### Steps Performed

1. Created a new branch named `feature/teamNHM`.
2. Modified `app.py` to display "DevOps Challenge 1 - Team NHM".
3. Used `git add app.py` to stage the changes.
4. Created a commit using `git commit`.
5. Switched back to the `main` branch.
6. Merged `feature/teamNHM` into `main`.
7. Pushed the updated `main` branch to GitHub.

### Git Workflow Explanation

- **Working Directory:** Where developers modify source code.
- **Staging Area:** Where selected changes are prepared using `git add`.
- **Commit:** Saves a snapshot of staged changes to the local Git repository.
- **Remote Repository:** GitHub stores the shared version after `git push`.

### Result

The feature branch was successfully merged into `main`. The application homepage displays "DevOps Challenge 1 - Team NHM".
## Part 3 – systemd Service

### Objective

Run the Flask application as a Linux service using systemd, so the application can run in the background without keeping a terminal open.

### Service Configuration

The application is deployed in `/opt/devops-app`.

The systemd service file is stored at `systemd/devops-app.service`.

The service configuration includes:

- **User:** `vannhan`
- **WorkingDirectory:** `/opt/devops-app`
- **ExecStart:** `/opt/devops-app/venv/bin/python /opt/devops-app/app.py`
- **Restart:** `always`
- **RestartSec:** `3`

### Service Management

The following commands are used to manage the application:

```bash
sudo systemctl daemon-reload
sudo systemctl enable devops-app
sudo systemctl start devops-app
sudo systemctl stop devops-app
sudo systemctl restart devops-app
sudo systemctl status devops-app
```

### Why is systemd better than running the application in a terminal?

Running the Flask application directly in a terminal requires manually starting and managing the process.

Using systemd provides several benefits:

- The application runs in the background.
- It does not depend on keeping the terminal open.
- It can start automatically when Ubuntu boots.
- It can restart automatically if the application process stops.
- We can manage the application using `systemctl`.
- We can investigate application logs using `journalctl`.

### Verification

The systemd service was successfully started and returned `active (running)`.

The application was tested using:

```bash
curl http://127.0.0.1:5000
curl http://127.0.0.1:5000/health
```

The homepage returned `DevOps Challenge 1 - Team NHM`, and the health endpoint returned `{"status":"ok"}`.
## Part 4 – Nginx Reverse Proxy

### Objective

Configure Nginx as a reverse proxy so users can access the Flask application through port 80 instead of port 5000.

### Architecture

Browser → Nginx (Port 80) → Flask Application (127.0.0.1:5000)

### Nginx Configuration

The Nginx configuration is stored in `nginx/devops-app.conf`.

- `listen 80`: Nginx listens for HTTP requests on port 80.
- `server_name _`: Defines the server name used for this configuration.
- `proxy_pass`: Forwards requests to the Flask application.
- `proxy_set_header Host`: Passes the original Host header.
- `proxy_set_header X-Real-IP`: Passes the client IP address.

### Deployment Steps

1. Created the Nginx configuration file.
2. Copied the configuration to `/etc/nginx/sites-available/devops-app`.
3. Enabled the configuration using a symbolic link in `/etc/nginx/sites-enabled/`.
4. Disabled the default Nginx website.
5. Tested the configuration using `sudo nginx -t`.
6. Reloaded Nginx using `sudo systemctl reload nginx`.

### Verification

The following commands were used to verify the reverse proxy:

`curl http://localhost`

Result: `DevOps Challenge 1 - Team NHM`

`curl http://localhost/health`

Result: `{"status":"ok"}`

### Troubleshooting

During configuration, Nginx initially displayed the default welcome page instead of forwarding requests to Flask.

We investigated the enabled site configurations and found that the default website was still active.

We also encountered an Nginx configuration syntax error. After correcting the configuration and copying it to the correct location, `nginx -t` passed successfully.

Finally, we reloaded Nginx and verified that both the homepage and health endpoint worked correctly.
## Part 5 – Environment Configuration

### Objective

Separate application configuration from source code using environment variables.

### Environment Variables

| Variable | Description | Example |
|---|---|---|
| APP_NAME | Application name displayed on the homepage | DevOps Challenge 1 - Team NHM |
| APP_ENV | Application environment | production |
| APP_PORT | Port used by Flask | 5000 |

### Configuration

The application uses `os.getenv()` to read environment variables.

The `.env.example` file provides sample configuration values.

The actual environment configuration is stored at `/etc/devops-app.env` and is loaded by systemd using:

`EnvironmentFile=/etc/devops-app.env`

### Verification

We changed `APP_NAME` to `DevOps Challenge 1 - Environment Test` without modifying `app.py`.

After restarting the service with `sudo systemctl restart devops-app`, the homepage displayed the new application name.

This confirms that the application reads configuration from environment variables.

### Why Separate Configuration from Source Code?

Separating configuration makes the application easier to maintain and deploy across different environments.

It allows configuration changes without modifying source code and helps prevent sensitive information from being committed to GitHub.
