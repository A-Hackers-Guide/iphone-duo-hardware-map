# `SBSystemApertureRestrictionServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSSystemApertureRestrictionServiceServerInterface`, `BSInvalidatable`
- 7 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clientServiceCollectionLock;
@"NSMutableArray" _connections;
@"NSMutableArray" _remoteAssertions;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnectionListener" _connectionListener;
B _isValid;
@"<SBSystemApertureRestrictionServerDelegate>" _delegate;
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
-[SBSystemApertureRestrictionServer listener:didReceiveConnection:withContext:];
-[SBSystemApertureRestrictionServer initWithDelegate:];
-[SBSystemApertureRestrictionServer invalidate];
-[SBSystemApertureRestrictionServer acquireRestrictSystemApertureLayoutToInertAssertionIdentifierWithReason:];
-[SBSystemApertureRestrictionServer acquireSuppressHidingEmptySystemApertureOnClonedDisplaysAssertionIdentifierWithReason:];
-[SBSystemApertureRestrictionServer acquireSystemApertureCompleteSuppressionAssertionIdentifierWithReason:];
-[SBSystemApertureRestrictionServer invalidateRestrictSystemApertureLayoutToInertAssertionWithIdentifier:];
-[SBSystemApertureRestrictionServer invalidateSuppressHidingEmptySystemApertureOnClonedDisplaysAssertionWithIdentifier:];
-[SBSystemApertureRestrictionServer invalidateSystemApertureCompleteSuppressionAssertionWithIdentifier:];
```
