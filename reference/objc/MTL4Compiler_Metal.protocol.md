# `MTL4Compiler` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (T@"<MTL4PipelineDataSetSerializer>",R) pipelineDataSetSerializer;
```

## Instance methods

```
-[MTL4Compiler newLibraryWithDescriptor:completionHandler:];
-[MTL4Compiler newDynamicLibrary:error:];
-[MTL4Compiler newLibraryWithDescriptor:error:];
-[MTL4Compiler newDynamicLibraryWithURL:error:];
-[MTL4Compiler device];
-[MTL4Compiler label];
-[MTL4Compiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:];
-[MTL4Compiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4Compiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:];
-[MTL4Compiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4Compiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:];
-[MTL4Compiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4Compiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[MTL4Compiler newDynamicLibrary:completionHandler:];
-[MTL4Compiler newDynamicLibraryWithURL:completionHandler:];
-[MTL4Compiler newMachineLearningPipelineStateWithDescriptor:completionHandler:];
-[MTL4Compiler newMachineLearningPipelineStateWithDescriptor:error:];
-[MTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:];
-[MTL4Compiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:];
-[MTL4Compiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4Compiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4Compiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[MTL4Compiler pipelineDataSetSerializer];
```
