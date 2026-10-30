# `_MTLRasterizationRateMap`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLRasterizationRateMapSPI`
- 5 instance variables, 12 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"NSString" _label;
{?="width"Q"height"Q"depth"Q} _dim;
Q _mutability;
f _minFactor;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (T{?=QQQ},R) screenSize;
@property (TQ,R) layerCount;
@property (T{?=QQQ},R) physicalGranularity;
@property (TQ,R,N) mutability;
@property (Tf,R,N) minFactor;
@property (T{?=QQ},R) parameterBufferSizeAndAlign;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLRasterizationRateMap screenSize];
-[_MTLRasterizationRateMap initWithDevice:descriptor:];
-[_MTLRasterizationRateMap formattedDescription:];
-[_MTLRasterizationRateMap device];
-[_MTLRasterizationRateMap init];
-[_MTLRasterizationRateMap label];
-[_MTLRasterizationRateMap dealloc];
-[_MTLRasterizationRateMap description];
-[_MTLRasterizationRateMap layerCount];
-[_MTLRasterizationRateMap copyParameterDataToBuffer:atOffset:];
-[_MTLRasterizationRateMap copyParameterDataToBuffer:offset:];
-[_MTLRasterizationRateMap mapPhysicalToScreenCoordinates:forLayer:];
-[_MTLRasterizationRateMap mapScreenToPhysicalCoordinates:forLayer:];
-[_MTLRasterizationRateMap minFactor];
-[_MTLRasterizationRateMap mutability];
-[_MTLRasterizationRateMap parameterBufferSizeAndAlign];
-[_MTLRasterizationRateMap physicalCoordinate:forLayer:];
-[_MTLRasterizationRateMap physicalGranularity];
-[_MTLRasterizationRateMap physicalSizeForLayer:];
-[_MTLRasterizationRateMap resetUsingDescriptor:];
-[_MTLRasterizationRateMap screenCoordinate:forLayer:];
```
