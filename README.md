# Elab Report Downloader

## requirements 
- Install requirements with 
```python
pip3 install -r requirements.txt
```
- Requires that you don't have any `.png` file in download_path.

## Need to download 
- [Chromedriver](https://chromedriver.chromium.org/downloads) accordng to chrome version. 

## Things to set before use
- email_value.
- pwd_value.
- download_path: default download path that chrome uses, not the one that you want.
- deafult profile on line 27.
- chromedriver path in webdriver.Chrome in arg executable_path.

## Now run

```python
python3 oops_report.py
```
And then use `image_extractor.py` to get a single report from all the folders.
