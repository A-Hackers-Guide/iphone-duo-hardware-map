# `MPSGraphPackageMLIRLibrary`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 1 instance variables, 0 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _mlirLibrary;
```

## Instance methods

```
-[MPSGraphPackageMLIRLibrary init];
-[MPSGraphPackageMLIRLibrary setCallables:];
-[MPSGraphPackageMLIRLibrary getDict];
-[MPSGraphPackageMLIRLibrary addAdaptersByRank:];
-[MPSGraphPackageMLIRLibrary addDataFileNames:];
-[MPSGraphPackageMLIRLibrary addGpuAdapterPresent:];
-[MPSGraphPackageMLIRLibrary addOptimizedNoDeviceResourcesUsed:withSignature:];
-[MPSGraphPackageMLIRLibrary addOptimizedResourcesUsed:withSignature:];
-[MPSGraphPackageMLIRLibrary addOriginalMLIRFile:];
-[MPSGraphPackageMLIRLibrary addOriginalResourcesUsed:];
-[MPSGraphPackageMLIRLibrary addRDFFMap:];
-[MPSGraphPackageMLIRLibrary getANERegionsSHADict];
-[MPSGraphPackageMLIRLibrary getAdaptersByRank];
-[MPSGraphPackageMLIRLibrary getBinaryResourceFiles];
-[MPSGraphPackageMLIRLibrary getCallablesDescriptor];
-[MPSGraphPackageMLIRLibrary getOptimizedModules];
-[MPSGraphPackageMLIRLibrary getOptimizedNoDeviceModules];
-[MPSGraphPackageMLIRLibrary getOptimizedNoDeviceResourcesUsedLibrary];
-[MPSGraphPackageMLIRLibrary getOptimizedResourcesUsedLibrary];
-[MPSGraphPackageMLIRLibrary getOriginalResourcesUsed];
-[MPSGraphPackageMLIRLibrary getResourceOffsetsLibrary];
-[MPSGraphPackageMLIRLibrary getResourceStorageMode];
-[MPSGraphPackageMLIRLibrary initWithMLIRLibraryDict:];
-[MPSGraphPackageMLIRLibrary optimizedModuleWithSignature:];
-[MPSGraphPackageMLIRLibrary optimizedNoDeviceModuleWithSignature:];
-[MPSGraphPackageMLIRLibrary originalModuleExists];
-[MPSGraphPackageMLIRLibrary originalModuleSerialized];
-[MPSGraphPackageMLIRLibrary setANERegionsSHADict:];
-[MPSGraphPackageMLIRLibrary setOptimizedModule:withSignature:];
-[MPSGraphPackageMLIRLibrary setOptimizedNoDeviceModule:withSignature:];
-[MPSGraphPackageMLIRLibrary setOriginalModuleSerialized:];
-[MPSGraphPackageMLIRLibrary setResourceStorageMode:];
-[MPSGraphPackageMLIRLibrary updateWithMLIRLibrary:];
```
