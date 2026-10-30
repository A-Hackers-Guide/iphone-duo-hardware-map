# `MPSGraphExecutableReflection`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _mpsGraphPackageURL;
@"NSFileManager" _fileManager;
@"NSData" _reflectionFb;
```

## Instance methods

```
-[MPSGraphExecutableReflection functionNames];
-[MPSGraphExecutableReflection initWithMPSGraphPackage:error:];
-[MPSGraphExecutableReflection inputNamesForFunction:];
-[MPSGraphExecutableReflection inputShapesForFunction:];
-[MPSGraphExecutableReflection outputNamesForFunction:];
-[MPSGraphExecutableReflection outputShapesForFunction:];
-[MPSGraphExecutableReflection inputRanksForFunction:];
-[MPSGraphExecutableReflection outputRanksForFunction:];
```
