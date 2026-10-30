# `SBAppRepairTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransaction`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _appInfos;
@"NSMutableSet" _repairRequests;
@"STTelephonyStatusDomain" _telephonyDomain;
```

## Properties

```
@property (T@"NSSet",R,C,N,V_appInfos) appInfos;
```

## Instance methods

```
-[SBAppRepairTransaction _canBeInterrupted];
-[SBAppRepairTransaction _didComplete];
-[SBAppRepairTransaction _begin];
-[SBAppRepairTransaction dealloc];
-[SBAppRepairTransaction _evaluateCompletion];
-[SBAppRepairTransaction appInfos];
-[SBAppRepairTransaction _completeRequest:success:error:];
-[SBAppRepairTransaction _startAppRepairs];
-[SBAppRepairTransaction initWithApplicationInfos:];
```
