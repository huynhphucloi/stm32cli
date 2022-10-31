from hw.driver.cmd import CMD


import click


@click.command
@click.option("--port", prompt = "Enter port", help="The name port")
@click.option("--baud", prompt = "Enter Baud rate", help="The Baud rate")
def main(port, baud):
  cmd = CMD(port, baud)
  cmd.init()
  cmd.open()
  cmd.cmdSendCmd(0x10, [1], 1)
  
  
  
if __name__ == "__main__":
  main()