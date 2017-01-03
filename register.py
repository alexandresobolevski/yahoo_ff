import pypandoc
import os

# pandoc.core.PANDOC_PATH = '/path/to/pandoc'

rst = pypandoc.convert_file('README.md', 'rst')
f = open('README.txt','w+')
f.write(rst)
f.close()
os.system("python setup.py register sdist upload")
os.remove('README.txt')
