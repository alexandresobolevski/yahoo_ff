from distutils.core import setup

import os
long_description = 'Add a fallback short description here'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name = "yahoo_ff",
    version = "1.0.19",
    author = "Alexandre Sobolevski",
    author_email = "sobolevski.a@gmail.com",
    description = "Quick module to scrape yahoo financial data for stocks.",
    license = "MIT",
    url = "http://github.com/alexandresobolevski/yahoo_ff",
    long_description=long_description,
    packages = ['yahoo_ff', 'yahoo_ff/tools']
)
