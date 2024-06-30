import os
import csv

def delete_last_row(file_path):
  with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    lines = list(reader)
    lines.pop()

  with open(file_path, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lines)

if __name__ == '__main__':
  directory_path = '/home/radar/Desktop/ayush/dataset/02-09-2023/radar_scene3'
  for file in os.listdir(directory_path):
    if file.endswith('.csv'):
      delete_last_row(os.path.join(directory_path, file))
