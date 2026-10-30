# `MPSGraphNDXAdapterCache`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 3 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _adapterURLToRuntimeMap;
@"NSURL" _latestLoadedAdapterURL;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _lock;
```

## Instance methods

```
-[MPSGraphNDXAdapterCache init];
-[MPSGraphNDXAdapterCache dealloc];
-[MPSGraphNDXAdapterCache collectAdaptedModels:];
-[MPSGraphNDXAdapterCache createANEModelInstanceParametersForAdapterURL:entryPointANEProcedures:error:];
-[MPSGraphNDXAdapterCache getRDFFMapFromAdapterURL:];
-[MPSGraphNDXAdapterCache ndxRuntimeForAdapterURL:entryPointANEProcedures:creationBlock:error:];
```
