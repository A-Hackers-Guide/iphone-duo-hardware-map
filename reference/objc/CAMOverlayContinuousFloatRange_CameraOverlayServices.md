# `CAMOverlayContinuousFloatRange`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayFloatValueRange`, `NSSecureCoding`
- 2 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
d _minimum;
d _maximum;
```

## Properties

```
@property (Td,R,N,V_minimum) minimum;
@property (Td,R,N,V_maximum) maximum;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMOverlayContinuousFloatRange supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayContinuousFloatRange minimum];
-[CAMOverlayContinuousFloatRange maximum];
-[CAMOverlayContinuousFloatRange isFloatingPoint];
-[CAMOverlayContinuousFloatRange containsValue:];
-[CAMOverlayContinuousFloatRange valueType];
-[CAMOverlayContinuousFloatRange encodeWithCoder:];
-[CAMOverlayContinuousFloatRange description];
-[CAMOverlayContinuousFloatRange initWithCoder:];
-[CAMOverlayContinuousFloatRange isEqual:];
-[CAMOverlayContinuousFloatRange initWithMinimum:maximum:];
-[CAMOverlayContinuousFloatRange isDiscrete];
-[CAMOverlayContinuousFloatRange rangeType];
-[CAMOverlayContinuousFloatRange isEqualToRange:];
-[CAMOverlayContinuousFloatRange isValueExpectedType:];
-[CAMOverlayContinuousFloatRange valueClosestToValue:];
```
