# `CTCellularData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{network_usage_policy_client_s=} _cuPolicyClient;
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _cuPolicyClientQueue;
Q _restrictedState;
@? _cellularDataRestrictionDidUpdateNotifier;
```

## Properties

```
@property (T@?,C,V_cellularDataRestrictionDidUpdateNotifier) cellularDataRestrictionDidUpdateNotifier;
@property (TQ,R,N,V_restrictedState) restrictedState;
```

## Instance methods

```
-[CTCellularData init];
-[CTCellularData dealloc];
-[CTCellularData restrictedState];
-[CTCellularData cellularDataRestrictionDidUpdateNotifier];
-[CTCellularData setCellularDataRestrictionDidUpdateNotifier:];
-[CTCellularData setCellularDataRestrictionStateFromPolicies:];
```
