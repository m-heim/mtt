import os
import argparse


def main():
    parser = make_parser()
    args = parser.parse_args()
    
    
    args.func(args)
    
    
def init(args: argparse.Namespace) -> bool:
    userdir = os.path.expanduser('~')
    mttdir = os.path.join(userdir, '.mtt')
    print('Initializing mtt now')
    if not os.path.isdir(mttdir):
        os.mkdir(mttdir)
        return True
    return False
    

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('mtt', description='Track work time')
    subparsers = parser.add_subparsers(required=True)
    init_parser = subparsers.add_parser('init', aliases=['i'])
    start_parser = subparsers.add_parser('start')
    stop_parser = subparsers.add_parser('resume')
    
    init_parser.set_defaults(func=init)
    return parser
    