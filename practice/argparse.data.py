import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x",
                        type=float,
                        default=1.0,
                        help="What is X?")
    parser.add_argument("--y",
                        type=str,
                        default='ABC',
                        choices=["ABC","DEF"],
                        help = "What is Y?")
    parser.add_argument("--z",
                        type=int,
                        default=5,
                        required=True,
                        help="What is Z?")
    args = parser.parse_args()
    print('x = ',args.x)
    print('y = ',args.y)
    print('z = ',args.z)

if __name__ == "__main__":
    main()
    # import 못하게 막고 직접 파일 실행으로만 실행하게끔 만들어주는 라인
    
