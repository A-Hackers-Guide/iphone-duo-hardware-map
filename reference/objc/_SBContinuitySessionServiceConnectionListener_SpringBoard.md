# `_SBContinuitySessionServiceConnectionListener`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIContinuitySessionServiceClientToServerInterface`, `BSServiceConnectionListenerDelegate`, `BSInvalidatable`
- 6 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMapTable" _lock_connectionToClientMap;
@"FBServiceClientAuthenticator" _serviceClientAuthenticator;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnectionListener" _connectionListener;
@"<_SBContinuitySessionServiceConnectionListenerDelegate>" _delegate;
```

## Properties

```
@property (T@"<_SBContinuitySessionServiceConnectionListenerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBContinuitySessionServiceConnectionListener listener:didReceiveConnection:withContext:];
-[_SBContinuitySessionServiceConnectionListener invalidate];
-[_SBContinuitySessionServiceConnectionListener setDelegate:];
-[_SBContinuitySessionServiceConnectionListener activate];
-[_SBContinuitySessionServiceConnectionListener delegate];
-[_SBContinuitySessionServiceConnectionListener updateHostMaximumAllowableSize:];
-[_SBContinuitySessionServiceConnectionListener clientActivated];
-[_SBContinuitySessionServiceConnectionListener clientHasAdoptedScreenCaptureNotifications];
-[_SBContinuitySessionServiceConnectionListener didCaptureScreenshot];
-[_SBContinuitySessionServiceConnectionListener didStartScreenRecording];
-[_SBContinuitySessionServiceConnectionListener didStopScreenRecording];
-[_SBContinuitySessionServiceConnectionListener didUpdateExternalBlockedReasons:];
-[_SBContinuitySessionServiceConnectionListener handleContinuityButtonEvent:];
-[_SBContinuitySessionServiceConnectionListener handleLaunchEventOfType:payload:];
-[_SBContinuitySessionServiceConnectionListener noteHIDServicesConfigured];
-[_SBContinuitySessionServiceConnectionListener setHostedInterfaceOrientation:];
-[_SBContinuitySessionServiceConnectionListener updateCornerRadiusForResize:];
-[_SBContinuitySessionServiceConnectionListener updateUserPreferredSize:toggleToOriginalSize:];
-[_SBContinuitySessionServiceConnectionListener updatedAppearanceSettings:transitionContext:completion:];
-[_SBContinuitySessionServiceConnectionListener _clientForConnection:];
-[_SBContinuitySessionServiceConnectionListener _lock_clientForConnection:];
-[_SBContinuitySessionServiceConnectionListener _removeClientForConnection:];
-[_SBContinuitySessionServiceConnectionListener _sessionServiceClientWithConnectionContext:];
-[_SBContinuitySessionServiceConnectionListener initWithServiceQueue:];
```
