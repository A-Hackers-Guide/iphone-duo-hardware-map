# `CTSimDeactivationEvent`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _isRoaming;
B _isNetworkInitiated;
Q _sourceType;
@"NSString" _reasonCode;
@"NSString" _networkPlmn;
@"NSString" _rat;
q _timeOfEvent;
```

## Properties

```
@property (TQ,N,V_sourceType) sourceType;
@property (T@"NSString",&,N,V_reasonCode) reasonCode;
@property (T@"NSString",&,N,V_networkPlmn) networkPlmn;
@property (TB,N,V_isRoaming) isRoaming;
@property (TB,N,V_isNetworkInitiated) isNetworkInitiated;
@property (T@"NSString",&,N,V_rat) rat;
@property (Tq,N,V_timeOfEvent) timeOfEvent;
```

## Class methods

```
+[CTSimDeactivationEvent supportsSecureCoding];
```

## Instance methods

```
-[CTSimDeactivationEvent isRoaming];
-[CTSimDeactivationEvent sourceType];
-[CTSimDeactivationEvent rat];
-[CTSimDeactivationEvent setSourceType:];
-[CTSimDeactivationEvent encodeWithCoder:];
-[CTSimDeactivationEvent description];
-[CTSimDeactivationEvent initWithCoder:];
-[CTSimDeactivationEvent isEqual:];
-[CTSimDeactivationEvent isNetworkInitiated];
-[CTSimDeactivationEvent networkPlmn];
-[CTSimDeactivationEvent reasonCode];
-[CTSimDeactivationEvent setReasonCode:];
-[CTSimDeactivationEvent timeOfEvent];
-[CTSimDeactivationEvent setNetworkPlmn:];
-[CTSimDeactivationEvent setRat:];
-[CTSimDeactivationEvent setTimeOfEvent:];
-[CTSimDeactivationEvent setIsNetworkInitiated:];
-[CTSimDeactivationEvent setIsRoaming:];
```
