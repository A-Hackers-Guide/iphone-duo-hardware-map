# `_MTLPipelineLibrary`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLPipelineLibrarySPI`
- 4 instance variables, 11 properties, 13 instance methods, 0 class methods

## Instance variables

```
^v _pipelineLibraryData;
@"<MTLDevice>" _device;
@"NSArray" _pipelineNames;
B _disableRunTimeCompilation;
```

## Properties

```
@property (T@"NSString",C,D) label;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSArray",R,V_pipelineNames) pipelineNames;
@property (TB,V_disableRunTimeCompilation) disableRunTimeCompilation;
@property (T@"<MTLPipelineCache>",R,D,N) pipelineCache;
@property (T@"<MTLPipelineCache>",R,D,N) functionCache;
@property (T@"NSArray",R) metallibPaths;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLPipelineLibrary device];
-[_MTLPipelineLibrary dealloc];
-[_MTLPipelineLibrary pipelineCache];
-[_MTLPipelineLibrary setDisableRunTimeCompilation:];
-[_MTLPipelineLibrary disableRunTimeCompilation];
-[_MTLPipelineLibrary functionCache];
-[_MTLPipelineLibrary initWithDevice:pipelineLibraryData:];
-[_MTLPipelineLibrary metallibPaths];
-[_MTLPipelineLibrary newComputePipelineDescriptorWithName:error:];
-[_MTLPipelineLibrary newComputePipelineStateWithName:options:reflection:error:];
-[_MTLPipelineLibrary newRenderPipelineDescriptorWithName:error:];
-[_MTLPipelineLibrary newRenderPipelineStateWithName:options:reflection:error:];
-[_MTLPipelineLibrary pipelineNames];
```
