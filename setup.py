from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name = "yahoo_ff",
    version = "1.0.5",
    author = "Alexandre Sobolevski",
    author_email = "sobolevski.a@gmail.com",
    description = "Quick module to scrape yahoo financial data for stocks.",
    license = "MIT",
    url = "http://github.com/alexandresobolevski/yahoo_ff",
    long_description=long_description,
    packages=['yahoo_ff']
)
