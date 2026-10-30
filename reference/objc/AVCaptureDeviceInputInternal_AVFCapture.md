# `AVCaptureDeviceInputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureDevice" device;
@"NSArray" ports;
@"NSArray" multiCamPorts;
B unifiedAutoExposureDefaultsEnabled;
q audioCaptureMode;
q multichannelAudioMode;
B windNoiseRemovalEnabled;
B audioZoomEnabled;
B cinematicVideoCaptureSupported;
B cinematicVideoCaptureEnabled;
B visionDataDeliveryEnabled;
B cameraCalibrationDataDeliveryEnabled;
f simulatedAperture;
{?="value"q"timescale"i"flags"I"epoch"q} videoMinFrameDurationOverride;
B lockedVideoFrameDurationSupported;
{?="value"q"timescale"i"flags"I"epoch"q} activeLockedVideoFrameDuration;
B externalSyncSupported;
{?="value"q"timescale"i"flags"I"epoch"q} activeExternalSyncVideoFrameDuration;
@"AVExternalSyncDevice" activeVideoExternalSyncDevice;
f maxGainOverride;
B centerStageAllowed;
B backgroundBlurAllowed;
B studioLightingAllowed;
B reactionEffectsAllowed;
B backgroundReplacementAllowed;
@"NSObject<OS_xpc_object>" sensitiveContentAnalyzerXPCObject;
B sensitiveContentAnalyzerEnabled;
B ready;
f portraitLightingEffectStrength;
@"AVWeakReference" weakReference;
@"<AVCallbackCancellation>" deviceOpenCallbackInvoker;
@"AVAudioFormat" remoteIOOutputFormat;
```

## Instance methods

```
-[AVCaptureDeviceInputInternal dealloc];
```
