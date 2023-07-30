import argparse

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description = "This is Argparse Tutorial")

# 입력받을 인자값 설정(default 값 설정 가능)
parser.add_argument('--epoch', type=int, default=150)
parser.add_argument('--batch_size', type=int, default = 128)
parser.add_argument('--lr_initial', type = float, default = 0.1)

# args에 위의 내용을 저장
args = parser.parse_args()

# 입력받은 인자값 출력
print(args.epoch)
print(args.batch_size)
print(args.lr_initial)

# main.py : 모델 train/test가 이루어지는 코드
# 해당 코드에 argparse를 import하여 넣는다.
# argparse_example.sh 를 shell에서 돌린다.

