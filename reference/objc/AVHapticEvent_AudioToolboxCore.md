# `AVHapticEvent`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 9 properties, 15 instance methods, 7 class methods

## Instance variables

```
d _time;
d _duration;
Q _eventCategory;
(?="_eventType"Q"_paramType"Q) _u;
[8{AVHapticPlayerFixedParameter="type"Q"value"f}] _fixedParams;
@"AVHapticPlayerParameterCurve" _paramCurve;
q _fixedParamCount;
f _value;
```

## Properties

```
@property (Td,R,V_time) time;
@property (Td,R,V_duration) duration;
@property (TQ,R,V_eventCategory) eventCategory;
@property (TQ,R) eventType;
@property (TQ,R) paramType;
@property (Tf,R,V_value) value;
@property (T^{AVHapticPlayerFixedParameter=Qf},R) fixedParams;
@property (T@"AVHapticPlayerParameterCurve",R) parameterCurve;
@property (Tq,R,V_fixedParamCount) fixedParamCount;
```

## Class methods

```
+[AVHapticEvent supportsSecureCoding];
+[AVHapticEvent eventWithEventType:time:duration:];
+[AVHapticEvent eventWithParameterCurve:];
+[AVHapticEvent eventWithEventType:time:];
+[AVHapticEvent eventWithParameter:value:time:];
+[AVHapticEvent eventWithEventType:time:parameters:count:];
+[AVHapticEvent eventWithEventType:time:parameters:count:duration:];
```

## Instance methods

```
-[AVHapticEvent eventType];
-[AVHapticEvent paramType];
-[AVHapticEvent value];
-[AVHapticEvent fixedParamCount];
-[AVHapticEvent duration];
-[AVHapticEvent eventCategory];
-[AVHapticEvent initWithParameterCurve:];
-[AVHapticEvent initWithEventType:time:parameters:count:duration:];
-[AVHapticEvent encodeWithCoder:];
-[AVHapticEvent fixedParams];
-[AVHapticEvent parameterCurve];
-[AVHapticEvent initWithCoder:];
-[AVHapticEvent initWithParameter:value:time:];
-[AVHapticEvent initWithEventType:time:duration:];
-[AVHapticEvent time];
```
