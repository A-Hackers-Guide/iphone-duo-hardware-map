# `AVHapticPlayerParameterCurve`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _type;
d _time;
Q _shape;
@"NSArray" _controlPoints;
```

## Properties

```
@property (TQ,V_type) type;
@property (Td,V_time) time;
@property (TQ,V_shape) shape;
@property (T@"NSArray",R) controlPoints;
```

## Class methods

```
+[AVHapticPlayerParameterCurve supportsSecureCoding];
```

## Instance methods

```
-[AVHapticPlayerParameterCurve setShape:];
-[AVHapticPlayerParameterCurve shape];
-[AVHapticPlayerParameterCurve init];
-[AVHapticPlayerParameterCurve setType:];
-[AVHapticPlayerParameterCurve controlPoints];
-[AVHapticPlayerParameterCurve type];
-[AVHapticPlayerParameterCurve encodeWithCoder:];
-[AVHapticPlayerParameterCurve initWithCoder:];
-[AVHapticPlayerParameterCurve setTime:];
-[AVHapticPlayerParameterCurve time];
-[AVHapticPlayerParameterCurve initWithType:relativeTime:shape:controlPoints:];
```
