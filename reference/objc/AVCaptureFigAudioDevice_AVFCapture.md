# `AVCaptureFigAudioDevice`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureDevice`
- 23 instance variables, 0 properties, 38 instance methods, 5 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _fcsQueue;
^{OpaqueFigCaptureSource=} _fcs;
@"FigCaptureSourceAttributes" _attributes;
@"AVInputDeviceDiscoverySession" _inputDeviceDiscoverySession;
@"AVInputContext" _inputContext;
@"AVAudioSession" _auxiliarySession;
@"AVInputDevice" _committedInputDevice;
B _levelMeteringEnabled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _isConnectedLock;
B _isConnected;
B _isSoonToBeDisconnected;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _localizedNameLock;
@"NSString" _localizedName;
@"NSObject<OS_dispatch_queue>" _audioRoutesInfoUpdateQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _audioRoutesInfoLock;
@"NSObject<OS_dispatch_group>" _audioRoutesInfoFirstQueryGroup;
B _audioInputRouteIsBuiltInMic;
@"AVWeakReference" _weakReference;
@"NSObject<OS_dispatch_semaphore>" _serverConnectionDiedSemaphore;
@"NSString" _clientAudioClockDeviceUID;
^{OpaqueCMClock=} _sharedAVAudioSessionClock;
@"NSNumber" _preferredIOBufferDuration;
B _allowsBluetoothHighQualityRecording;
```

## Class methods

```
+[AVCaptureFigAudioDevice _devicesWithPriorRegisteredDevices:];
+[AVCaptureFigAudioDevice _reconnectDevices:];
+[AVCaptureFigAudioDevice initialize];
+[AVCaptureFigAudioDevice _devices];
+[AVCaptureFigAudioDevice _newFigCaptureSources];
```

## Instance methods

```
-[AVCaptureFigAudioDevice isWindNoiseRemovalSupported];
-[AVCaptureFigAudioDevice isConnected];
-[AVCaptureFigAudioDevice deviceClock];
-[AVCaptureFigAudioDevice _copyFigCaptureSourceProperty:];
-[AVCaptureFigAudioDevice _handleNotification:payload:];
-[AVCaptureFigAudioDevice clientAudioClockDeviceUID];
-[AVCaptureFigAudioDevice init];
-[AVCaptureFigAudioDevice deviceType];
-[AVCaptureFigAudioDevice isAudioCaptureModeSupported:];
-[AVCaptureFigAudioDevice modelID];
-[AVCaptureFigAudioDevice dealloc];
-[AVCaptureFigAudioDevice _setFigCaptureSource:];
-[AVCaptureFigAudioDevice fallbackAudioCaptureModeIfApplicableForCurrentRoute:];
-[AVCaptureFigAudioDevice manufacturer];
-[AVCaptureFigAudioDevice _currentAudioInputDeviceLocalizedName:];
-[AVCaptureFigAudioDevice localizedName];
-[AVCaptureFigAudioDevice isAudioInputRouteBuiltInMic];
-[AVCaptureFigAudioDevice uniqueID];
-[AVCaptureFigAudioDevice _reconnectToFigCaptureSource:];
-[AVCaptureFigAudioDevice audioInputDeviceDidChangeHandler:];
-[AVCaptureFigAudioDevice preferredIOBufferDuration];
-[AVCaptureFigAudioDevice setPreferredIOBufferDuration:];
-[AVCaptureFigAudioDevice _systemHasAudioInputDevice];
-[AVCaptureFigAudioDevice setClientAudioClockDeviceUID:];
-[AVCaptureFigAudioDevice setAllowsBluetoothHighQualityRecording:];
-[AVCaptureFigAudioDevice figCaptureSource];
-[AVCaptureFigAudioDevice supportsAVCaptureSessionPreset:];
-[AVCaptureFigAudioDevice _currentAudioInputRouteIsBuiltInMic];
-[AVCaptureFigAudioDevice shouldAudioCaptureModeTriggerGraphRebuildOnAudioRouteChange:];
-[AVCaptureFigAudioDevice _updateStateForInputDevice:];
-[AVCaptureFigAudioDevice isSoonToBeDisconnected];
-[AVCaptureFigAudioDevice isBuiltInStereoAudioCaptureSupported];
-[AVCaptureFigAudioDevice hasMediaType:];
-[AVCaptureFigAudioDevice startUsingDevice:];
-[AVCaptureFigAudioDevice stopUsingDevice];
-[AVCaptureFigAudioDevice figCaptureSourceAudioSettingsForSessionPreset:];
-[AVCaptureFigAudioDevice _initWithFigCaptureSource:];
-[AVCaptureFigAudioDevice audioServicesWereResetHandler:];
```
