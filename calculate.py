import math_lib
import argparse


def main(temp_F):
    tmp = math_lib.add(temp_F, -32)
    degrees_c = math_lib.div(tmp, 9/5)
    print(str(temp_F), "degrees F equals", str(degrees_c), "degrees C")
    return degrees_c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="F to C calculator",
                                     prog="calculate.py")

    parser.add_argument("--temp_F",
                        type=float,
                        help="Temperature (degrees F)",
                        required=True)

    args = parser.parse_args()
    main(args.temp_F)
