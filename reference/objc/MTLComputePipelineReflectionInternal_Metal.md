# `MTLComputePipelineReflectionInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLComputePipelineReflection`
- 9 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _arguments;
@"NSArray" _builtInArguments;
@"NSDictionary" _performanceStatistics;
{?="kernelRegisterSpill"b1"threadgroupBarrier"b1"deviceMemoryAtomics"b1"threadgroupMemoryAtomics"b1"kernelThreadInvariantRegisterSpill"b1"genericMemoryAtomics"b1"threadMemoryAtomics"b1"reserved"b57} _flags;
I _traceBufferIndex;
@"NSData" _pluginReturnData;
@"NSArray" _constantSamplerUniqueIdentifiers;
@"NSArray" _constantSamplerDescriptors;
@"NSArray" _bindings;
```

## Instance methods

```
-[MTLComputePipelineReflectionInternal arguments];
-[MTLComputePipelineReflectionInternal formattedDescription:];
-[MTLComputePipelineReflectionInternal dealloc];
-[MTLComputePipelineReflectionInternal description];
-[MTLComputePipelineReflectionInternal bindings];
-[MTLComputePipelineReflectionInternal usageFlags];
-[MTLComputePipelineReflectionInternal builtInArguments];
-[MTLComputePipelineReflectionInternal constantSamplerDescriptors];
-[MTLComputePipelineReflectionInternal constantSamplerUniqueIdentifiers];
-[MTLComputePipelineReflectionInternal initWithSerializedData:device:options:flags:];
-[MTLComputePipelineReflectionInternal initWithSerializedData:dynamicLibraries:serializedStageInputDescriptor:device:options:flags:];
-[MTLComputePipelineReflectionInternal initWithSerializedData:serializedStageInputDescriptor:device:options:flags:];
-[MTLComputePipelineReflectionInternal performanceStatistics];
-[MTLComputePipelineReflectionInternal pluginReturnData];
-[MTLComputePipelineReflectionInternal setConstantSamplerDescriptorsFromBitmasks:count:];
-[MTLComputePipelineReflectionInternal setConstantSamplerDescriptorsFromBitmasks:stride:count:];
-[MTLComputePipelineReflectionInternal setConstantSamplerUniqueIdentifiers:];
-[MTLComputePipelineReflectionInternal setPerformanceStatistics:];
-[MTLComputePipelineReflectionInternal traceBufferIndex];
```
