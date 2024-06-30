import os
import csv

def delete_first_row(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        lines = list(reader)
        lines = lines[1:]  # Remove the first row

    with open(file_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lines)

if __name__ == '__main__':
    directory_path = '/home/radar/Documents/fusion_dataset/scene3_radar_synch/scene3/20'
    for file in os.listdir(directory_path):
        if file.endswith('.csv'):
            delete_first_row(os.path.join(directory_path, file))
