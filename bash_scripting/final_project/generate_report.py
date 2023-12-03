import re

def generate_user_report(syslog_file_path):
   # Use a dictionary to count the occurrences of each error message
   user_report = {}

   # Read the syslog file line by line
   with open(syslog_file_path, 'r') as file:
      user_pattern = r'User  \((\w+)\)$'
      for line in file:
         line = line.strip()
         user_part = re.search(user_pattern, line)
         if "ticky" not in line or not user_part:
            continue
         username = user_part[1]
         user_report[username] = user_report.get(username, {'infos': 0, 'errors': 0})
         if "ERROR" in line:
            user_report[username]['errors'] = user_report[username]['errors'] + 1
         if "INFO" in line:
            user_report[username]['infos'] = user_report[username]['infos'] + 1
   sorted_report = dict(sorted(user_report.items()))
   print(sorted_report)

def count_errors(syslog_file_path):
   error_count = {}

   with open(syslog_file_path, 'r') as file:
      error_pattern = r'ERROR: (.+) - (User .+)$'
      for line in file:
         line = line.strip()
         if "ticky" not in line:
            continue
         error_line = re.search(error_pattern, line)
         if(not error_line):
            continue
         error_count[error_line[1]] = error_count.get(error_line[1], 0) + 1
   sorted_error_count = dict(sorted(error_count.items(), key= lambda item: item[1], reverse=True))
   print(sorted_error_count)

# Example usage:
syslog_path = "/home/kratosgado/projects/python/python_automation/bash_scripting/log.txt"
# generate_user_report(syslog_path)
count_errors(syslog_path)
