import csv
import argparse
import sys
from tqdm import tqdm


def transcript_parser(filepath: str, filename: str):
    """
    This function parses transcript txt file and refine to csv file

    :param filepath: transcript txt file location
    :param filename: transcript txt filename (parse_ header will be applied on the CSV filename)
    :return: None
    """
    original_txt_file = filename + '.txt'
    parsed_file = 'parsed_' + filename + '.csv'
    csvf = open(filepath + parsed_file, "w")
    wr = csv.writer(csvf, dialect='excel')
    wr.writerow(['name', 'time', 'contents'])

    with open(filepath + original_txt_file, 'r') as fp:
        x = []
        for cnt, line in tqdm(enumerate(fp)):
            if cnt % 3 == 0:
                tmp = line.split(":", 1)
                tmp[1] = tmp[1].replace(" ", "").replace("(", "").replace(")", "").replace("\n", "")
                x.extend(tmp)
                # print(tmp)
            elif cnt % 3 == 1:
                x.extend([line.replace("\n", "")])
            else:
                wr.writerow(x)
                x = []
                continue
    csvf.close()
    print('Saved in "{}"'.format(filepath + parsed_file))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", help="Filepath, ends with / (ex. 'dataset/')", dest="filepath",
                        type=str, required=True)
    parser.add_argument("--filename", help="Filename (ex. 'transcript_1_p2')", dest="filename", type=str, required=True)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    return args


if __name__ == "__main__":
    # filepath = 'dataset/'
    # filename = 'transcript_1_p2'

    args = parse_args()
    filepath = args.filepath
    filename = args.filename
    transcript_parser(filepath, filename)

