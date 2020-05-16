Shaper to google translate
---
### what is this?
WIP

### how to install
1. clone repository
```
git clone https://github.com/swkky/text_shaping_for_translate
cd text_shaping_for_translate
```

2. start app
if you already installed `flask`, following command will be available.
```
python3 run.py
```

if you are docker user, following command will be available.
```
docker build -t shaper_to_gt . 
docker run -p 5000:5000 --rm -it shaper_to_gt 
```
or
```
sh build.sh
```
`docker run` command is available at any directory. So I recommend you to make docker image.

3. go to browser

Enter address.
```
http://0.0.0.0:5000/
```
