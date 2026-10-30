# `AVCaptureConnectionInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 55 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" inputPorts;
@"AVCaptureDeviceInput" sourceDeviceInput;
@"AVCaptureDevice" sourceDevice;
@"AVWeakReference" outputWeakReference;
@"AVWeakReference" videoPreviewLayerWeakReference;
B hasActiveObservers;
B active;
B enabled;
i changeSeed;
@"AVCaptureInputPort" audioInputPort;
I spatialAudioChannelLayoutTagForChannelLevels;
@"NSMutableArray" audioChannels;
@"NSArray" audioChannelLevels;
q lastGetAudioLevelsTime;
@"AVCaptureInputPort" videoInputPort;
@"AVCaptureInputPort" secureVideoInputPort;
@"AVCaptureInputPort" metadataInputPort;
@"AVCaptureInputPort" metadataItemInputPort;
@"AVCaptureInputPort" depthDataInputPort;
@"AVCaptureInputPort" visionDataInputPort;
@"AVCaptureInputPort" pointCloudDataInputPort;
@"AVCaptureInputPort" cameraCalibrationDataInputPort;
B videoMirroringSupported;
B automaticallyAdjustsVideoMirroring;
B videoMirrored;
B videoRotationSupported;
d videoRotationAngle;
B v68CompatibilityEnabledForConnection;
d v68CompatibilityCoordinatorAngle;
{?="value"q"timescale"i"flags"I"epoch"q} videoMinFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} videoMaxFrameDuration;
d videoMaxScaleAndCropFactor;
d videoScaleAndCropFactor;
i videoRetainedBufferCountHint;
q preferredVideoStabilizationMode;
B videoStabilizationEnabled;
q activeVideoStabilizationMode;
B hasVideoMinFrameDurationObserver;
@"NSString" connectionID;
B cameraIntrinsicMatrixDeliverySupported;
B cameraIntrinsicMatrixDeliveryEnabled;
B livePhotoMetadataWritingEnabled;
B debugMetadataSidecarFileEnabled;
B videoDBGFileEnabled;
@"NSArray" supportedVideoMirroringMethodsForMovieRecording;
q videoMirroringMethodForMovieRecording;
B videoZoomSmoothingSupported;
B videoZoomSmoothingEnabled;
B videoGreenGhostMitigationSupported;
B videoGreenGhostMitigationEnabled;
B videoDeviceOrientationCorrectionSupported;
B videoDeviceOrientationCorrectionEnabled;
B lowLightVideoNoiseReductionSupported;
B lowLightVideoNoiseReductionEnabled;
B automaticallyEnablesLowLightVideoNoiseReduction;
```
