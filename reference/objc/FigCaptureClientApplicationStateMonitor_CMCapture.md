# `FigCaptureClientApplicationStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureDisplayLayoutObserver`, `FigCaptureDeviceLockStateObserver`
- 31 instance variables, 10 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"FigCaptureClientApplicationStateMonitorClient" _client;
^{OpaqueFigSimpleMutex=} _stateChangeLock;
@"AVAudioSession" _audioSession;
@ _applicationStateDidChangeNotificationToken;
@ _audioSessionMediaServicesWereResetNotificationToken;
@"RBSProcessMonitor" _mediaEndowmentMonitor;
B _isVisibilityEndowmentMonitoringRequiredForClient;
@"RBSProcessMonitor" _visibilityEndowmentMonitor;
B _isBKSApplicationStateMonitoringRequiredForClient;
I _bksApplicationState;
B _bksApplicationStateInitialized;
i _applicationState;
B _isLayoutMonitoringRequiredForClient;
i _layoutState;
B _layoutStateInitialized;
B _isExternalDisplayLayoutMonitoringRequiredForClient;
i _externalDisplayLayoutState;
B _isExternalDisplayLayoutStateInitialized;
B _isContinuityDisplayLayoutMonitoringRequiredForClient;
i _continuityDisplayLayoutState;
B _isContinuityDisplayLayoutStateInitialized;
i _aggregateLayoutState;
B _rawBackgroundedState;
@"FigCaptureDisplayLayoutMonitor" _displayLayoutMonitor;
@"FigCaptureDisplayLayoutMonitor" _externalDisplayLayoutMonitor;
@"FigCaptureDisplayLayoutMonitor" _continuityDisplayLayoutMonitor;
B _isDeviceLockStateMonitoringRequiredForClient;
B _deviceIsLocked;
B _deviceLockStateInitialized;
@"FigCaptureDeviceLockStateMonitor" _deviceLockStateMonitor;
B _invalid;
```

## Properties

```
@property (T{?=[8I]},R) clientAuditToken;
@property (T@"NSString",R) applicationID;
@property (Ti,R) applicationState;
@property (Ti,R) clientType;
@property (T@"NSString",R,N) mediaEnvironment;
@property (T@"NSObject<OS_tcc_identity>",R,N) mediaEnvironmentTCCIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureClientApplicationStateMonitor initialize];
+[FigCaptureClientApplicationStateMonitor startContinuityCaptureTerminationMonitorWithHandler:];
+[FigCaptureClientApplicationStateMonitor startPrewarmingMonitorWithHandler:];
+[FigCaptureClientApplicationStateMonitor stopPrewarmingMonitor];
```

## Instance methods

```
-[FigCaptureClientApplicationStateMonitor clientType];
-[FigCaptureClientApplicationStateMonitor applicationID];
-[FigCaptureClientApplicationStateMonitor debugDescription];
-[FigCaptureClientApplicationStateMonitor layoutMonitor:didUpdateLayout:];
-[FigCaptureClientApplicationStateMonitor applicationState];
-[FigCaptureClientApplicationStateMonitor mediaEnvironmentTCCIdentity];
-[FigCaptureClientApplicationStateMonitor clientAuditToken];
-[FigCaptureClientApplicationStateMonitor dealloc];
-[FigCaptureClientApplicationStateMonitor mediaEnvironment];
-[FigCaptureClientApplicationStateMonitor invalidate];
-[FigCaptureClientApplicationStateMonitor description];
-[FigCaptureClientApplicationStateMonitor deviceLockStateMonitor:didUpdateDeviceLockState:];
-[FigCaptureClientApplicationStateMonitor initWithClientAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:];
-[FigCaptureClientApplicationStateMonitor updateApplicationState];
```
