from distutils.core import setup
import io


def readme():
    with io.open('README.md', encoding="utf-8") as f:
        return f.read()

setup(
  name='kgb_rules',
  description='A commit message linter',
  long_description=readme(),
  packages=['kgb_rules'],
  version='0.0.2',
  author='Augustin Borsu',
  author_email='dev@sagacify.com',
  url='https://githubv.com/Sagacify/kgb-rules',
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: English',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Topic :: Text Processing'
  ],
  keywords='git lint russian_history',
)
