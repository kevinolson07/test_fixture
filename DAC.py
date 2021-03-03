import smbus
import time

bus = smbus.SMBus(1)
Device_address = 0x57

bus.write_i2c_block_data(Device_address,0x80 , [0x00,0x01])
bus.write_i2c_block_data(Device_address,0x2F , [0x00,0x00])

# DAC channels 
DAC_A = 0x20
DAC_B = 0x21
DAC_C = 0x22
DAC_D = 0x23
DAC_E = 0x24
DAC_F = 0x25
DAC_G = 0x26
DAC_H = 0x27
All_DAC = 0x2F

# DAC values
DAC_value_1 = [0x29, 0x00]
DAC_value_2 = [0x99, 0x00]
DAC_value_3 = [0xCD, 0x00]
DAC_values = [DAC_value_1, DAC_value_2, DAC_value_3 ]

# auto mode
def auto_mode():
    dwell = int(input("Enter dwell time in seconds: "))
    cycles = int(input("Enter number of cycles: "))
    for a in range(cycles):
        for b in range(3):
            bus.write_i2c_block_data(Device_address,All_DAC , DAC_values[b])
            print(DAC_values[b])
            time.sleep(dwell)
    bus.write_i2c_block_data(Device_address,All_DAC , DAC_values[0])    


# Manual Mode
def manual_mode():
    x = 1
    while x:
        command_byte = int(input("Select which DAC you would like to edit (type 1-8 for A-H channels or 9 for all channels): "))
        if command_byte == 1:
            DAC_select = DAC_A
            x = 0
        elif command_byte ==2:
            DAC_select = DAC_B
            x = 0
        elif command_byte ==3:
            DAC_select = DAC_C
            x = 0
        elif command_byte ==4:
            DAC_select = DAC_D
            x = 0
        elif command_byte ==5:
            DAC_select = DAC_E
            x = 0
        elif command_byte ==6:
            DAC_select = DAC_F
            x = 0
        elif command_byte ==7:
            DAC_select = DAC_G
            x = 0
        elif command_byte == 8:
            DAC_select = DAC_H
            x = 0
        elif  command_byte == 9:
            DAC_select = All_DAC
            x = 0
        else:
            print("Invalid input")
    y = 1 
    while y:
        data_byte = int(input("Select a DAC value (1, 2 or 3 for 4mA, 15mA, or 20mA respectively): "))
        if data_byte == 1:
            DAC_value = DAC_value_1
            y = 0
        elif data_byte ==2:
            DAC_value = DAC_value_2
            y = 0
        elif data_byte ==3:
            DAC_value = DAC_value_3
            y = 0
        else: 
            print("Invalid value")
        
    bus.write_i2c_block_data(Device_address,DAC_select , DAC_value)





while 1:
    mode_select = int(input("Select 1 for auto or 2 for manual: "))
    if mode_select == 1:
        auto_mode()
    elif mode_select == 2:
        manual_mode()
