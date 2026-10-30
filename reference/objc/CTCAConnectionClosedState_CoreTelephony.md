# `CTCAConnectionClosedState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _reason;
@"NSDate" _closedAt;
Q _wasActiveServices;
```

## Properties

```
@property (Tq,N,V_reason) reason;
@property (T@"NSDate",&,N,V_closedAt) closedAt;
@property (TQ,N,V_wasActiveServices) wasActiveServices;
```

## Class methods

```
+[CTCAConnectionClosedState supportsSecureCoding];
```

## Instance methods

```
-[CTCAConnectionClosedState setReason:];
-[CTCAConnectionClosedState encodeWithCoder:];
-[CTCAConnectionClosedState description];
-[CTCAConnectionClosedState initWithCoder:];
-[CTCAConnectionClosedState reason];
-[CTCAConnectionClosedState copyWithZone:];
-[CTCAConnectionClosedState closedAt];
-[CTCAConnectionClosedState setClosedAt:];
-[CTCAConnectionClosedState setWasActiveServices:];
-[CTCAConnectionClosedState wasActiveServices];
```
