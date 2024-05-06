# Discord IP Notification
Send a notification to a Discord room about the host machine's current public IP address.

**Requirements**: Linux, Docker

## Usage
```sh
docker pull ghcr.io/lidj22/discord-ip-notification
```

Run (ensure Discord webhook URL is included):
```sh
docker run -e WEBHOOK_URL=$WEBHOOK_URL ghcr.io/lidj22/discord-ip-notification
```
A notification should pop up in the corresponding Discord room.

### Cronjob (Daily Notifications)
> Set up a cronjob to run this everyday.

Create script `/root/send_ip_notification.sh`.
```shell
#!/usr/bin/bash
WEBHOOK_URL="your_webhook_url"
docker run -e WEBHOOK_URL=$WEBHOOK_URL ghcr.io/lidj22/discord-ip-notification
```
Run `chmod +x /root/send_ip_notification.sh`, and add to `crontab`:
```
0 * * * * /root/send_ip_notification_.sh
```

## Build from Source

Build the Docker image.
```sh
docker build -t discord-ip-notification .
```

Run the container to check for IP address and send a notification.
```sh
docker run -e WEBHOOK_URL=$WEBHOOK_URL discord-ip-notification
```