# `BKSMutableHIDEventPolicyObservation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventPolicyObservation`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (Ti,D,N) pid;
@property (T@"BKSHIDEventDisplay",&,D,N) display;
@property (T@"BKSHIDEventDeferringEnvironment",&,D,N) environment;
@property (T@"BKSHIDEventDeferringSelectionPathIdentifier",&,D,N) selectionPath;
@property (T@"BKSHIDEventDeferringToken",&,D,N) token;
@property (Tq,D,N) policyStatus;
@property (TB,D,N,GisFinalStringToken) finalStringToken;
@property (Tq,D,N) generation;
```

## Instance methods

```
-[BKSMutableHIDEventPolicyObservation setDisplay:];
-[BKSMutableHIDEventPolicyObservation setPid:];
-[BKSMutableHIDEventPolicyObservation setEnvironment:];
-[BKSMutableHIDEventPolicyObservation setGeneration:];
-[BKSMutableHIDEventPolicyObservation setFinalStringToken:];
-[BKSMutableHIDEventPolicyObservation setToken:];
-[BKSMutableHIDEventPolicyObservation copyWithZone:];
-[BKSMutableHIDEventPolicyObservation setPolicyStatus:];
-[BKSMutableHIDEventPolicyObservation setSelectionPath:];
```
