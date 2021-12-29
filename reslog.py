#!/bin/python3

import os
import time
import logging
import psutil
import platform
import argparse

"""
A program used to monitor system performance
"""

# Global variables
OS_TYPE = (platform.system())
CLEAR = ''
OS_DETAILS = [(platform.system()), (platform.platform())]

parser = argparse.ArgumentParser(description='ResLog by pufereq')
parser.add_argument('-v', '--verbose', help='Enable Verbose output.', action='store_true')
args = parser.parse_args()

# logging config
if args.verbose == True:
    logging.basicConfig(format='[%(levelname)s] [%(asctime)s] - %(message)s', level=logging.INFO)

def os_check():
    # OS check
    logging.info('Checking OS Version...\n\n')
    if OS_TYPE == 'Linux':
        CLEAR = 'clear'
    elif OS_TYPE == 'Windows':
        CLEAR = 'cls'
    elif OS_TYPE == 'Darwin':
        CLEAR = 'clear'
    else:
        logging.critical('Detected OS ({}) is not compatible with this program. The program will halt to prevent unwanted problems.\nYou can disable this check using --disable-os-check argument.'.format(OS_TYPE))
        input('Press Enter to exit...')
        exit()
    start_test()
    

def start_test():
    cpu_list = []

    ram_total_list = []
    ram_usage_list = []
    ram_percent_list = []
    iterations = 0
    try:
        print('ResLog\nTo stop the test press Ctrl+C.')
        while True:
            time.sleep(0.5)
            iterations += 1
            
            cpu = psutil.cpu_percent()
            ram_total = round(psutil.virtual_memory().total / (1024 * 1024), 2) # Megabytes
            ram_usage = round(psutil.virtual_memory().used / (1024 * 1024), 2) # Megabytes
            ram_percent = psutil.virtual_memory().percent

            cpu_list.append(cpu)
            ram_total_list.append(ram_total)
            ram_usage_list.append(ram_usage)
            ram_percent_list.append(ram_percent)

            cpu_avg = round(sum(cpu_list) / len(cpu_list), 3)
            ram_total_avg = sum(ram_total_list) / len(ram_total_list)
            ram_usage_avg = round(sum(ram_usage_list) / len(ram_usage_list), 3)
            ram_percent_avg = round(sum(ram_percent_list) / len(ram_percent_list), 3)
            
            logging.info('Iteration - {}; CPU - {}; RAM Total (MB) - {}; RAM Usage (MB) - {}; RAM Usage Percentage - {}'.format(iterations, cpu, ram_total, ram_usage, ram_percent))
            #logging.info('CPU List - {}; RAM Total List - {}; RAM Usage List - {}; RAM Usage Percentage List - {}'.format(cpu_list, ram_total_list, ram_usage_list, ram_percent_list))
    except KeyboardInterrupt:
        time.sleep(0.5)
        print('Complete')
        os.system(CLEAR)
        tod = time.strftime('%d.%m.%Y_%H:%M.%S')
        log = open('ResLog_{}.txt'.format(tod), 'w')
        log.write('{}\nRESULTS:\n\n\nPlatform details: {}; {}\n\nIterations ran: {}\n\nAverage CPU Usage: {}\nAverage RAM Usage (MB): {}\nAverage RAM Usage (%): {}'.format(time.strftime('%d/%m/%Y %H:%M.%S'),OS_DETAILS[0], OS_DETAILS[1], iterations, cpu_avg, ram_usage_avg, ram_percent_avg))
        print('{}\nRESULTS:\n\n\nPlatform details: {}; {}\n\nIterations ran: {}\n\nAverage CPU Usage: {}\nAverage RAM Usage (MB): {}\nAverage RAM Usage (%): {}'.format(tod, OS_DETAILS[0], OS_DETAILS[1], iterations, cpu_avg, ram_usage_avg, ram_percent_avg)) 

os_check()