# `SBBRNet_MLP`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _pso;
{SBBRNet_MLP_Descriptor="device"@"<MTLDevice>""Hs"S"Ws"S"Weights"@"NSData""WeightsFP16"@"NSData""Biases"@"NSData""BiasesFP16"@"NSData""WeightScales"@"NSData""WeightZP"@"NSData""NmatsHW"S"nsimd_per_tg"S"inputIsFP16"B"inputIsNCHW"B"outputIsFP16"B"outputIsNCHW"B"fp16Intermediate"B} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufWeightsFP16;
@"<MTLBuffer>" _bufBias;
@"<MTLBuffer>" _bufBiasFP16;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufWeightZP;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
```

## Instance methods

```
-[SBBRNet_MLP computeGridAndTGSize];
-[SBBRNet_MLP createBuffers];
-[SBBRNet_MLP executeWithCommandBuffer:feed:target:];
-[SBBRNet_MLP executeWithMTL4CommandBuffer:feed:target:fence:];
-[SBBRNet_MLP initWithDescriptor:library:];
-[SBBRNet_MLP internalAllocations];
-[SBBRNet_MLP setupMetalWithLibrary:];
```
