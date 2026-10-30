# `AVExternalSyncDevice`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVExternalSyncDeviceDeviceNotificationDelegate`
- 16 instance variables, 18 properties, 45 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _deviceWeakReference;
^{OpaqueCMClock=} _clock;
B _usbConnected;
@"AVWeakReference" _delegate;
@"FigStateMachine" _stateMachine;
@"NSObject<OS_dispatch_queue>" _queue;
@? _configurationTimeoutBlock;
@? _unfollowTimeoutBlock;
@"AVCaptureDeviceInput" _captureDeviceInput;
@"NSString" _uniqueIdentifier;
I _vendorID;
I _productID;
B _sessionRunning;
B _locked;
@"NSUUID" _uuid;
{?="value"q"timescale"i"flags"I"epoch"q} _signalCompensationDelay;
```

## Properties

```
@property (TB,R,N,GisUsbConnected,V_usbConnected) usbConnected;
@property (T@"NSString",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@?,C,N,V_configurationTimeoutBlock) configurationTimeoutBlock;
@property (TB,N,GisLocked,V_locked) locked;
@property (TB,N,GisSessionRunning,V_sessionRunning) sessionRunning;
@property (Tq,R,N) state;
@property (Tq,R,N) status;
@property (T^{OpaqueCMClock=},R,N,V_clock) clock;
@property (TB,R,N,GisSignalCompensationDelaySupported) signalCompensationDelaySupported;
@property (T{?=qiIq},N,V_signalCompensationDelay) signalCompensationDelay;
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (TI,R,N,V_vendorID) vendorID;
@property (TI,R,N,V_productID) productID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVExternalSyncDevice initialize];
```

## Instance methods

```
-[AVExternalSyncDevice vendorID];
-[AVExternalSyncDevice _setDelegate:];
-[AVExternalSyncDevice clock];
-[AVExternalSyncDevice productID];
-[AVExternalSyncDevice isLocked];
-[AVExternalSyncDevice setLocked:];
-[AVExternalSyncDevice uuid];
-[AVExternalSyncDevice _notifyDelegateOfError:];
-[AVExternalSyncDevice dealloc];
-[AVExternalSyncDevice status];
-[AVExternalSyncDevice queue];
-[AVExternalSyncDevice uniqueIdentifier];
-[AVExternalSyncDevice _setClock:];
-[AVExternalSyncDevice isSessionRunning];
-[AVExternalSyncDevice state];
-[AVExternalSyncDevice _setupStateMachine];
-[AVExternalSyncDevice _handleUnfollow];
-[AVExternalSyncDevice _handleSourceDiedEvent];
-[AVExternalSyncDevice _handleUSBConnectionStateChange:];
-[AVExternalSyncDevice _initWithIdentifier:pid:vid:];
-[AVExternalSyncDevice applyActiveExternalSyncVideoFrameDuration];
-[AVExternalSyncDevice configurationTimeoutBlock];
-[AVExternalSyncDevice handleClockReceived:];
-[AVExternalSyncDevice handleClockSetupFailedWithError:];
-[AVExternalSyncDevice handleFollowForDevice:withSessionRunning:];
-[AVExternalSyncDevice handleFollowTimeout];
-[AVExternalSyncDevice handleLockStateUpdateTriggerID:lockState:];
-[AVExternalSyncDevice handleSessionStateChange:];
-[AVExternalSyncDevice handleTSMSGOutOfBoundsTriggerID:error:];
-[AVExternalSyncDevice handleTSMSGSessionStoppedTriggerID:status:];
-[AVExternalSyncDevice handleTransitionToActiveSync];
-[AVExternalSyncDevice handleTransitionToActiveSyncFromConfiguring];
-[AVExternalSyncDevice handleTransitionToConfiguring];
-[AVExternalSyncDevice handleTransitionToIdle];
-[AVExternalSyncDevice handleTransitionToJamSync];
-[AVExternalSyncDevice handleTransitionToUnavailable];
-[AVExternalSyncDevice handleTriggerPresentTriggerID:isPresentState:];
-[AVExternalSyncDevice handleUnfollow];
-[AVExternalSyncDevice isSignalCompensationDelaySupported];
-[AVExternalSyncDevice isUsbConnected];
-[AVExternalSyncDevice notifyDelegateStatusChange];
-[AVExternalSyncDevice setConfigurationTimeoutBlock:];
-[AVExternalSyncDevice setSessionRunning:];
-[AVExternalSyncDevice setSignalCompensationDelay:];
-[AVExternalSyncDevice signalCompensationDelay];
```
