# `CAMOverlayValueRange` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
```

## Instance methods

```
-[CAMOverlayValueRange isFloatingPoint];
-[CAMOverlayValueRange containsValue:];
-[CAMOverlayValueRange valueType];
-[CAMOverlayValueRange isDiscrete];
-[CAMOverlayValueRange rangeType];
-[CAMOverlayValueRange isEqualToRange:];
-[CAMOverlayValueRange isValueExpectedType:];
```
