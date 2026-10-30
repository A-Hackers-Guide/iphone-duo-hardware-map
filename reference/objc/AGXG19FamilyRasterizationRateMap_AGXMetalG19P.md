# `AGXG19FamilyRasterizationRateMap`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLRasterizationRateMap`
- 1 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T{?=QQQ},R) screenSize;
@property (T{?=QQQ},R) physicalGranularity;
@property (TQ,R) layerCount;
@property (T{?=QQ},R) parameterBufferSizeAndAlign;
```

## Instance methods

```
-[AGXG19FamilyRasterizationRateMap screenSize];
-[AGXG19FamilyRasterizationRateMap initWithDevice:descriptor:];
-[AGXG19FamilyRasterizationRateMap device];
-[AGXG19FamilyRasterizationRateMap dealloc];
-[AGXG19FamilyRasterizationRateMap layerCount];
-[AGXG19FamilyRasterizationRateMap copyParameterDataToBuffer:atOffset:];
-[AGXG19FamilyRasterizationRateMap parameterBufferSizeAndAlign];
-[AGXG19FamilyRasterizationRateMap physicalCoordinate:forLayer:];
-[AGXG19FamilyRasterizationRateMap physicalGranularity];
-[AGXG19FamilyRasterizationRateMap physicalSizeForLayer:];
-[AGXG19FamilyRasterizationRateMap resetUsingDescriptor:];
-[AGXG19FamilyRasterizationRateMap screenCoordinate:forLayer:];
-[AGXG19FamilyRasterizationRateMap getImpl];
```
