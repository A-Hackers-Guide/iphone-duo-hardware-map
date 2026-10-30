# `Conv3x3SigmoidD2S`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _convPSO;
@"<MTLComputePipelineState>" _convPSO_MTL4;
{Conv3x3SigmoidD2SDescriptor="device"@"<MTLDevice>""K"S"C"S"Hout"S"Wout"S"Weights"@"NSData""QsI"f"QsRinv"f"QsW"@"NSData""Biases"@"NSData"} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufBias;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
S _mxu_version;
@"<MTLTensor>" _weightsTensor;
```

## Instance methods

```
-[Conv3x3SigmoidD2S computeGridAndTGSize];
-[Conv3x3SigmoidD2S createBuffers];
-[Conv3x3SigmoidD2S executeWithCommandBuffer:feed:target:];
-[Conv3x3SigmoidD2S executeWithMTL4CommandBuffer:feed:target:];
-[Conv3x3SigmoidD2S initWithDescriptor:library:];
-[Conv3x3SigmoidD2S setupMetalWithLibrary:];
```
