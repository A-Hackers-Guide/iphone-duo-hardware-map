# `LACBiomeDialogEvent`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSString" _dialogID;
@"NSString" _bundleID;
d _timeSinceUpdate;
@"NSArray" _mechanisms;
q _successfulMechanism;
@"NSArray" _failedMechanisms;
@"NSArray" _actions;
q _failingAction;
```

## Properties

```
@property (T@"NSString",&,N,V_dialogID) dialogID;
@property (T@"NSString",&,N,V_bundleID) bundleID;
@property (Td,R,N,V_timeSinceUpdate) timeSinceUpdate;
@property (T@"NSArray",R,N,V_mechanisms) mechanisms;
@property (Tq,R,N,V_successfulMechanism) successfulMechanism;
@property (T@"NSArray",R,N,V_failedMechanisms) failedMechanisms;
@property (T@"NSArray",R,N,V_actions) actions;
@property (Tq,R,N,V_failingAction) failingAction;
```

## Instance methods

```
-[LACBiomeDialogEvent init];
-[LACBiomeDialogEvent setBundleID:];
-[LACBiomeDialogEvent actions];
-[LACBiomeDialogEvent description];
-[LACBiomeDialogEvent bundleID];
-[LACBiomeDialogEvent timeSinceUpdate];
-[LACBiomeDialogEvent dialogID];
-[LACBiomeDialogEvent failedMechanisms];
-[LACBiomeDialogEvent failingAction];
-[LACBiomeDialogEvent mechanisms];
-[LACBiomeDialogEvent successfulMechanism];
-[LACBiomeDialogEvent addAction:failing:];
-[LACBiomeDialogEvent determineTimeSinceLastSystemUpdateWithCompletion:];
-[LACBiomeDialogEvent failedAuthenticationWithMechanism:];
-[LACBiomeDialogEvent mergeBiomeEvent:];
-[LACBiomeDialogEvent setDialogID:];
-[LACBiomeDialogEvent startedAuthenticationWithMechanism:];
-[LACBiomeDialogEvent succeededAuthenticationWithMechanism:];
```
