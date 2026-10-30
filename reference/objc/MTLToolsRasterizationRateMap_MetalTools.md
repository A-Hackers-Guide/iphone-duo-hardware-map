# `MTLToolsRasterizationRateMap`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLRasterizationRateMapSPI`
- 0 instance variables, 12 properties, 14 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) mutability;
@property (Tf,R,N) minFactor;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (T{?=QQQ},R) screenSize;
@property (T{?=QQQ},R) physicalGranularity;
@property (TQ,R) layerCount;
@property (T{?=QQ},R) parameterBufferSizeAndAlign;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsRasterizationRateMap screenSize];
-[MTLToolsRasterizationRateMap formattedDescription:];
-[MTLToolsRasterizationRateMap device];
-[MTLToolsRasterizationRateMap label];
-[MTLToolsRasterizationRateMap layerCount];
-[MTLToolsRasterizationRateMap copyParameterDataToBuffer:offset:];
-[MTLToolsRasterizationRateMap mapPhysicalToScreenCoordinates:forLayer:];
-[MTLToolsRasterizationRateMap mapScreenToPhysicalCoordinates:forLayer:];
-[MTLToolsRasterizationRateMap minFactor];
-[MTLToolsRasterizationRateMap mutability];
-[MTLToolsRasterizationRateMap parameterBufferSizeAndAlign];
-[MTLToolsRasterizationRateMap physicalGranularity];
-[MTLToolsRasterizationRateMap physicalSizeForLayer:];
-[MTLToolsRasterizationRateMap resetUsingDescriptor:];
```
