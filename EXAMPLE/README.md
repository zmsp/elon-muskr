
To install the script on on cron run-
```bash
crontab -e
## append the following line
0 6 * * * python3 cd /Users/username/{PROJECT_DIRECTORY} && python3 -m EXAMPLE.slacker > /tmp/cron.log # runs this everyday at 6:00 am and saves log to /tmp/cron.log
```

https://crontab.guru/examples.html