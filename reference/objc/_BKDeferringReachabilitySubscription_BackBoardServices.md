# `_BKDeferringReachabilitySubscription`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _hasDeliveredInitialState;
B _respectsConstraints;
@"BKSHIDEventDeferringSelectionTarget" _target;
@? _handler;
@"BKSHIDEventDeferringReachabilityStatus" _lastStatus;
```

## Properties

```
@property (T@"BKSHIDEventDeferringSelectionTarget",&,N,V_target) target;
@property (T@?,C,N,V_handler) handler;
@property (T@"BKSHIDEventDeferringReachabilityStatus",&,N,V_lastStatus) lastStatus;
@property (TB,N,V_hasDeliveredInitialState) hasDeliveredInitialState;
@property (TB,N,V_respectsConstraints) respectsConstraints;
```

## Instance methods

```
-[_BKDeferringReachabilitySubscription setHandler:];
-[_BKDeferringReachabilitySubscription handler];
-[_BKDeferringReachabilitySubscription setTarget:];
-[_BKDeferringReachabilitySubscription target];
-[_BKDeferringReachabilitySubscription hasDeliveredInitialState];
-[_BKDeferringReachabilitySubscription lastStatus];
-[_BKDeferringReachabilitySubscription respectsConstraints];
-[_BKDeferringReachabilitySubscription setHasDeliveredInitialState:];
-[_BKDeferringReachabilitySubscription setLastStatus:];
-[_BKDeferringReachabilitySubscription setRespectsConstraints:];
```
