from distutils.core import setup
setup(
  name = 'qwipy',
  packages = ['qwipy'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Quick Web Interfacing (QwiPy) for Python 3.5+ is a client-side rendering framework for Python 3.5+ using async/await handlers.',
  author = 'Shawn Niederriter',
  author_email = 'shawnhitsback@gmail.com',
  url = 'https://github.com/Sniedes722/qwipy', # use the URL to the github repo until it get a readthedocs
  download_url = 'https://github.com/Sniedes722/qwipy', # Make tarballs
  keywords = ['framework', 'development', 'web' , 'asyncio', 'async', 'real-time'], # arbitrary keywords
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Operating System :: Linux x86_64',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)