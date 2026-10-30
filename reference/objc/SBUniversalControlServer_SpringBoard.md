# `SBUniversalControlServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSUniversalControlClientToServerInterface`, `BSServiceConnectionListenerDelegate`, `BSDescriptionStreamable`
- 13 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _connectionListener;
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableSet" _connections;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _lock_keyboardDisabledReasonsByPID;
@"NSMutableDictionary" _lock_screenEdgesOwnedByPID;
@"<BSInvalidatable>" _lock_keyboardFocusAssertion;
@"<BSInvalidatable>" _lock_keyboardSuppressionAssertion;
Q _lock_externallyControlledScreenEdgeMask;
Q _externalProcessActiveOnScreenEdges;
@"<SBKeyboardFocusControlling>" _keyboardFocusController;
@"SBKeyboardSuppressionManager" _keyboardSuppressionManager;
```

## Properties

```
@property (TQ,N,V_externalProcessActiveOnScreenEdges) externalProcessActiveOnScreenEdges;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUniversalControlServer listener:didReceiveConnection:withContext:];
-[SBUniversalControlServer appendDescriptionToFormatter:];
-[SBUniversalControlServer description];
-[SBUniversalControlServer setKeyboardFocusDisabled:reason:];
-[SBUniversalControlServer setScreenEdgesOwned:reason:];
-[SBUniversalControlServer _queue_addConnection:];
-[SBUniversalControlServer _queue_removeConnection:];
-[SBUniversalControlServer _lock_reevaluateKeyboardFocusDisablement];
-[SBUniversalControlServer _lock_reevaluateScreenEdgeOwnership];
-[SBUniversalControlServer externalProcessActiveOnScreenEdges];
-[SBUniversalControlServer initWithKeyboardFocusController:keyboardSuppressionManager:];
-[SBUniversalControlServer setExternalProcessActiveOnScreenEdges:];
```
