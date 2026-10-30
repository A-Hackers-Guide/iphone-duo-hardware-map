# `AVCaptureVideoDataOutputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
@"NSDictionary" videoSettings;
@"NSDictionary" clientVideoSettings;
{?="value"q"timescale"i"flags"I"epoch"q} deprecatedMinFrameDuration;
B alwaysDiscardsLateVideoFrames;
B automaticallyConfiguresOutputBufferDimensions;
B deliversPreviewSizedOutputBuffers;
B sceneStabilityMetadataEnabled;
B allLossyVideoCVPixelFormatTypesEnabled;
@"NSArray" requestedBufferAttachments;
B videoSettingsDimensionsOverrideEnabled;
B videoSettingsDimensionsOverrideEnabledByClient;
B videoSettingsAspectRatioOverrideEnabled;
@"NSArray" availableVideoCVPixelFormatTypes;
@"AVCaptureDataOutputDelegateCallbackHelper" delegateCallbackHelper;
@"FigCaptureFrameRateMonitor" frameRateMonitor;
B preparesCellularRadioForNetworkConnection;
B preparesCellularRadioForNetworkConnectionSetByClient;
B preservesDynamicHDRMetadata;
B panoRecordingInProgress;
```

## Instance methods

```
-[AVCaptureVideoDataOutputInternal init];
-[AVCaptureVideoDataOutputInternal dealloc];
```
