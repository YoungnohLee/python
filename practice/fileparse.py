# fileparse.py
import csv

def parse_csv(filename):
    '''
    csv 파일을 파싱해 레코드의 목록을 작성
    파싱 : 구성 성분을 분해하여 구조를 결정함
    '''
    with open(filename) as f:
        rows = csv.reader(f) # csv.reader : row 마다 읽음. for이나 next문으로 다음 행을 읽을 수 있음
        
        # 헤더를 읽음
        headers = next(rows)
        records = []
        for row in rows:
            if not row: # 데이터가 없으면
                continue # 건너뛰어라
            record = dict(zip(headers, row))
            records.append(record)
    
    return records

def parse(f, types = None, names = None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line : continue
        try : 
            records.append(split(line,types, names, delimiter))
        except ValueError as e:
            print("parse 할 수 없습니다 :", line)
            print("이유 : ", e)
    return records

# try-except에서 경고를 출력해야하나? 아니면 무시해야하나?
# 두가지 행위를 모두 원할 수 있음
