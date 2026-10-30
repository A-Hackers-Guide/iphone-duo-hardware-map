# `CAMOverlayBooleanRange`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayDiscreteValueRange`
- 0 instance variables, 9 properties, 11 instance methods, 1 class methods

## Properties

```
@property (TQ,R,N) count;
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
+[CAMOverlayBooleanRange _values];
```

## Instance methods

```
-[CAMOverlayBooleanRange isFloatingPoint];
-[CAMOverlayBooleanRange containsValue:];
-[CAMOverlayBooleanRange valueAtIndex:];
-[CAMOverlayBooleanRange valueType];
-[CAMOverlayBooleanRange count];
-[CAMOverlayBooleanRange description];
-[CAMOverlayBooleanRange isDiscrete];
-[CAMOverlayBooleanRange rangeType];
-[CAMOverlayBooleanRange indexOfValue:];
-[CAMOverlayBooleanRange isEqualToRange:];
-[CAMOverlayBooleanRange isValueExpectedType:];
```
