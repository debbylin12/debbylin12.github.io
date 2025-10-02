def convolution_four_loops(img, kernel):
    """
    Implement 2D convolution with four loops, padding with zeros.
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
            cum = 0
            for u in range(-kh, kh+1):
                for v in range(-kw, kw+1):
                    cum += kernel[u+kh, v+kw] * padded[i-u, j-v]
            out[i-kh, j-kw] = cum
            
    return out