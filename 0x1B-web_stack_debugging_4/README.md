Webstack Debugging #4
Resources: https://stackoverflow.com/questions/27849331/how-to-set-nginx-max-open-files
How to debug:
Run ApacheBench to simulate requests to server ab -c 100 -n 2000 localhost/
Look on /var/log/nginx/error.log. for errors and find "accept4() failed (24: Too many open files)"
Google error message and try different solutions pertaining to resetting max files open limit 1 2
Ultimate solution that solved the issue is modifying limit in /etc/default/nginx file
Execute puppet script to automate solving issue across magnitude of servers puppet apply [0-filename]
