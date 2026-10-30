# `Conv3x3Stride1`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _convPSO;
@"<MTLComputePipelineState>" _bilinearPSO;
@"<MTLBuffer>" _scratchBuf;
{Conv3x3Stride1Descriptor="device"@"<MTLDevice>""K"S"C"S"CSkip"S"Hout"S"Wout"S"Weights"@"NSData""useBilinear"B"useFusedBilinear"B"DqsBilinearImage"f"DqsSkip"f"QsI"f"QsRinv"f"QsW"@"NSData""Biases"@"NSData""RefWeightsUInt8"@"NSData""ScalesF32"@"NSData""ZeroPointsU8"@"NSData""WeightZeroPointsRuntime"@"NSData""outputBlockK"S"nsimd_per_tg"S"nmatsHW"S"nmatsK"S"inputIsQuantized"B"inputIsSigned"B"WeightsFP16"@"NSData""BiasesFP16"@"NSData""outputToTexture"B"inputFromTexture"B"splitFakeQuantInput"B"splitQuantInput"B"WeightsFirst16FP16"@"NSData""WeightsLast16U8"@"NSData""useSigmoid"B"useD2S"B"useLeakyReLU"B"outZp"f"combinedInZp"f"bilinearImageZp"f"skipZpAct"f"blockMajorWeights"B"headTemporalTex"B"headRnnTex"B} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufWeightsFirst16;
@"<MTLBuffer>" _bufWeightsLast16;
@"<MTLBuffer>" _bufWeightZPRuntime;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufBias;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
{?="width"Q"height"Q"depth"Q} _bilinearThreadsPerGrid;
{?="width"Q"height"Q"depth"Q} _bilinearThreadsPerTG;
S _mxu_version;
S _nmatsHW;
S _nmatsK;
B _useScratchPath;
```

## Instance methods

```
-[Conv3x3Stride1 computeGridAndTGSize];
-[Conv3x3Stride1 createBuffers];
-[Conv3x3Stride1 dispatchWithEncoder:argTable:feed:skip:target:];
-[Conv3x3Stride1 dispatchWithEncoder:argTable:feed:skip:targetTexture:];
-[Conv3x3Stride1 dispatchWithEncoder:argTable:feed:target:temporalTex:rnnTex:];
-[Conv3x3Stride1 dispatchWithEncoder:argTable:feedTexture:skip:target:];
-[Conv3x3Stride1 dispatchWithEncoder:argTable:feedU8:feedF16:target:];
-[Conv3x3Stride1 executeWithCommandBuffer:feed:skip:target:];
-[Conv3x3Stride1 executeWithCommandBuffer:feed:skip:targetTexture:];
-[Conv3x3Stride1 executeWithCommandBuffer:feed:target:temporalTex:rnnTex:];
-[Conv3x3Stride1 executeWithCommandBuffer:feedTexture:skip:target:];
-[Conv3x3Stride1 executeWithCommandBuffer:feedU8:feedF16:target:];
-[Conv3x3Stride1 executeWithMTL4CommandBuffer:feed:skip:target:fence:];
-[Conv3x3Stride1 executeWithMTL4CommandBuffer:feed:skip:targetTexture:fence:];
-[Conv3x3Stride1 executeWithMTL4CommandBuffer:feedTexture:skip:target:fence:];
-[Conv3x3Stride1 initWithDescriptor:library:];
-[Conv3x3Stride1 internalAllocations];
-[Conv3x3Stride1 prepareImageTensorFeed:];
-[Conv3x3Stride1 setupMetalWithLibrary:];
```
