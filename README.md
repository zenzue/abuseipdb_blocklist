# AbuseIPDB Blocklist for Nginx

This project provides a script that integrates AbuseIPDB's blacklist API with Nginx to automatically block IPs that have been reported for abusive behavior.

## Prerequisites

- Python 3
- `requests` library (Install using `pip install requests`)
- Nginx installed on your server
- An API key from AbuseIPDB

## Installation

1. **API Key**: Obtain an API key from [AbuseIPDB](https://www.abuseipdb.com).

2. **Script Setup**:
   - Download the script `update_abuseipdb_blocklist.py`.
   - Replace `your_api_key_here` in the script with your actual AbuseIPDB API key.

3. **Nginx Configuration**:
   - Ensure your Nginx configuration includes the generated blocklist. You can add the following line inside the `http` block of your Nginx configuration (`/etc/nginx/nginx.conf`):
     ```
     include /etc/nginx/blocklist.conf;
     ```

4. **Automate Script Execution**:
   - Set up a cron job to run the script at regular intervals. For daily updates, add the following line to your crontab:
     ```
     0 0 * * * /usr/bin/python3 /path/to/update_abuseipdb_blocklist.py
     ```

5. **Reload Nginx Configuration**:
   - Configure another cron job to reload Nginx daily or after the script runs to ensure that the new blocklist is used:
     ```
     5 0 * * * /usr/bin/nginx -s reload
     ```

## Usage

The script fetches the blacklist from AbuseIPDB based on the defined confidence level (default is 90), writes the IP addresses in Nginx deny format to `/etc/nginx/blocklist.conf`, and expects Nginx to be reloaded to enforce the new rules.

## Notes

- Adjust the `confidenceMinimum` in the script if you want to block IPs based on a different confidence threshold.
- Always test changes in a staging environment before applying them to your production server to avoid unintentional service disruptions.
