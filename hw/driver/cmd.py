from uart import UART
from bsp import delay, millis

CMD_STX =                 0x02
CMD_EXT =                 0x03

CMD_STATE_WAIT_STX=       0
CMD_STATE_WAIT_CMD=       1
CMD_STATE_WAIT_DIR=       2
CMD_STATE_WAIT_ERROR=     3
CMD_STATE_WAIT_LENGTH_L=  4
CMD_STATE_WAIT_LENGTH_H=  5
CMD_STATE_WAIT_DATA=      6
CMD_STATE_WAIT_CHECKSUM=  7
CMD_STATE_WAIT_ETX=       8

CMD_MAX_DATA_LENGTH=      256

class CmdPacket:
  cmd = 0
  dir = 0
  error = 0
  length = 0
  check_sum = 0
  check_sum_recv = 0
  buffer = []
  data= 0

class CMD:
  is_init = False
  state = CMD_STATE_WAIT_STX
  pre_time = 0
  index = 0
  error = 0
  rx_packet = CmdPacket()
  tx_packet = CmdPacket()
  
  def __init__(self, ch, baud):
    self.uart = UART(ch, baud)
    
  def init(self):
    self.is_init = True
    self.state = CMD_STATE_WAIT_STX

  def open(self):
    self.pre_time = millis()
    return self.uart.open()
  
  def close(self):
    return self.uart.close()
  
  def cmdReceivePacket(self):
    
  