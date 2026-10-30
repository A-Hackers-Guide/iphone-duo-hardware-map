# `MTLRenderPipelineReflectionInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLRenderPipelineReflection`
- 27 instance variables, 0 properties, 38 instance methods, 0 class methods

## Instance variables

```
{?="fragmentUsesDiscard"b1"fragmentWritesSampleMask"b1"fragmentWritesDepth"b1"vertexRegisterSpill"b1"fragmentRegisterSpill"b1"fragmentReadsFramebufferValues"b1"fragmentPunchThrough"b1"vertexWritesPointSize"b1"private2"b1"vertexThreadInvariantRegisterSpill"b1"fragmentThreadInvariantRegisterSpill"b1"reserved"b53} _flags;
@"NSArray" _vertexBuiltInArguments;
Q _postVertexDumpStride;
@"NSArray" _postVertexDumpOutputs;
@"NSArray" _vertexArguments;
@"NSArray" _fragmentArguments;
@"NSArray" _tileArguments;
@"NSArray" _tileBuiltInArguments;
@"<MTLBinding>" _imageBlockDataReturn;
@"NSDictionary" _performanceStatistics;
I _traceBufferIndex;
@"NSData" _vertexPluginReturnData;
@"NSData" _fragmentPluginReturnData;
@"NSArray" _constantSamplerUniqueIdentifiers;
@"NSArray" _constantSamplerDescriptors;
@"NSArray" _objectArguments;
@"NSArray" _meshArguments;
@"NSArray" _objectBuiltInArguments;
@"NSArray" _meshBuiltInArguments;
@"NSData" _objectPluginReturnData;
@"NSData" _meshPluginReturnData;
@"NSArray" _vertexBindings;
@"NSArray" _fragmentBindings;
@"NSArray" _tileBindings;
@"NSArray" _objectBindings;
@"NSArray" _meshBindings;
Q _printStyle;
```

## Instance methods

```
-[MTLRenderPipelineReflectionInternal formattedDescription:];
-[MTLRenderPipelineReflectionInternal dealloc];
-[MTLRenderPipelineReflectionInternal description];
-[MTLRenderPipelineReflectionInternal usageFlags];
-[MTLRenderPipelineReflectionInternal objectArguments];
-[MTLRenderPipelineReflectionInternal vertexArguments];
-[MTLRenderPipelineReflectionInternal constantSamplerDescriptors];
-[MTLRenderPipelineReflectionInternal constantSamplerUniqueIdentifiers];
-[MTLRenderPipelineReflectionInternal fragmentArguments];
-[MTLRenderPipelineReflectionInternal fragmentBindings];
-[MTLRenderPipelineReflectionInternal fragmentPluginReturnData];
-[MTLRenderPipelineReflectionInternal imageBlockDataReturn];
-[MTLRenderPipelineReflectionInternal initWithObjectData:meshData:fragmentData:device:options:flags:];
-[MTLRenderPipelineReflectionInternal initWithObjectData:objectDynamicLibraries:meshData:meshDynamicLibraries:fragmentData:fragmentDynamicLibraries:device:options:flags:];
-[MTLRenderPipelineReflectionInternal initWithTileData:functionType:device:options:flags:];
-[MTLRenderPipelineReflectionInternal initWithTileData:tileDynamicLibraries:functionType:device:options:flags:];
-[MTLRenderPipelineReflectionInternal initWithVertexData:fragmentData:serializedVertexDescriptor:device:options:flags:];
-[MTLRenderPipelineReflectionInternal initWithVertexData:vertexDynamicLibraries:fragmentData:fragmentDynamicLibraries:serializedVertexDescriptor:device:options:flags:];
-[MTLRenderPipelineReflectionInternal meshArguments];
-[MTLRenderPipelineReflectionInternal meshBindings];
-[MTLRenderPipelineReflectionInternal meshBuiltInArguments];
-[MTLRenderPipelineReflectionInternal meshPluginReturnData];
-[MTLRenderPipelineReflectionInternal objectBindings];
-[MTLRenderPipelineReflectionInternal objectBuiltInArguments];
-[MTLRenderPipelineReflectionInternal objectPluginReturnData];
-[MTLRenderPipelineReflectionInternal performanceStatistics];
-[MTLRenderPipelineReflectionInternal postVertexDumpOutputs];
-[MTLRenderPipelineReflectionInternal postVertexDumpStride];
-[MTLRenderPipelineReflectionInternal setConstantSamplerDescriptorsFromBitmasks:count:];
-[MTLRenderPipelineReflectionInternal setConstantSamplerDescriptorsFromBitmasks:stride:count:];
-[MTLRenderPipelineReflectionInternal setConstantSamplerUniqueIdentifiers:];
-[MTLRenderPipelineReflectionInternal setPerformanceStatistics:];
-[MTLRenderPipelineReflectionInternal tileArguments];
-[MTLRenderPipelineReflectionInternal tileBindings];
-[MTLRenderPipelineReflectionInternal traceBufferIndex];
-[MTLRenderPipelineReflectionInternal vertexBindings];
-[MTLRenderPipelineReflectionInternal vertexBuiltInArguments];
-[MTLRenderPipelineReflectionInternal vertexPluginReturnData];
```
