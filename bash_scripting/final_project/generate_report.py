import re

def rank_syslog_errors(syslog_file_path):
   # Define a regex pattern for extracting error messages
   error_pattern = r'ERROR (.+)$'
   info_pattern = r'INFO (.+)$'

   # Use a dictionary to count the occurrences of each error message
   error_counts = {}

   # Read the syslog file line by line
   with open(syslog_file_path, 'r') as file:
      for line in file:
         line = line.strip()
         error_line = re.search(error_pattern, line)
         info_line = re.search(info_pattern, line)
         
         if(error_line):
            error_line = line[error_line.start():error_line.end()].split('-')
            error_message, user = error_line[0], error_line[1]
            if(error_message in error_counts.keys()):
               error_counts[error_message] += 1
            else:
               error_counts[error_message] = 1
         if(info_line):
            user_part = info_line.string.split('-')[1]
            print(user_part)

   print(error_counts)

# Example usage:
syslog_path = "/home/kratosgado/projects/python_automation/bash_scripting/log.txt"
rank_syslog_errors(syslog_path)
