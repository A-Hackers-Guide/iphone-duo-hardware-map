# `Conv12x12Stride4`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _convPSO;
@"<MTLComputePipelineState>" _convPSO_MTL4;
{Conv12x12Descriptor="device"@"<MTLDevice>""K"S"C"S"Hout"S"Wout"S"Weights"@"NSData""QsI"f"QsRinv"f"QsW"@"NSData""Biases"@"NSData"} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufBias;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
S _mxu_version;
@"<MTLLibrary>" _library;
@"<MTLTensor>" _weightsTensor;
```

## Instance methods

```
-[Conv12x12Stride4 LoadReorderWeights];
-[Conv12x12Stride4 computeGridAndTGSize];
-[Conv12x12Stride4 createBuffers];
-[Conv12x12Stride4 dispatchWithEncoder:argTable:feed:target:];
-[Conv12x12Stride4 executeWithCommandBuffer:feed:target:];
-[Conv12x12Stride4 executeWithMTL4CommandBuffer:feed:target:];
-[Conv12x12Stride4 initWithDescriptor:library:];
-[Conv12x12Stride4 internalAllocations];
-[Conv12x12Stride4 setupMetalWithLibrary:];
```
