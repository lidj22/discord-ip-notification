# Discord IP Notification
Send a notification to Discord about the host machine's current IP address.

**Requirements**: Linux, Docker

Build the Docker image.
```sh
docker build -t discord-ip-notification .
```

Run the container to check for IP address and send a notification.
```sh
docker run -e WEBHOOK_URL=$WEBHOOK_URL discord-ip-notification
```

## Daily Notifications
> Set up a cronjob to run this everyday.

Create script `/root/send_ip_notification.sh`:
```shell
#!/usr/bin/bash
WEBHOOK_URL="your_webhook_url"
docker run -e WEBHOOK_URL=$WEBHOOK_URL discord-ip-notification
```

Add to `crontab`:
```
0 * * * * /root/send-ip-notification.sh
```
