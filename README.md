# Batch-Geocoder
The batch geocoder which can convert mass address data to geocoding data. It supports Python3.

### Installation
```
pip install -r requirements.txt
```

### Usage
- Paste your address list to data.xlsx
- Run python
```
$ python regeocoding.py
```
- (Optional) If you want to use your own Google map API key, you can define them in your system's environment variables before running program.
```
$ export GOOGLE_API_KEY=<Secret API Key>
$ export GOOGLE_CLIENT=<Secret Client>
$ export GOOGLE_CLIENT_SECRET=<Secret Client Secret>
$ python regeocoding.py
```

### Source File Format
- File name : data.xlsx
- Row 1 is the Header (Please don't modify the header name)
- Columns
 - Address

### Result File Format
- File name: result.xls (Due to xlwt's limitation, it can't produce xlsx format file)
- Row 1 is the Header
- Columns
 - Address
 - Lat
 - Lng
 - Error (shows error message there, if any error occurs)
 
