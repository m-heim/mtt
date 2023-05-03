import os
import argparse
import datetime
import sqlite3
from pathlib import Path


def main():
    parser = make_parser()
    args = parser.parse_args()
    
    
    args.func(args)
    
def get_datetime() -> datetime:
    return datetime.datetime.now()
    
    
def init(args: argparse.Namespace) -> bool:
    userdir = Path.home()
    mttdir = userdir / '.mtt'
    print('Initializing mtt now')
    if not mttdir.exists():
        mttdir.mkdir()
        print(f'Created {mttdir}')
        return True
    else:
        print('Nothing to do')
    return False

def start() -> None:
    current_datetime = get_datetime()
    
    

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('mtt', description='Track work time')
    subparsers = parser.add_subparsers(required=True)
    init_parser = subparsers.add_parser('init', aliases=['i'])
    start_parser = subparsers.add_parser('start')
    stop_parser = subparsers.add_parser('resume')
    
    init_parser.set_defaults(func=init)
    return parser
    