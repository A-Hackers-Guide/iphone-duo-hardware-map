# `MTLRasterizationRateLayerDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 6 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T{?=QQQ},D,N) sampleCount;
@property (T{?=QQQ},R,D,N) maxSampleCount;
@property (T^f,R,D,N) horizontalSampleStorage;
@property (T^f,R,D,N) verticalSampleStorage;
@property (T@"MTLRasterizationRateSampleArray",R,D,N) horizontal;
@property (T@"MTLRasterizationRateSampleArray",R,D,N) vertical;
```

## Class methods

```
+[MTLRasterizationRateLayerDescriptor allocWithZone:];
```

## Instance methods

```
-[MTLRasterizationRateLayerDescriptor init];
-[MTLRasterizationRateLayerDescriptor copyWithZone:];
-[MTLRasterizationRateLayerDescriptor initWithSampleCount:];
-[MTLRasterizationRateLayerDescriptor initWithSampleCount:horizontal:vertical:];
```
