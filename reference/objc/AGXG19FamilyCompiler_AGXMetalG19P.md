# `AGXG19FamilyCompiler`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4Compiler`
- Protocols: `MTL4CompilerSPI`
- 5 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"AGXG19FamilyDevice" _device;
^v _dylib_factory;
^v _pipeline_factory;
^v _binary_function_factory;
@"AGXG19FamilyBinaryArchive" _harvesting_archive;
```

## Properties

```
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
-[AGXG19FamilyCompiler newDynamicLibrary:error:];
-[AGXG19FamilyCompiler initWithDevice:descriptor:];
-[AGXG19FamilyCompiler dealloc];
-[AGXG19FamilyCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:error:];
-[AGXG19FamilyCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:];
-[AGXG19FamilyCompiler newBinaryFunctionWithDescriptor:compilerTaskOptions:error:];
-[AGXG19FamilyCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[AGXG19FamilyCompiler newComputePipelineStateWithDescriptor:compilerTaskOptions:error:];
-[AGXG19FamilyCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[AGXG19FamilyCompiler newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
-[AGXG19FamilyCompiler newDynamicLibrary:completionHandler:];
-[AGXG19FamilyCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:completionHandler:];
-[AGXG19FamilyCompiler newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:];
-[AGXG19FamilyCompiler newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:];
-[AGXG19FamilyCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:];
-[AGXG19FamilyCompiler newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:];
```
