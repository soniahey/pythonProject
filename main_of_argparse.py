# https://docs.python.org/ko/3.5/library/argparse.html 참고
import argparse

parser = argparse.ArgumentParser(description='정수 관련 계산')

# positional arguments:
parser.add_argument('ints', metavar='N', type=int, nargs='+',
                    help='계산을 위한 정수')
# optional arguments:
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='정수들의 합 (default: 가장 큰 수 찾기)')

args = parser.parse_args()
print("결과: ", args.accumulate(args.ints))

