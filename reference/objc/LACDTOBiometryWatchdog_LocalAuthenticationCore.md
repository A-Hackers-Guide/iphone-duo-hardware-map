# `LACDTOBiometryWatchdog`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
B _isRunning;
d _time;
d _threshold;
```

## Properties

```
@property (TB,R,N,V_isRunning) isRunning;
@property (Td,R,N,V_time) time;
@property (Td,R,N,V_threshold) threshold;
@property (TB,R,N) isBarking;
```

## Class methods

```
+[LACDTOBiometryWatchdog supportsSecureCoding];
+[LACDTOBiometryWatchdog nullInstance];
```

## Instance methods

```
-[LACDTOBiometryWatchdog isRunning];
-[LACDTOBiometryWatchdog threshold];
-[LACDTOBiometryWatchdog encodeWithCoder:];
-[LACDTOBiometryWatchdog description];
-[LACDTOBiometryWatchdog initWithCoder:];
-[LACDTOBiometryWatchdog isEqual:];
-[LACDTOBiometryWatchdog time];
-[LACDTOBiometryWatchdog initWithIsRunning:time:threshold:];
-[LACDTOBiometryWatchdog isBarking];
```
