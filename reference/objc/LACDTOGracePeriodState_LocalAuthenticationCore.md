# `LACDTOGracePeriodState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 5 properties, 11 instance methods, 3 class methods

## Instance variables

```
B _allowsUI;
d _time;
d _maxThreshold;
```

## Properties

```
@property (Td,R,N,V_time) time;
@property (Td,R,N,V_maxThreshold) maxThreshold;
@property (TB,R,N) isActive;
@property (TB,R,N,V_allowsUI) allowsUI;
@property (Td,R,N) duration;
```

## Class methods

```
+[LACDTOGracePeriodState supportsSecureCoding];
+[LACDTOGracePeriodState nullInstance];
+[LACDTOGracePeriodState unlimitedGracePeriod];
```

## Instance methods

```
-[LACDTOGracePeriodState duration];
-[LACDTOGracePeriodState encodeWithCoder:];
-[LACDTOGracePeriodState description];
-[LACDTOGracePeriodState initWithCoder:];
-[LACDTOGracePeriodState isActive];
-[LACDTOGracePeriodState isEqual:];
-[LACDTOGracePeriodState time];
-[LACDTOGracePeriodState allowsUI];
-[LACDTOGracePeriodState initWithTime:maxThreshold:];
-[LACDTOGracePeriodState initWithTime:maxThreshold:allowsUI:];
-[LACDTOGracePeriodState maxThreshold];
```
