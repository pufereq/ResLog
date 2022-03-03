# ResLog
A simple program logging the resource usage.
## How does it work
The script uses `psutil()` library along with the `logging()` library.
Reads CPU, RAM, and Disk usage every 0.5s and saves it to a log file after confirmation.
## Usage
Start the program, it will monitor automatically. To end the scan, use CTRL-C. The script will save results to a file if user agreed.

## Arguments
You can enable the Verbose output mode by running the script with `--verbose` or `-v` argument.