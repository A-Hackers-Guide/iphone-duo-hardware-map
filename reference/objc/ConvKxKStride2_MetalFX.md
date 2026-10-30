# `ConvKxKStride2`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _convPSO;
{ConvKxKStride2Descriptor="device"@"<MTLDevice>""K"S"C"S"Hout"S"Wout"S"KH"S"KW"S"pad"S"Weights"@"NSData""QsI"f"QsRinv"f"QsW"@"NSData""Biases"@"NSData""useUInt8"B"quantScheme"I"activation"I"useTEC"B"RefWeightsUInt8"@"NSData""ScalesF32"@"NSData""ZeroPointsU8"@"NSData""inputBlockK"S"useLeakyReLU"B"outZp"f"consumeRowSum"B"produceRowSum"B} _desc;
@"<MTLBuffer>" _bufWeights;
@"<MTLBuffer>" _bufQsW;
@"<MTLBuffer>" _bufBias;
@"<MTLBuffer>" _bufZP;
@"<MTLBuffer>" _bufRowSumOut;
{?="width"Q"height"Q"depth"Q} _threadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
S _mxu_version;
S _nsimdPerTG;
B _useRowSumIn;
B _produceRowSum;
B _isFP16;
B _is6x6;
B _use6x6Gemv;
S _kTile6x6;
```

## Instance methods

```
-[ConvKxKStride2 rowSumOutBuffer];
-[ConvKxKStride2 computeGrid6x6];
-[ConvKxKStride2 computeGridAndTGSize];
-[ConvKxKStride2 createBuffers];
-[ConvKxKStride2 dispatchWithEncoder:argTable:feed:rowSum:target:];
-[ConvKxKStride2 dispatchWithEncoder:argTable:feed:target:];
-[ConvKxKStride2 executeWithCommandBuffer:feed:rowSum:target:];
-[ConvKxKStride2 executeWithCommandBuffer:feed:target:];
-[ConvKxKStride2 executeWithMTL4CommandBuffer:feed:target:];
-[ConvKxKStride2 executeWithMTL4CommandBuffer:feed:target:fence:];
-[ConvKxKStride2 initWithDescriptor:library:];
-[ConvKxKStride2 internalAllocations];
-[ConvKxKStride2 mxu3ConvUses4DImageTensor];
-[ConvKxKStride2 schemeHasZeroPoint];
-[ConvKxKStride2 setupMetalWithLibrary:];
```
