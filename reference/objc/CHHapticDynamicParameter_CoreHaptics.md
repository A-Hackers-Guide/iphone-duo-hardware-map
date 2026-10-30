# `CHHapticDynamicParameter`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _param;
f _value;
d _time;
```

## Properties

```
@property (T@"NSString",R,V_param) parameterID;
@property (Tf,V_value) value;
@property (Td,V_time) relativeTime;
```

## Instance methods

```
-[CHHapticDynamicParameter init];
-[CHHapticDynamicParameter value];
-[CHHapticDynamicParameter setRelativeTime:];
-[CHHapticDynamicParameter setValue:];
-[CHHapticDynamicParameter relativeTime];
-[CHHapticDynamicParameter parameterID];
-[CHHapticDynamicParameter initWithParameterID:value:relativeTime:];
```
