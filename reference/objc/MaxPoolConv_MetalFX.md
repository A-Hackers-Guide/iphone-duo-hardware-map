# `MaxPoolConv`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _pso;
{MaxPoolConvDescriptor="device"@"<MTLDevice>""C"S"K3"S"K1"S"Khead"S"Hout"S"Wout"S"poolStride"S"Weights3x3"@"NSData""Weights1x1"@"NSData""WeightsHead"@"NSData""Biases"@"NSData""act3"I"act1"I"actHead"I"quantScheme"I"useBilinear"B"useSkip"B"CSkip"S"skipChannelStride"S"DqsBilinearImage"f"DqsSkip"f"nmatsHW"S"nmatsK"S"nsimd_per_tg"S"QsW"@"NSData""ZeroPointsU8"@"NSData""QsI"f"QsRinv"f} _desc;
@"<MTLComputePipelineState>" _bilinearPSO;
@"<MTLBuffer>" _scratchBuf;
{?="width"Q"height"Q"depth"Q} _bilinearThreadsPerGrid;
{?="width"Q"height"Q"depth"Q} _bilinearThreadsPerTG;
@"<MTLBuffer>" _bufWeights3x3;
@"<MTLBuffer>" _bufWeights1x1;
@"<MTLBuffer>" _bufWeightsHead;
@"<MTLBuffer>" _bufBias;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufZeroPoints;
@"<MTLTensor>" _tWeights3x3;
@"<MTLTensor>" _tWeights1x1;
@"<MTLTensor>" _tWeightsHead;
S _mxu_version;
S _nmatsHW;
S _nmatsK;
S _wElemsPerTG;
S _hElemsPerTG;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
```

## Instance methods

```
-[MaxPoolConv computeGridAndTGSize];
-[MaxPoolConv createBuffers];
-[MaxPoolConv dispatchWithEncoder:argTable:feed:skip:target:];
-[MaxPoolConv executeWithCommandBuffer:feed:skip:target:];
-[MaxPoolConv initWithDescriptor:library:];
-[MaxPoolConv internalAllocations];
-[MaxPoolConv prepareImageTensorFeed:];
-[MaxPoolConv scratchBuffer];
-[MaxPoolConv setupMetalWithLibrary:];
```
