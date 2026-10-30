# `_SBContinuitySessionServiceClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionStateObserver`, `SBContinuitySessionOrientationObserver`, `SBContinuitySessionResizeObserver`, `BSDescriptionStreaming`
- 21 instance variables, 19 properties, 56 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
B _lock_waitingForClientActivation;
B _main_suppressClientCallouts;
B _main_sentDisplayUUID;
B _main_sentResizabilityConfiguration;
B _negotiatingSessionStart;
B _resizable;
i _pid;
@"<_SBContinuitySessionServiceClientDelegate>" _delegate;
@"SBContinuitySession" _session;
@"NSSet" _clientExternallyBlockedReasons;
Q _state;
@"NSSet" _stateReasons;
q _interfaceOrientation;
Q _supportedInterfaceOrientations;
@"NSString" _displayHardwareIdentifier;
@"BSServiceConnection" _connection;
{CGSize="width"d"height"d} _minAllowableSize;
{CGSize="width"d"height"d} _maxAllowableSize;
{CGSize="width"d"height"d} _sceneSize;
```

## Properties

```
@property (Ti,R,N,V_pid) pid;
@property (T@"NSSet",&,N,V_clientExternallyBlockedReasons) clientExternallyBlockedReasons;
@property (TQ,N,V_state) state;
@property (T@"NSSet",C,N,V_stateReasons) stateReasons;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (TQ,N,V_supportedInterfaceOrientations) supportedInterfaceOrientations;
@property (T@"NSString",C,N,V_displayHardwareIdentifier) displayHardwareIdentifier;
@property (T{CGSize=dd},N,V_minAllowableSize) minAllowableSize;
@property (T{CGSize=dd},N,V_maxAllowableSize) maxAllowableSize;
@property (TB,N,V_resizable) resizable;
@property (T{CGSize=dd},N,V_sceneSize) sceneSize;
@property (T@"BSServiceConnection",R,N,V_connection) connection;
@property (T@"<_SBContinuitySessionServiceClientDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,C,N) externallyBlockedReasons;
@property (T@"SBContinuitySession",&,N,V_session) session;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBContinuitySessionServiceClient interfaceOrientation];
-[_SBContinuitySessionServiceClient setState:];
-[_SBContinuitySessionServiceClient setInterfaceOrientation:];
-[_SBContinuitySessionServiceClient supportedInterfaceOrientations];
-[_SBContinuitySessionServiceClient succinctDescription];
-[_SBContinuitySessionServiceClient setSession:];
-[_SBContinuitySessionServiceClient pid];
-[_SBContinuitySessionServiceClient setDelegate:];
-[_SBContinuitySessionServiceClient connection];
-[_SBContinuitySessionServiceClient delegate];
-[_SBContinuitySessionServiceClient description];
-[_SBContinuitySessionServiceClient appendDescriptionToStream:];
-[_SBContinuitySessionServiceClient session];
-[_SBContinuitySessionServiceClient state];
-[_SBContinuitySessionServiceClient resizable];
-[_SBContinuitySessionServiceClient setResizable:];
-[_SBContinuitySessionServiceClient setSupportedInterfaceOrientations:];
-[_SBContinuitySessionServiceClient displayHardwareIdentifier];
-[_SBContinuitySessionServiceClient continuitySession:didUpdateResizability:];
-[_SBContinuitySessionServiceClient continuitySession:didUpdateSceneSize:];
-[_SBContinuitySessionServiceClient externallyBlockedReasons];
-[_SBContinuitySessionServiceClient sceneSize];
-[_SBContinuitySessionServiceClient initWithConnection:pid:];
-[_SBContinuitySessionServiceClient _pushLatestResizabilityToClient];
-[_SBContinuitySessionServiceClient _connectionQueue_clientHasAdoptedScreenCaptureNotifications];
-[_SBContinuitySessionServiceClient _connectionQueue_didCaptureScreenshot];
-[_SBContinuitySessionServiceClient _connectionQueue_didInvalidate];
-[_SBContinuitySessionServiceClient _connectionQueue_didStartScreenRecording];
-[_SBContinuitySessionServiceClient _connectionQueue_didStopScreenRecording];
-[_SBContinuitySessionServiceClient _connectionQueue_handleActivated];
-[_SBContinuitySessionServiceClient _connectionQueue_handleContinuityButtonEvent:];
-[_SBContinuitySessionServiceClient _connectionQueue_handleHIDServicesConfigured];
-[_SBContinuitySessionServiceClient _connectionQueue_handleLaunchEventOfType:payload:];
-[_SBContinuitySessionServiceClient _connectionQueue_handleUpdatedExternallyBlockedReasons:];
-[_SBContinuitySessionServiceClient _connectionQueue_setHostedInterfaceOrientation:];
-[_SBContinuitySessionServiceClient _connectionQueue_updateCornerRadiusForResize:];
-[_SBContinuitySessionServiceClient _connectionQueue_updateHostMaximumAllowableSize:];
-[_SBContinuitySessionServiceClient _connectionQueue_updateUserPreferredSize:toggleToOriginalSize:];
-[_SBContinuitySessionServiceClient _connectionQueue_updatedAppearanceSettings:transitionContext:completion:];
-[_SBContinuitySessionServiceClient _pushLatestOrientationToClient];
-[_SBContinuitySessionServiceClient _pushLatestResizableSizeToClient];
-[_SBContinuitySessionServiceClient _pushLatestSceneSizeToClient];
-[_SBContinuitySessionServiceClient _pushLatestStateToClient];
-[_SBContinuitySessionServiceClient clientExternallyBlockedReasons];
-[_SBContinuitySessionServiceClient continuitySession:didUpdateInterfaceOrientation:supportedInterfaceOrientations:];
-[_SBContinuitySessionServiceClient continuitySession:didUpdateMinAllowableSize:maxAllowableSize:];
-[_SBContinuitySessionServiceClient continuitySessionDidUpdateState:];
-[_SBContinuitySessionServiceClient maxAllowableSize];
-[_SBContinuitySessionServiceClient minAllowableSize];
-[_SBContinuitySessionServiceClient setClientExternallyBlockedReasons:];
-[_SBContinuitySessionServiceClient setDisplayHardwareIdentifier:];
-[_SBContinuitySessionServiceClient setMaxAllowableSize:];
-[_SBContinuitySessionServiceClient setMinAllowableSize:];
-[_SBContinuitySessionServiceClient setSceneSize:];
-[_SBContinuitySessionServiceClient setStateReasons:];
-[_SBContinuitySessionServiceClient stateReasons];
```
