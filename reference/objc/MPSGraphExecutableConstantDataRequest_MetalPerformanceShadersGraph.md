# `MPSGraphExecutableConstantDataRequest`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _mpsgraphPackageURL;
@"NSDictionary" _resourceOffsets;
```

## Properties

```
@property (T@"NSURL",&,V_mpsgraphPackageURL) mpsgraphPackageURL;
@property (T@"NSDictionary",&,V_resourceOffsets) resourceOffsets;
```

## Class methods

```
+[MPSGraphExecutableConstantDataRequest supportsSecureCoding];
```

## Instance methods

```
-[MPSGraphExecutableConstantDataRequest encodeWithCoder:];
-[MPSGraphExecutableConstantDataRequest initWithCoder:];
-[MPSGraphExecutableConstantDataRequest resourceOffsets];
-[MPSGraphExecutableConstantDataRequest initForMPSGraphPackageAtURL:device:multipleInputTypes:compilationDescriptor:includeConstantDataForNewSpecializations:];
-[MPSGraphExecutableConstantDataRequest mpsgraphPackageURL];
-[MPSGraphExecutableConstantDataRequest setMpsgraphPackageURL:];
-[MPSGraphExecutableConstantDataRequest setResourceOffsets:];
```
