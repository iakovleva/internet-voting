import sys
import argparse

def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_register = subparsers.add_parser('register')
    parser_register.add_argument('voter_id', type=int)
    parser_start_node = subparsers.add_parser('start-node')
    parser_start_node.add_argument('--arguments', nargs=1)
    parser_pull = subparsers.add_parser('pull')
    parser_vote = subparsers.add_parser('vote')
    parser_sign = subparsers.add_parser('sign')
    parser_count = subparsers.add_parser('count')
    args = parser.parse_args()

    if sys.argv[1]=='register':
        print 'id: {}'.format(args.voter_id), 'subcommand: {}'.format(sys.argv[1])
    elif sys.argv[1]=='start-node':
        print 'arguments: {}'.format(args.arguments), 'subcommand: {}'.format(sys.argv[1])
    else:
        print 'subcommand: {}'.format(sys.argv[1])
    
main()
