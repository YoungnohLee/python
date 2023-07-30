python argparse_example.py # default value
python argparse_example.py --epoch=200 --batch_size=256 --lr_initial=0.3
python argparse_example.py --epoch=300 --batch_size=64 --lr_initial=0.03
python argparse_example.py --epoch=400 --batch_size=32 --lr_initial=0.003

# sh 파일은 linux (ubuntu) 환경에서만 돌아가고 window 운영체제 하에서는 돌아가지 않음
# 용도 : 터미널에 각각 쳐야 하는 커맨드를 묶어서 실행할 수 있게 해줌.