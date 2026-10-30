# `MTLPipelineLibrarySPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLPipelineLibrary`
- 0 instance variables, 7 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSArray",R) pipelineNames;
@property (TB) disableRunTimeCompilation;
@property (T@"<MTLPipelineCache>",R,N) pipelineCache;
@property (T@"<MTLPipelineCache>",R,N) functionCache;
@property (T@"NSArray",R) metallibPaths;
```

## Instance methods

```
-[MTLPipelineLibrarySPI device];
-[MTLPipelineLibrarySPI label];
-[MTLPipelineLibrarySPI setLabel:];
-[MTLPipelineLibrarySPI pipelineCache];
-[MTLPipelineLibrarySPI setDisableRunTimeCompilation:];
-[MTLPipelineLibrarySPI disableRunTimeCompilation];
-[MTLPipelineLibrarySPI functionCache];
-[MTLPipelineLibrarySPI metallibPaths];
-[MTLPipelineLibrarySPI newComputePipelineDescriptorWithName:error:];
-[MTLPipelineLibrarySPI newComputePipelineStateWithName:options:reflection:error:];
-[MTLPipelineLibrarySPI newRenderPipelineDescriptorWithName:error:];
-[MTLPipelineLibrarySPI newRenderPipelineStateWithName:options:reflection:error:];
-[MTLPipelineLibrarySPI pipelineNames];
```
