'''
Program for reading HAN-port from AIDON-AMS with an onion Omega2+

developed by Kenneth R. Eirkehagen
'''
import serial as ser                                                     
import logging as log
import codecs                                                    
                                  
device = ser.Serial( 
        port='/dev/ttyS1',
        baudrate=9600,
        stopbits=ser.STOPBITS_ONE,
        bytesize=ser.EIGHTBITS,   
        timeout=4)
totBits = 1024                                   
                                                 
log.basicConfig(filename='HAN.log', level=log.DEBUG)
log.info('Connected to: ' + device.portstr)         
                                                    
print("Starter for alltid lokka")                   
while True:                                         
    bytes = device.read(totBits)             
    if bytes:
        log.info('Reading from HAN-port')
        print('Got %d bytes:' % len(bytes))
        log.info('Got %d bytes:' % len(bytes))
        msg = ('%02x' % int(codecs.encode(bytes, 'hex'), 16)).upper()
        msg = ' '.join(msg[i:i+2] for i in range(0, len(msg), 2))                      
        print(msg)              
        log.info(msg)                   
        log.info('Stop reading from HAN-port')
    else:                                     
        log.warning('Got nothing!')   