# `CAMOverlayIndexedRange`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayDiscreteValueRange`, `NSSecureCoding`
- 2 instance variables, 10 properties, 16 instance methods, 1 class methods

## Instance variables

```
Q _count;
@"NSArray" __titles;
```

## Properties

```
@property (T@"NSArray",R,C,N,V__titles) _titles;
@property (TQ,R,N,V_count) count;
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
+[CAMOverlayIndexedRange supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayIndexedRange isFloatingPoint];
-[CAMOverlayIndexedRange containsValue:];
-[CAMOverlayIndexedRange valueAtIndex:];
-[CAMOverlayIndexedRange valueType];
-[CAMOverlayIndexedRange count];
-[CAMOverlayIndexedRange initWithCount:];
-[CAMOverlayIndexedRange encodeWithCoder:];
-[CAMOverlayIndexedRange description];
-[CAMOverlayIndexedRange initWithCoder:];
-[CAMOverlayIndexedRange isEqual:];
-[CAMOverlayIndexedRange isDiscrete];
-[CAMOverlayIndexedRange rangeType];
-[CAMOverlayIndexedRange indexOfValue:];
-[CAMOverlayIndexedRange isEqualToRange:];
-[CAMOverlayIndexedRange _titles];
-[CAMOverlayIndexedRange isValueExpectedType:];
```
