#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 00:37:38 2020

@author: amr
"""

# Function to calculate CRC for a message
def crc(msg, divisor, code):
    # Put the code at the end of the message (append code to message)
    msg = msg + code 
    # Convert into list form for easier handling
    code = list(code)
    msg = list(msg)
    divisor = list(divisor)
    # Loop over every message bit minus the appended code
    for i in range(len(msg)-len(code)):
        # If the messsage bit is 1, perform modulo 2 multiplication
        if msg[i] == '1':
            for j in range(len(divisor)):
                # Perform modulo 2 multiplication on each index of the divisor
                msg[i+j] = str((int(msg[i+j])+int(divisor[j]))%2)

    # Output the error-checking code at the end of the message
    return ''.join(msg[-len(code):])

# Enter the message and divisor
msg = input('Input message to send: ')
divisor = input('Input divisor: ')
code = ''
code = code.zfill(len(divisor)-1)
# Calculate the error-checking code
CRC = crc(msg, divisor, code)
print()
print('CRC = ', CRC)

# Enter the received message and perform CRC test on the message
received = input('Input received message: ')
check = crc(received[:len(received)-len(code)], divisor, received[-len(code):])

# Check if the message was correctly received
print('Message was sent correctly? ', check == code) # Check if the remainder is zero 
print('Receiver should receive = ', msg + CRC)