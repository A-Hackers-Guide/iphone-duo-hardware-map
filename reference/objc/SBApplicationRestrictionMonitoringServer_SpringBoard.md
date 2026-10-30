# `SBApplicationRestrictionMonitoringServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBApplicationRestrictionObserver`
- 7 instance variables, 11 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _listener;
@"FBServiceClientAuthenticator" _authenticator;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _connections;
@"NSUUID" _pendingRestrictionUpdateUUID;
@"BSCompoundAssertion" _pendingRestrictionUpdateAssertion;
@"<BSInvalidatable>" _restrictionControllerDidFinishNotifyingObserversAssertion;
```

## Properties

```
@property (T@"BSServiceConnectionListener",R,N,V_listener) listener;
@property (T@"FBServiceClientAuthenticator",R,N,V_authenticator) authenticator;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSMutableArray",R,N,V_connections) connections;
@property (T@"NSUUID",&,N,V_pendingRestrictionUpdateUUID) pendingRestrictionUpdateUUID;
@property (T@"BSCompoundAssertion",&,N,V_pendingRestrictionUpdateAssertion) pendingRestrictionUpdateAssertion;
@property (T@"<BSInvalidatable>",&,N,V_restrictionControllerDidFinishNotifyingObserversAssertion) restrictionControllerDidFinishNotifyingObserversAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationRestrictionMonitoringServer applicationRestrictionController:didUpdateVisibleTags:hiddenTags:];
-[SBApplicationRestrictionMonitoringServer listener:didReceiveConnection:withContext:];
-[SBApplicationRestrictionMonitoringServer connections];
-[SBApplicationRestrictionMonitoringServer init];
-[SBApplicationRestrictionMonitoringServer queue];
-[SBApplicationRestrictionMonitoringServer listener];
-[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerDidPostAppVisibilityUpdate:];
-[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerWillPostAppVisibilityUpdate:];
-[SBApplicationRestrictionMonitoringServer authenticator];
-[SBApplicationRestrictionMonitoringServer acquireApplicationRestrictionUpdatePendingAssertionForReason:];
-[SBApplicationRestrictionMonitoringServer pendingRestrictionUpdateAssertion];
-[SBApplicationRestrictionMonitoringServer pendingRestrictionUpdateUUID];
-[SBApplicationRestrictionMonitoringServer restrictionControllerDidFinishNotifyingObserversAssertion];
-[SBApplicationRestrictionMonitoringServer setPendingRestrictionUpdateAssertion:];
-[SBApplicationRestrictionMonitoringServer setPendingRestrictionUpdateUUID:];
-[SBApplicationRestrictionMonitoringServer setRestrictionControllerDidFinishNotifyingObserversAssertion:];
```
