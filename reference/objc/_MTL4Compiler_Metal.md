# `_MTL4Compiler`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4CompilerGGDSPI`
- 6 instance variables, 9 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mlcompiler_queue;
@"NSObject<OS_dispatch_queue>" _debugQueue;
B _shouldMaximizeConcurrentCompilation;
@"<MTLBinaryArchive>" _destinationBinaryArchive;
@"<MTL4PipelineDataSetSerializer>" _pipelineDataSetSerializer;
@"<MTLDevice>" _device;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"<MTL4PipelineDataSetSerializer>",R,V_pipelineDataSetSerializer) pipelineDataSetSerializer;
@property (T@"<MTLBinaryArchive>",R,V_destinationBinaryArchive) destinationBinaryArchive;
@property (TB,R,V_shouldMaximizeConcurrentCompilation) shouldMaximizeConcurrentCompilation;
@property (T@"NSString",R) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4Compiler newLibraryWithDescriptor:completionHandler:];
-[_MTL4Compiler newDynamicLibrary:error:];
-[_MTL4Compiler newLibraryWithDescriptor:error:];
-[_MTL4Compiler newDynamicLibraryWithURL:options:error:];
-[_MTL4Compiler newDynamicLibraryWithURL:error:];
-[_MTL4Compiler initWithDevice:];
-[_MTL4Compiler initWithDevice:descriptor:];
-[_MTL4Compiler device];
-[_MTL4Compiler dealloc];
-[_MTL4Compiler cancel];
-[_MTL4Compiler destinationBinaryArchive];
-[_MTL4Compiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:];
-[_MTL4Compiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:];
-[_MTL4Compiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:];
-[_MTL4Compiler newBinaryFunctionWithDescriptor:functionType:compilerTaskOptions:completionHandler:];
-[_MTL4Compiler newBinaryFunctionWithDescriptor:functionType:compilerTaskOptions:error:];
-[_MTL4Compiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[_MTL4Compiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:];
-[_MTL4Compiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[_MTL4Compiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[_MTL4Compiler newDynamicLibrary:completionHandler:];
-[_MTL4Compiler newDynamicLibraryWithURL:completionHandler:];
-[_MTL4Compiler newDynamicLibraryWithURL:options:completionHandler:];
-[_MTL4Compiler newMachineLearningPipelineStateWithDescriptor:completionHandler:];
-[_MTL4Compiler newMachineLearningPipelineStateWithDescriptor:error:];
-[_MTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:];
-[_MTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:];
-[_MTL4Compiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[_MTL4Compiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[_MTL4Compiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[_MTL4Compiler pipelineDataSetSerializer];
-[_MTL4Compiler setPipelineDataSetSerializer:];
-[_MTL4Compiler shouldMaximizeConcurrentCompilation];
```
