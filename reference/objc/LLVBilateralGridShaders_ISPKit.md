# `LLVBilateralGridShaders`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
[2@"<MTLComputePipelineState>"] _bgSplat;
[3@"<MTLComputePipelineState>"] _bgBlur;
@"<MTLComputePipelineState>" _bgNormalize;
@"<MTLRenderPipelineState>" _bgUpsample8;
@"<MTLRenderPipelineState>" _bgUpsample16;
@"<MTLRenderPipelineState>" _bgUpsample16ToneMapped;
@"<MTLComputePipelineState>" _bgBistochastizeInit;
@"<MTLComputePipelineState>" _bgBistochastizeIter;
@"<MTLComputePipelineState>" _bgBistochastizeFinal;
@"<MTLComputePipelineState>" _bgSolverInit1;
@"<MTLComputePipelineState>" _bgSolverInit2;
@"<MTLComputePipelineState>" _bgSolverPcgIter0;
@"<MTLComputePipelineState>" _bgSolverPcgIter1;
@"<MTLComputePipelineState>" _bgSolverPcgIter2;
@"<MTLComputePipelineState>" _bgSolverPcgIter3;
```

## Instance methods

```
-[LLVBilateralGridShaders createBasicComputeShader:metal:];
-[LLVBilateralGridShaders initWithMetal:normalizeGridConfidence:];
```
