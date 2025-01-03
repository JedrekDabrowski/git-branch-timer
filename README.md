# Git Branch Timer Script

This Python script automates time tracking by starting a timer in Toggl when you begin working on a Git branch. The timer is tagged with the branch name to keep track of your activities.

---

## Features

- **Git Branch Detection**: Automatically detects the current Git branch.
- **Timer Integration**: Starts a timer in Toggl or using their API.
- **Custom Tags**: Tags the timer with the Git branch name for better organization.
- **Easy Automation**: Can be scheduled to run automatically at the start of your workday.

---

## Requirements

- Python 3.8+
- Toggl account (with API access)
- Installed libraries:
  - `subprocess`
  - `requests`

---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/git-branch-timer.git
cd git-branch-timer
```

### Step 2: Install Dependencies

Ensure Python and `pip` are installed. Then, install required libraries:

```bash
pip install -r requirements.txt
```

### Step 3: Set Environment Variables

Create an environment variable file (`.env`) or export these variables:

```plaintext
TOGGL_API_KEY=your_toggl_api_key
TOGGL_WORKSPACE_ID=your_workspace_id
```

You can also export them directly in your terminal:

```bash
export TOGGL_API_KEY=your_toggl_api_key
export TOGGL_WORKSPACE_ID=your_workspace_id
```

### Step 4: Run the Script

Run the script manually:

```bash
python timer_script.py
```

Or schedule it to run automatically (see [Automation](#automation)).

---

## Automation

### Linux/macOS: Using `cron`

1. Open the crontab editor:
   ```bash
   crontab -e
   ```
2. Add the following line to schedule the script at 9 AM on weekdays:
   ```plaintext
   0 9 * * 1-5 python3 /path/to/timer_script.py
   ```

### Windows: Using Task Scheduler

1. Open Task Scheduler.
2. Create a new task.
3. Set the trigger to daily at 9 AM.
4. Set the action to run `python` with the script path as an argument.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## Disclaimer

This script is provided "as is" without warranty of any kind. Use it at your own risk.

---

## Contact

For issues or suggestions, open a GitHub issue or contact me at [jedrzejdabrowski.jd@gmail.com]
