# `_MTL4Archive`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4ArchiveGGDSPI`
- 2 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
{unique_ptr<MTL4ArchiveImpl, std::default_delete<MTL4ArchiveImpl>>=""{?="__ptr_"^{MTL4ArchiveImpl}}} _archiveReader;
```

## Properties

```
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4Archive newComputePipelineStateWithDescriptor:error:];
-[_MTL4Archive newRenderPipelineStateWithDescriptor:error:];
-[_MTL4Archive initWithDevice:];
-[_MTL4Archive loadFromURL:error:];
-[_MTL4Archive newComputePipelineStateWithName:dynamicLinkingDescriptor:error:];
-[_MTL4Archive newArchiveArrayReplyForPipelineWithName:];
-[_MTL4Archive newArchiveReplyForBinaryFunctionWithDescriptor:];
-[_MTL4Archive newArchiveReplyForPipelineFunctionWithDescriptor:functionType:functionId:];
-[_MTL4Archive newBinaryFunctionWithDescriptor:error:];
-[_MTL4Archive newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:];
-[_MTL4Archive newComputePipelineStateWithName:error:];
-[_MTL4Archive newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:];
-[_MTL4Archive newRenderPipelineStateWithName:dynamicLinkingDescriptor:error:];
-[_MTL4Archive newRenderPipelineStateWithName:error:];
```
