import logging
log = logging.getLogger(__name__)

def parse(f, types=None, names=None, delimiter=None):
    records=[]
    for line in f:
        line = line.strip()
        if not line : continue
        try : 
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            # 경고 메세지를 출력 + 조용히 무시
            log.warning("Couldn't parse : %s", line)
            log.debug("Reason : %s", e)