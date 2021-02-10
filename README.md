# In musk we trust  
This project looks for specific keywords from any twitter account including Elon musk's.  

To use this script, Twitter API key is needed. Its free!    
https://developer.twitter.com/en/portal/dashboard  
 
  
 
The project can be extended to forward messages to slack and use Google Spreadsheet to configure keywords. 
See EXAMPLE folder for usage.  
  
## Screenies  

Slack:![slack](https://i.imgur.com/5qzxqLb.png)  
Google Spreadsheet:![google-docs](https://i.imgur.com/M52iCaW.png)


## Running it in a time interval via cron
To install the script on on cron run-
```bash
crontab -e
0 6 * * * python3 cd /Users/username/{PROJECT_DIRECTORY} && python3 -m EXAMPLE.slacker > /tmp/cron.log # runs this everyday at 6:00 am and saves log to /tmp/cron.log
```

https://crontab.guru/examples.html