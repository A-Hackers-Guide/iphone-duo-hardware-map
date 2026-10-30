# `MPSGraphExecutableConstantData`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _mpsgraphPackageURL;
@"NSDictionary" _ioSurfaces;
```

## Properties

```
@property (T@"NSURL",&,V_mpsgraphPackageURL) mpsgraphPackageURL;
@property (T@"NSDictionary",&,V_ioSurfaces) ioSurfaces;
```

## Class methods

```
+[MPSGraphExecutableConstantData supportsSecureCoding];
```

## Instance methods

```
-[MPSGraphExecutableConstantData loadResources:];
-[MPSGraphExecutableConstantData encodeWithCoder:];
-[MPSGraphExecutableConstantData initWithCoder:];
-[MPSGraphExecutableConstantData initForRequest:];
-[MPSGraphExecutableConstantData extendWithRequest:];
-[MPSGraphExecutableConstantData ioSurfaces];
-[MPSGraphExecutableConstantData loadIntoResourceManager:];
-[MPSGraphExecutableConstantData mpsgraphPackageURL];
-[MPSGraphExecutableConstantData setIoSurfaces:];
-[MPSGraphExecutableConstantData setMpsgraphPackageURL:];
```
