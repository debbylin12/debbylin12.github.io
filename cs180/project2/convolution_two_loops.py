def convolution_two_loops(img, kernel):
    """
    Implement 2D convolution with two loops, padding with zeros.
        img - 2D array;
        kernel - 2D (h x w) array, h and w must be odd number;
    """
    kh, kw = kernel.shape[0] // 2, kernel.shape[1] // 2

    # Padding with zeros
    padded = np.pad(img, ((kh,), (kw,)), mode='constant')

    h, w = padded.shape
    out = np.zeros_like(img, dtype=np.float32)

    for i in range(kh, h-kh):
        for j in range(kw, w-kw):
            cropped = padded[i-kh:i+kh+1, j-kw:j+kw+1]
            out[i-kh, j-kw] = np.sum(cropped * np.flip(kernel))
            
    return out