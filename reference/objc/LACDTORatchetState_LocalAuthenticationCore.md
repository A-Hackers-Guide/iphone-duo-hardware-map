# `LACDTORatchetState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 5 properties, 10 instance methods, 2 class methods

## Instance variables

```
q _rawValue;
d _duration;
d _resetDuration;
@"NSString" _uuid;
```

## Properties

```
@property (Tq,R,N,V_rawValue) rawValue;
@property (Td,R,N,V_duration) duration;
@property (Td,R,N,V_resetDuration) resetDuration;
@property (Td,R,N) effectiveDuration;
@property (T@"NSString",R,N,V_uuid) uuid;
```

## Class methods

```
+[LACDTORatchetState supportsSecureCoding];
+[LACDTORatchetState nullInstance];
```

## Instance methods

```
-[LACDTORatchetState uuid];
-[LACDTORatchetState rawValue];
-[LACDTORatchetState effectiveDuration];
-[LACDTORatchetState duration];
-[LACDTORatchetState encodeWithCoder:];
-[LACDTORatchetState description];
-[LACDTORatchetState initWithCoder:];
-[LACDTORatchetState isEqual:];
-[LACDTORatchetState initWithRawValue:duration:resetDuration:uuid:];
-[LACDTORatchetState resetDuration];
```
