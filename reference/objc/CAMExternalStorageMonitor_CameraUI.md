# `CAMExternalStorageMonitor`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _hasExternalStorageNotRecommendedForCapture;
B _initialReportPending;
B __isObservingKVO;
B __hasPendingChangesSinceLastDelegateCall;
@"<CAMExternalStorageMonitorDelegate>" _delegate;
Q _monitoringState;
@"NSArray" _connectedStorageDevices;
@"AVExternalStorageDeviceDiscoverySession" __externalStorageDiscoverySession;
@ __monitoringContext;
@"NSObject<OS_dispatch_queue>" __authorizationQueue;
```

## Properties

```
@property (T@"AVExternalStorageDeviceDiscoverySession",&,N,V__externalStorageDiscoverySession) _externalStorageDiscoverySession;
@property (T@,&,N,V__monitoringContext) _monitoringContext;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__authorizationQueue) _authorizationQueue;
@property (TB,N,V__isObservingKVO) _isObservingKVO;
@property (TB,N,V__hasPendingChangesSinceLastDelegateCall) _hasPendingChangesSinceLastDelegateCall;
@property (T@"<CAMExternalStorageMonitorDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_monitoringState) monitoringState;
@property (T@"NSArray",R,N,V_connectedStorageDevices) connectedStorageDevices;
@property (TB,R,N,V_hasExternalStorageNotRecommendedForCapture) hasExternalStorageNotRecommendedForCapture;
@property (TB,R,N,V_initialReportPending) initialReportPending;
```

## Class methods

```
+[CAMExternalStorageMonitor _stringFromMonitoringState:];
```

## Instance methods

```
-[CAMExternalStorageMonitor _beginMonitoring];
-[CAMExternalStorageMonitor observeValueForKeyPath:ofObject:change:context:];
-[CAMExternalStorageMonitor init];
-[CAMExternalStorageMonitor setDelegate:];
-[CAMExternalStorageMonitor delegate];
-[CAMExternalStorageMonitor _isObservingKVO];
-[CAMExternalStorageMonitor monitoringState];
-[CAMExternalStorageMonitor _authorizationQueue];
-[CAMExternalStorageMonitor _beginInitialReportSettling];
-[CAMExternalStorageMonitor _endMonitoring];
-[CAMExternalStorageMonitor _externalStorageDiscoverySession];
-[CAMExternalStorageMonitor _handleInitialReportSettlingElapsed];
-[CAMExternalStorageMonitor _hasPendingChangesSinceLastDelegateCall];
-[CAMExternalStorageMonitor _logMonitoringChangeFromState:toState:];
-[CAMExternalStorageMonitor _monitoringContext];
-[CAMExternalStorageMonitor _resolveInitialReportPendingForConnectedStorageDevices:];
-[CAMExternalStorageMonitor _resumeMonitoring];
-[CAMExternalStorageMonitor connectedStorageDevices];
-[CAMExternalStorageMonitor hasExternalStorageNotRecommendedForCapture];
-[CAMExternalStorageMonitor initialReportPending];
-[CAMExternalStorageMonitor setMonitoringState:];
-[CAMExternalStorageMonitor set_externalStorageDiscoverySession:];
-[CAMExternalStorageMonitor set_hasPendingChangesSinceLastDelegateCall:];
-[CAMExternalStorageMonitor set_isObservingKVO:];
-[CAMExternalStorageMonitor set_monitoringContext:];
```
