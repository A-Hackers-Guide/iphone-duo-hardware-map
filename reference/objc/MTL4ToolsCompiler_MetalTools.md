# `MTL4ToolsCompiler`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4CompilerGGDSPI`
- 0 instance variables, 9 properties, 30 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLBinaryArchive>",R) destinationBinaryArchive;
@property (TB,R) shouldMaximizeConcurrentCompilation;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (T@"<MTL4PipelineDataSetSerializer>",R) pipelineDataSetSerializer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsCompiler newLibraryWithDescriptor:completionHandler:];
-[MTL4ToolsCompiler newDynamicLibrary:error:];
-[MTL4ToolsCompiler newLibraryWithDescriptor:error:];
-[MTL4ToolsCompiler newDynamicLibraryWithURL:options:error:];
-[MTL4ToolsCompiler newDynamicLibraryWithURL:error:];
-[MTL4ToolsCompiler label];
-[MTL4ToolsCompiler setLabel:];
-[MTL4ToolsCompiler cancel];
-[MTL4ToolsCompiler destinationBinaryArchive];
-[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:];
-[MTL4ToolsCompiler initWithBaseObject:parent:];
-[MTL4ToolsCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4ToolsCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:];
-[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:];
-[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4ToolsCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[MTL4ToolsCompiler newDynamicLibrary:completionHandler:];
-[MTL4ToolsCompiler newDynamicLibraryWithURL:completionHandler:];
-[MTL4ToolsCompiler newDynamicLibraryWithURL:options:completionHandler:];
-[MTL4ToolsCompiler newMachineLearningPipelineStateWithDescriptor:completionHandler:];
-[MTL4ToolsCompiler newMachineLearningPipelineStateWithDescriptor:error:];
-[MTL4ToolsCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:];
-[MTL4ToolsCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:];
-[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[MTL4ToolsCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[MTL4ToolsCompiler pipelineDataSetSerializer];
-[MTL4ToolsCompiler setPipelineDataSetSerializer:];
-[MTL4ToolsCompiler shouldMaximizeConcurrentCompilation];
```
