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
