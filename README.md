# Project

This project contains scraper scripts which I needed to build for different reasons.


## NCSC advisories

```
→ python3 ncsc/ncsc.py -h
usage: ncsc.py [-h] [-n N] [-p] [-w WRITEFILE]

A scraper for fetching advisories from the ncsc.nl website.

optional arguments:
  -h, --help            show this help message and exit
  -n N                  Number of advisories to fetch (default: 5)
  -p, --pgp,            Enable PGP signature verification (default: False)
  -w WRITEFILE, --writefile WRITEFILE
                        Write output to file (default: None)
```
