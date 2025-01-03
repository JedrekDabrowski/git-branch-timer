import os
import subprocess
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Toggl API Configuration
TOGGL_API_KEY = os.getenv("TOGGL_API_KEY")
TOGGL_WORKSPACE_ID = os.getenv("TOGGL_WORKSPACE_ID")
TOGGL_BASE_URL = "https://api.track.toggl.com/api/v9"

if not TOGGL_API_KEY or not TOGGL_WORKSPACE_ID:
    raise EnvironmentError("Missing TOGGL_API_KEY or TOGGL_WORKSPACE_ID in environment variables.")

# Get current git branch
def get_git_branch():
    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL
        ).strip().decode("utf-8")
        return branch
    except subprocess.CalledProcessError:
        return "unknown_branch"

# Start a Toggl Timer
def start_timer(branch_name):
    url = f"{TOGGL_BASE_URL}/time_entries"
    headers = {"Content-Type": "application/json"}
    auth = (TOGGL_API_KEY, "api_token")

    payload = {
        "description": f"Working on branch: {branch_name}",
        "start": datetime.utcnow().isoformat() + "Z",
        "duration": -1,  # Toggl timer runs until stopped
        "tags": [branch_name],
        "workspace_id": TOGGL_WORKSPACE_ID,
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)
    if response.status_code in [200, 201]:
        print(f"Started timer for branch: {branch_name}")
    else:
        print(f"Failed to start timer: {response.status_code}, {response.text}")

# Main Function
if __name__ == "__main__":
    branch = get_git_branch()
    if branch == "unknown_branch":
        print("Not in a Git repository or unable to determine the branch.")
    else:
        start_timer(branch)
