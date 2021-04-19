from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse

client = ModbusClient(method="rtu", port="/dev/ttyUSB0", stopbits=1, bytesize=8, parity='N', baudrate=9600)
connection = client.connect()

result = client.read_input_registers(2, 2, unit=1)
print(result.registers)
