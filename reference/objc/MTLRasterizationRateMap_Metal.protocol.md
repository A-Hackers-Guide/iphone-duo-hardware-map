# `MTLRasterizationRateMap` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (T{?=QQQ},R) screenSize;
@property (T{?=QQQ},R) physicalGranularity;
@property (TQ,R) layerCount;
@property (T{?=QQ},R) parameterBufferSizeAndAlign;
```

## Instance methods

```
-[MTLRasterizationRateMap screenSize];
-[MTLRasterizationRateMap device];
-[MTLRasterizationRateMap label];
-[MTLRasterizationRateMap layerCount];
-[MTLRasterizationRateMap copyParameterDataToBuffer:offset:];
-[MTLRasterizationRateMap mapPhysicalToScreenCoordinates:forLayer:];
-[MTLRasterizationRateMap mapScreenToPhysicalCoordinates:forLayer:];
-[MTLRasterizationRateMap parameterBufferSizeAndAlign];
-[MTLRasterizationRateMap physicalGranularity];
-[MTLRasterizationRateMap physicalSizeForLayer:];
```
