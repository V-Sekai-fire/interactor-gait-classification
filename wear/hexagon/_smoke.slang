[AutoPyBindCUDA]
[CUDAKernel]
void scale(TensorView<float> inp, TensorView<float> outp, float k) {
    uint i = cudaThreadIdx().x + cudaBlockIdx().x * cudaBlockDim().x;
    if (i >= inp.size(0)) return;
    outp[i] = inp[i] * k;
}
