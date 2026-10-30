# `AVCaptureMovieFileOutputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 34 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
@"NSMutableArray" recordingDelegatesArray;
@"NSMutableArray" connectionsThatRecordVideoOrientationAndMirroringChangesAsMetadataTrack;
{?="value"q"timescale"i"flags"I"epoch"q} movieFragmentInterval;
@"NSArray" metadata;
@"NSArray" availableVideoCodecs;
@"NSString" videoCodec;
@"NSDictionary" videoCompressionProperties;
B sendLastVideoPreviewFrame;
B recording;
B paused;
B primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled;
q primaryConstituentDeviceSwitchingBehavior;
Q primaryConstituentDeviceRestrictedSwitchingBehaviorConditions;
B deviceSupportsConstituentDeviceSwitching;
B deviceIsBravoVariant;
B deviceExposesOmahaConstituentDevices;
^{ct_green_tea_logger_s=} greenTeaLogger;
B streamingDepthSupported;
B depthCaptureEnabled;
B usesVirtualCaptureCard;
B spatialVideoCaptureSupported;
B spatialVideoCaptureEnabled;
@"NSObject<OS_dispatch_queue>" timewarpDecimationQueue;
q timewarpMode;
{?="value"q"timescale"i"flags"I"epoch"q} timewarpDestinationFrameRate;
B trueVideoCaptureSupported;
B trueVideoCaptureEnabled;
B multiCamClientCompositingEnabled;
@"AVCaptureConnection" multiCamClientCompositingPrimaryConnection;
B cinematicVideoMetadataCaptureSupported;
B cinematicVideoMetadataAspectRatioSupported;
B automaticallyAdjustsCinematicVideoMetadataCaptureEnabled;
B cinematicVideoMetadataCaptureEnabledByClient;
```

## Instance methods

```
-[AVCaptureMovieFileOutputInternal init];
-[AVCaptureMovieFileOutputInternal dealloc];
```
