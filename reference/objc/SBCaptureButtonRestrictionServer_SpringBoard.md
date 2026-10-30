# `SBCaptureButtonRestrictionServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSCaptureButtonRestrictionServiceServerInterface`, `BSInvalidatable`
- 7 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clientServiceCollectionLock;
@"NSMutableSet" _connections;
@"NSMutableDictionary" _versionedPIDToRemoteAssertion;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnectionListener" _connectionListener;
@"<SBCaptureButtonRestrictionServerDelegate>" _delegate;
B _isValid;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureButtonRestrictionServer listener:didReceiveConnection:withContext:];
-[SBCaptureButtonRestrictionServer initWithDelegate:];
-[SBCaptureButtonRestrictionServer dealloc];
-[SBCaptureButtonRestrictionServer invalidate];
-[SBCaptureButtonRestrictionServer setCaptureButtonActionInhibited:options:];
```
