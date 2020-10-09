from reu_split import split_dataset

import argparse
import random


def run():
    parser = argparse.ArgumentParser(
        description="Split folders with files (e.g. images) into training, validation and test(dataset) folders."
    )
    parser.add_argument(
        "--output",
        default="output",
        help="directory where to write the resulting split folders, defaults to `output`",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default= random.seed(),
        help="a seed value to make your split reproducible",
    )
    parser.add_argument(
        "--input",
        help="directory with the input data. The directory needs to have the labels as sub-directories. In those sub-directories are then the actual files that gets split.",
    )
    parser.add_argument(
        "--ratio",
        nargs="+",
        type=float,
        help="The ratio to split formatted (train,val,test)."
    )

    args = parser.parse_args()

    print(args.ratio)
    print(type(args.ratio))
    print(args.ratio[1])

    print(args.input)
    print(type(args.input))

    if args.ratio[0] + args.ratio[1] + args.ratio[2] != 1:
        print("Sum of ratios must add up to 1")

    split_dataset(args.input, args.output, args.ratio, args.seed)

if __name__ == '__main__':
    run()
