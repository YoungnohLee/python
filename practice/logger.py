import logging

def get_logger(name=None):
    # (1) logger instance를 만듬 
    # logging.getLogger()
    logger = logging.getLogger(name)
    
    # (2) logger의 level 설정
    logger.setLevel(logging.DEBUG)
    
    # (3) formatter 지정하여 log head 구성
    ## asctime - 시간정보
    ## levelname - logging level
    ## funcName - log가 기록된 함수
    ## lineno - log가 기록된 line
    formatter  = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")
    
    # (4) handler instance를 만듦. console 및 파일로 저장할 수 있도록 함.
    console = logging.StreamHandler()
    file_handler_debug = logging.FileHandler(filename="log_debug.log", encoding="utf-8")
    file_handler_error = logging.FileHandler(filename="log_error.log", encoding='utf-8')
    
    # (5) handler level 설정
    console.setLevel(logging.INFO)
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_error.setLevel(logging.ERROR)
    
    # (6) handler format 설정
    console.setFormatter(formatter)
    file_handler_debug.setFormatter(formatter)
    file_handler_error.setFormatter(formatter)
    
    # (7) logger에 handler 추가
    logger.addHandler(console)
    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_error)
    
    # (8) log setting 반환
    return logger

# https://greeksharifa.github.io/%ED%8C%8C%EC%9D%B4%EC%8D%AC/2019/12/13/logging/#214-logger%EC%97%90-%EC%83%9D%EC%84%B1%ED%95%9C-handler-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0
