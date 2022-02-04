"""
This file can mostly be disregarded
It helps solve problems when files from the code/analysis folders a run from main directory
"""

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
