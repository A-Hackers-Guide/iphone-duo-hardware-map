# `Conv1x1FusedBilinear`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _convPSO;
@"<MTLComputePipelineState>" _convPSO_MTL4;
{Conv1x1FusedBilinearDescriptor="device"@"<MTLDevice>""NCONV"S"K""C""CSkip"S"Hin"S"Win"S"Hout"S"Wout"S"Weights"[4@"NSData"]"QsI"[4f]"QsRinv"[4f]"QsW"[4@"NSData"]"Biases"[4@"NSData"]"useBilinear"B"DqsBilinearImage"f"DqsBilinearSkip"f} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufBias;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
S _mxu_version;
```

## Instance methods

```
-[Conv1x1FusedBilinear SanityCheckKC];
-[Conv1x1FusedBilinear computeGridAndTGSize];
-[Conv1x1FusedBilinear createBuffers];
-[Conv1x1FusedBilinear dispatchWithEncoder:argTable:feed:skip:target:];
-[Conv1x1FusedBilinear executeWithCommandBuffer:feed:skip:target:];
-[Conv1x1FusedBilinear executeWithMTL4CommandBuffer:feed:skip:target:];
-[Conv1x1FusedBilinear initWithDescriptor:library:];
-[Conv1x1FusedBilinear internalAllocations];
-[Conv1x1FusedBilinear maxC];
-[Conv1x1FusedBilinear minK];
-[Conv1x1FusedBilinear setupMetalWithLibrary:];
```
