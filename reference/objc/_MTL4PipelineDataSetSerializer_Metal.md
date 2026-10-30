# `_MTL4PipelineDataSetSerializer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4PipelineDataSetSerializerGGDSPI`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<MTLBinaryArchive>" _destinationBinaryArchive;
@"<MTLDevice>" _device;
{unique_ptr<MTL4MetalScriptBuilder, std::default_delete<MTL4MetalScriptBuilder>>=""{?="__ptr_"^{MTL4MetalScriptBuilder}}} _mtl4ScriptBuilder;
Q _configuration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4PipelineDataSetSerializer initWithDevice:descriptor:];
-[_MTL4PipelineDataSetSerializer dealloc];
-[_MTL4PipelineDataSetSerializer destinationBinaryArchive];
-[_MTL4PipelineDataSetSerializer addBinaryFunctionWithDescriptor:];
-[_MTL4PipelineDataSetSerializer addPipelineWithDescriptor:];
-[_MTL4PipelineDataSetSerializer serializeAsArchiveAndFlushToURL:error:];
-[_MTL4PipelineDataSetSerializer serializeAsPipelinesScriptWithError:];
```
