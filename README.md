# Todo

A simple todo-list APIs which provides the following functionality:  
• A list of todos   
• Create a new todo item  
• Mark a todo item as done or undone  
• Edit a todo item  
• Delete a todo item  

The project makes use of Python, Flask

##### Create virtualenv and activate

pip3 install -r requirements.txt

export FLASK_APP=app.py  
flask run  #flask run --host=0.0.0.0 (if require server to be publicly accessible)  

Request URL: http://localhost:5000/task

curl : curl --location 'http://127.0.0.1:5000/task' \
--header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
--header 'Accept-Language: en-US,en;q=0.9,hi;q=0.8' \
--header 'Cache-Control: max-age=0' \
--header 'Connection: keep-alive' \
--header 'Referer: http://127.0.0.1:5000/' \
--header 'Sec-Fetch-Dest: document' \
--header 'Sec-Fetch-Mode: navigate' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'Sec-Fetch-User: ?1' \
--header 'Upgrade-Insecure-Requests: 1' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--header 'Content-Type: application/json' \
--data '{
    
    "name" : "task_name"
    
}'

## Authors

**Prateek Sharma**
