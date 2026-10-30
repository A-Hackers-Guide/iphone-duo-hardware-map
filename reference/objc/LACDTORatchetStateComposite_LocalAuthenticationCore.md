# `LACDTORatchetStateComposite`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"LACDTORatchetState" _ratchetState;
@"LACDTOGracePeriodState" _gracePeriodState;
@"LACDTOBiometryWatchdogPack" _watchdogs;
```

## Properties

```
@property (T@"LACDTORatchetState",R,N,V_ratchetState) ratchetState;
@property (T@"LACDTOGracePeriodState",R,N,V_gracePeriodState) gracePeriodState;
@property (T@"LACDTOBiometryWatchdogPack",R,N,V_watchdogs) watchdogs;
```

## Class methods

```
+[LACDTORatchetStateComposite supportsSecureCoding];
+[LACDTORatchetStateComposite nullInstance];
```

## Instance methods

```
-[LACDTORatchetStateComposite gracePeriodState];
-[LACDTORatchetStateComposite encodeWithCoder:];
-[LACDTORatchetStateComposite description];
-[LACDTORatchetStateComposite initWithCoder:];
-[LACDTORatchetStateComposite ratchetState];
-[LACDTORatchetStateComposite isEqual:];
-[LACDTORatchetStateComposite initWithRatchetState:gracePeriodState:watchdogs:];
-[LACDTORatchetStateComposite watchdogs];
```
