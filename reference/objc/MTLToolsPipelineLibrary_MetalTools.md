# `MTLToolsPipelineLibrary`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLPipelineLibrarySPI`
- 0 instance variables, 11 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSArray",R) pipelineNames;
@property (TB) disableRunTimeCompilation;
@property (T@"<MTLPipelineCache>",R,N) pipelineCache;
@property (T@"<MTLPipelineCache>",R,N) functionCache;
@property (T@"NSArray",R) metallibPaths;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsPipelineLibrary device];
-[MTLToolsPipelineLibrary label];
-[MTLToolsPipelineLibrary setLabel:];
-[MTLToolsPipelineLibrary pipelineCache];
-[MTLToolsPipelineLibrary setDisableRunTimeCompilation:];
-[MTLToolsPipelineLibrary disableRunTimeCompilation];
-[MTLToolsPipelineLibrary functionCache];
-[MTLToolsPipelineLibrary metallibPaths];
-[MTLToolsPipelineLibrary newComputePipelineDescriptorWithName:error:];
-[MTLToolsPipelineLibrary newComputePipelineStateWithName:options:reflection:error:];
-[MTLToolsPipelineLibrary newRenderPipelineDescriptorWithName:error:];
-[MTLToolsPipelineLibrary newRenderPipelineStateWithName:options:reflection:error:];
-[MTLToolsPipelineLibrary pipelineNames];
```
