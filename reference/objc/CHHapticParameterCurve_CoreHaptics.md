# `CHHapticParameterCurve`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _param;
d _time;
@"NSArray" _controlPoints;
```

## Properties

```
@property (T@"NSString",R,V_param) parameterID;
@property (Td,V_time) relativeTime;
@property (T@"NSArray",R) controlPoints;
```

## Instance methods

```
-[CHHapticParameterCurve init];
-[CHHapticParameterCurve setRelativeTime:];
-[CHHapticParameterCurve controlPoints];
-[CHHapticParameterCurve relativeTime];
-[CHHapticParameterCurve parameterID];
-[CHHapticParameterCurve initWithParameterID:controlPoints:relativeTime:];
```
