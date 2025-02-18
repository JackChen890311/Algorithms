import numpy as np

def conv2d(input_data, kernel, stride=1, padding=0, dilation=1):
    in_height, in_width = input_data.shape
    ker_height, ker_width = kernel.shape

    input_data = np.pad(input_data, padding)

    valid_ker_height = ker_height + (ker_height - 1) * (dilation - 1)
    valid_ker_width = ker_width + (ker_width - 1) * (dilation - 1)

    out_height = (in_height + padding * 2 - valid_ker_height) // stride + 1
    out_width = (in_width + padding * 2 - valid_ker_width) // stride + 1
    out = np.zeros((out_height, out_width))

    for i in range(out_height):
        for j in range(out_width):
            out[i][j] = np.sum(
                input_data[
                    i * stride : i * stride + valid_ker_height : dilation, 
                    j * stride : j * stride + valid_ker_width : dilation
                ] * kernel)
    return out
            

if __name__ == "__main__":
    input_data = np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])

    kernel = np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ])

    print("Convolution Output:")
    output = conv2d(input_data, kernel, stride=2, padding=2, dilation=1)
    print(output)


