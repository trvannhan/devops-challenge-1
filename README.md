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
