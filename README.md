# eLab Report Downloader

## Requirements 
- Install requirements with 
```python
pip3 install -r requirements.txt
```
- Requires that you don't have any `.png` file in download_path.

## Need to download 
- [Chromedriver](https://chromedriver.chromium.org/downloads) accordng to chrome version. 

## Things to set before use
- email_value - line 10.
- pwd_value - line 13.
- url (the link to the eLab that you want to download the report from) - line 17.
- download_path (default download path that chrome uses, not the one that you want) - line 21.
- default profile - line 30.
- chromedriver path in webdriver.Chrome in arg executable_path - line 42.

## Now run

```python
python3 reports_download.py
```
And then use `image_extractor.py` to get a single report from all the folders.
