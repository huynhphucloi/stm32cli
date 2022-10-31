from hw.driver.uart import UART


import click


@click.command
@click.option("--port", prompt = "Enter port", help="The name port")
@click.option("--baud", prompt = "Enter Baud rate", help="The Baud rate")
def main(port, baud):
  
  uart = UART(port, baud)
  uart.open()
  
  
if __name__ == "__main__":
  main()