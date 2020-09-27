import datetime
import sys

def read_time():
  inputStr = (tuple(map(int, line.split())) for line in sys.stdin)
  year, month, day = next(inputStr)   
  return datetime.datetime(year, month, day)

def main():
  date = read_time()
  daysAdd = datetime.timedelta(int(input()))
  result = date + daysAdd
  print(result.year, result.month, result.day)
    
if __name__ == "__main__":
  main()