# `CAMOverlayDiscreteFloatRange`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayDiscreteValueRange`, `CAMOverlayFloatValueRange`, `NSSecureCoding`
- 5 instance variables, 13 properties, 25 instance methods, 1 class methods

## Instance variables

```
d _minimum;
d _maximum;
Q _count;
@"NSArray" __explicitStorage;
d __implicitStep;
```

## Properties

```
@property (T@"NSArray",R,C,N,V__explicitStorage) _explicitStorage;
@property (Td,R,N,V__implicitStep) _implicitStep;
@property (TQ,R,N,V_count) count;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N,V_minimum) minimum;
@property (Td,R,N,V_maximum) maximum;
```

## Class methods

```
+[CAMOverlayDiscreteFloatRange supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayDiscreteFloatRange initWithValues:];
-[CAMOverlayDiscreteFloatRange minimum];
-[CAMOverlayDiscreteFloatRange maximum];
-[CAMOverlayDiscreteFloatRange isFloatingPoint];
-[CAMOverlayDiscreteFloatRange containsValue:];
-[CAMOverlayDiscreteFloatRange valueAtIndex:];
-[CAMOverlayDiscreteFloatRange valueType];
-[CAMOverlayDiscreteFloatRange count];
-[CAMOverlayDiscreteFloatRange encodeWithCoder:];
-[CAMOverlayDiscreteFloatRange description];
-[CAMOverlayDiscreteFloatRange initWithCoder:];
-[CAMOverlayDiscreteFloatRange isEqual:];
-[CAMOverlayDiscreteFloatRange initWithMinimum:maximum:step:];
-[CAMOverlayDiscreteFloatRange isDiscrete];
-[CAMOverlayDiscreteFloatRange indexOfValueClosestToValue:];
-[CAMOverlayDiscreteFloatRange indexOfValueGreaterThanValue:];
-[CAMOverlayDiscreteFloatRange indexOfValueLessThanValue:];
-[CAMOverlayDiscreteFloatRange rangeType];
-[CAMOverlayDiscreteFloatRange indexOfValue:];
-[CAMOverlayDiscreteFloatRange isEqualToRange:];
-[CAMOverlayDiscreteFloatRange _explicitStorage];
-[CAMOverlayDiscreteFloatRange _implicitStep];
-[CAMOverlayDiscreteFloatRange indexesOfValuesInRange:];
-[CAMOverlayDiscreteFloatRange isValueExpectedType:];
-[CAMOverlayDiscreteFloatRange valueClosestToValue:];
```
