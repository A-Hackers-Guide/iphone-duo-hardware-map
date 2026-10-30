# `Conv3x3Stride2`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _convPSO;
@"<MTLComputePipelineState>" _convPSO_MTL4;
{Conv3x3Stride2Descriptor="device"@"<MTLDevice>""K"S"C"S"Hout"S"Wout"S"Weights"@"NSData""QsI"f"QsRinv"f"QsW"@"NSData""Biases"@"NSData""useUInt8"B"RefWeightsUInt8"@"NSData""ScalesF32"@"NSData""ZeroPointsU8"@"NSData""inputBlockK"S"useLeakyReLU"B"outZp"f} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufBias;
@"<MTLBuffer>" _bufZP;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
S _mxu_version;
@"<MTLTensor>" _weightsTensor;
```

## Instance methods

```
-[Conv3x3Stride2 computeGridAndTGSize];
-[Conv3x3Stride2 createBuffers];
-[Conv3x3Stride2 dispatchWithEncoder:argTable:feed:target:];
-[Conv3x3Stride2 executeWithCommandBuffer:feed:target:];
-[Conv3x3Stride2 executeWithMTL4CommandBuffer:feed:target:];
-[Conv3x3Stride2 executeWithMTL4CommandBuffer:feed:target:fence:];
-[Conv3x3Stride2 initWithDescriptor:library:];
-[Conv3x3Stride2 internalAllocations];
-[Conv3x3Stride2 setupMetalWithLibrary:];
```
