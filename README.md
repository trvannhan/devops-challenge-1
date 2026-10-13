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
