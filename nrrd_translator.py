import argparse
import nrrd
import csv
import numpy as np


def read_nrrd(file):
    data, header = nrrd.read(file)

    return [data, header]


def read_csv(file_name):
    data = {}

    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader, None)  # skip the header
        for row in reader:
            # identifier = int(row[0])
            value_1 = int(row[1])
            value_2 = int(row[2])

            data[value_1] = value_2

    return data


def translate(nrrd_file, dimensions, csv_data, vis=False):
    print('Creating array of zeroes')
    array = np.zeros(dimensions, dtype=np.ubyte)

    print('Filling array with values')
    # Iterate through every array position
    for i in range(len(nrrd_file)):
        for j in range(len(nrrd_file[i])):
            for k in range(len(nrrd_file[i][j])):
                if nrrd_file[i, j, k] != 0:
                    # Find corresponding position in csv_data and insert value
                    try:
                        if vis:
                            value = 1
                        else:
                            value = csv_data[nrrd_file[i, j, k]]
                    except ValueError:
                        # If not found either set 0 for normal operation,
                        # or 2 if we explicitly want to visualize positions of missing measurements in the dataset
                        if vis:
                            value = 2
                        else:
                            print('Id ' + str(nrrd_file[i, j, k]) + ' is not in supplied list. Using 0 instead.')
                            value = 0

                    # Note: ubyte is used. If values > 255 are possible => change to e.g. ushort
                    array[i, j, k] = np.ubyte(value)

    return array


def write_nrrd(data, header, target_file):
    # Set filename to write into
    filename = str(target_file) + ".nrrd"

    # write our array into a .nrrd file
    nrrd.write(filename, data, header)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create mapping from id to generation')
    parser.add_argument('-i', '--id', action='store', type=str, required=True,
                        help='.nrrd file containing ids')
    parser.add_argument('-c', '--csv', action='store', type=str, required=True,
                        help='.csv file containing id/generation list')
    parser.add_argument('-f', '--filename', action='store', type=str, required=True, help='Name of output file')
    parser.add_argument('-m', '--missing', action='store_true', required=False,
                        help='Visualize missing values (no other translation will be performed)')

    args = parser.parse_args()

    nrrd_id_file_path = args.id
    csv_gen_file_path = args.csv
    output_filename = args.filename
    visualization = args.missing

    print('Reading .nrrd')
    nrrd_id_data = read_nrrd(nrrd_id_file_path)
    nrrd_id_body = nrrd_id_data[0]
    nrrd_id_header = nrrd_id_data[1]
    print('Reading .csv')
    csv_gen_file = read_csv(csv_gen_file_path)
    print('Doing translation')
    nrrd_output_data = translate(nrrd_id_body, nrrd_id_header.get('sizes'), csv_gen_file, visualization)
    print('Writing output')
    write_nrrd(nrrd_output_data, nrrd_id_header, output_filename)
