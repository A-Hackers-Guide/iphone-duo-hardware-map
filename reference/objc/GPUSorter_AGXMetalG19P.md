# `GPUSorter`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<GPUSorterImpl, std::default_delete<GPUSorterImpl>>=""{?="__ptr_"^{GPUSorterImpl}}} _impl;
I _debugDispatchCount;
B _gpuAsserts;
B _starvationFreeAvailable;
@"AccelerationStructureShaderCache" _shaderCache;
```

## Properties

```
@property (T@"AccelerationStructureShaderCache",&,N,V_shaderCache) shaderCache;
@property (TB,N,V_gpuAsserts) gpuAsserts;
@property (TB,N,V_starvationFreeAvailable) starvationFreeAvailable;
```

## Instance methods

```
-[GPUSorter cppImpl];
-[GPUSorter setShaderCache:];
-[GPUSorter encodeToEncoder:keys:count:keyType:scratch:algorithm:error:];
-[GPUSorter encodeToEncoder:keys:upperBoundCount:indirectCount:keyType:scratch:algorithm:error:];
-[GPUSorter encodeToEncoder:pairsKeys:values:count:keyType:payloadType:scratch:algorithm:error:];
-[GPUSorter encodeToEncoder:pairsKeys:values:upperBoundCount:indirectCount:keyType:payloadType:scratch:algorithm:error:];
-[GPUSorter encodeToEncoder:pairsKeys:values:upperBoundCount:indirectCount:keyType:payloadType:scratch:algorithm:numBits:error:];
-[GPUSorter gpuAsserts];
-[GPUSorter initWithDevice:shaderCache:error:];
-[GPUSorter scratchBufferSizeForCount:keyType:payloadType:algorithm:];
-[GPUSorter setGpuAsserts:];
-[GPUSorter setStarvationFreeAvailable:];
-[GPUSorter setupDebugBuffer:];
-[GPUSorter shaderCache];
-[GPUSorter starvationFreeAvailable];
```
