# `CAMOverlayTitleRange`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayDiscreteValueRange`, `NSSecureCoding`
- 1 instance variables, 11 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSArray" __titles;
```

## Properties

```
@property (T@"NSArray",R,C,N,V__titles) _titles;
@property (T@"CAMOverlayIndexedRange",R,N) indexedRange;
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
+[CAMOverlayTitleRange supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayTitleRange isFloatingPoint];
-[CAMOverlayTitleRange containsValue:];
-[CAMOverlayTitleRange valueAtIndex:];
-[CAMOverlayTitleRange valueType];
-[CAMOverlayTitleRange count];
-[CAMOverlayTitleRange encodeWithCoder:];
-[CAMOverlayTitleRange initWithCoder:];
-[CAMOverlayTitleRange isEqual:];
-[CAMOverlayTitleRange isDiscrete];
-[CAMOverlayTitleRange rangeType];
-[CAMOverlayTitleRange indexOfValue:];
-[CAMOverlayTitleRange isEqualToRange:];
-[CAMOverlayTitleRange initWithTitles:];
-[CAMOverlayTitleRange _titles];
-[CAMOverlayTitleRange indexedRange];
-[CAMOverlayTitleRange isValueExpectedType:];
```
