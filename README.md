We are cooked

create user 'group_international'@localhost identified by 'EEKPAMSMAW';
grant create, select, insert, update on flight_game.* to group_international@localhost;

For alex; https://opentdb.com/api_config.php

Apit tehty : 
pickpocket


When game is done/ready for testing with class remove the comments marked with #!#, these implicate updates to the class witch doesnt work while testing since the player object is created at the beginning of the game

if jsons dont want to work with javascript, you can wrap the dictionary in a list so it should work eg. 
``` python
result_json = [result]
return jsonify(result_json)
```