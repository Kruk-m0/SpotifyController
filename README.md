I forgot that Fn+(f7/f9) exist so i made my own spotify forward/previous (mapped on Ctrl+f7 and Ctrl+f8)

In order to make it work, you need to create a config.py file in the main directory, that has the following:

access_token='your spotify acces token here'
client_id='your spotify client id'
client_secret='your spotify client_secret id'
refresh_token='your refresh token here'

how to get you own ids/tokens: https://developer.spotify.com/documentation/web-api/tutorials/getting-started 


and then, after running main.py, you should be able to skip and rewind songs. 

I also created these batch and vbs files to make the script run automaticly on startup.
