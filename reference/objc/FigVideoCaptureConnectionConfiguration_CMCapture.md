# `FigVideoCaptureConnectionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureConnectionConfiguration`
- 21 instance variables, 29 properties, 60 instance methods, 2 class methods

## Instance variables

```
i _outputFormat;
i _outputWidth;
i _outputHeight;
i _videoStabilizationMethod;
i _videoStabilizationType;
B _mirroringEnabled;
B _physicalMirroringForMovieRecordingEnabled;
i _rotationDegrees;
B _deviceOrientationCorrectionEnabled;
i _additionalContentRotationDegrees;
B _zoomSmoothingEnabled;
B _videoGreenGhostMitigationEnabled;
i _retainedBufferCount;
B _cameraIntrinsicMatrixDeliveryEnabled;
B _livePhotoMetadataWritingEnabled;
B _stereoVideoCaptureEnabled;
B _attachMetadataToVideoBuffers;
i _timewarpMode;
{?="value"q"timescale"i"flags"I"epoch"q} _timewarpDestinationFrameRate;
B _lowLightVideoNoiseReductionEnabled;
B _coreMediaFaceTrackingEnabled;
```

## Properties

```
@property (TB,R) previewDepthFilterRenderingEnabled;
@property (TB,R) previewDepthDataDeliveryEnabled;
@property (TB,R) previewFilterRenderingEnabled;
@property (TB,R) portraitAutoSuggestEnabled;
@property (TB,R) irisVISEnabled;
@property (Ti,R) irisVISMethod;
@property (TB,R) irisSDOFEnabled;
@property (T{FigCaptureVideoTransform=Bi{?=ii}},R) transform;
@property (Ti,N,V_outputFormat) outputFormat;
@property (Ti,N,V_outputWidth) outputWidth;
@property (Ti,N,V_outputHeight) outputHeight;
@property (Ti,N,V_videoStabilizationMethod) videoStabilizationMethod;
@property (TB,N,V_mirroringEnabled) mirroringEnabled;
@property (TB,N,V_physicalMirroringForMovieRecordingEnabled) physicalMirroringForMovieRecordingEnabled;
@property (Ti,N,V_rotationDegrees) rotationDegrees;
@property (TB,N,V_deviceOrientationCorrectionEnabled) deviceOrientationCorrectionEnabled;
@property (Ti,N,V_additionalContentRotationDegrees) additionalContentRotationDegrees;
@property (TB,N,V_zoomSmoothingEnabled) zoomSmoothingEnabled;
@property (TB,N,V_videoGreenGhostMitigationEnabled) videoGreenGhostMitigationEnabled;
@property (Ti,N,V_retainedBufferCount) retainedBufferCount;
@property (TB,N,V_cameraIntrinsicMatrixDeliveryEnabled) cameraIntrinsicMatrixDeliveryEnabled;
@property (TB,N,V_livePhotoMetadataWritingEnabled) livePhotoMetadataWritingEnabled;
@property (T{?=ii},R,N) nonRotatedOutputDimensions;
@property (TB,N,V_stereoVideoCaptureEnabled) stereoVideoCaptureEnabled;
@property (TB,N,V_attachMetadataToVideoBuffers) attachMetadataToVideoBuffers;
@property (TB,N,V_coreMediaFaceTrackingEnabled) coreMediaFaceTrackingEnabled;
@property (Ti,N,V_timewarpMode) timewarpMode;
@property (T{?=qiIq},N,V_timewarpDestinationFrameRate) timewarpDestinationFrameRate;
@property (TB,N,V_lowLightVideoNoiseReductionEnabled) lowLightVideoNoiseReductionEnabled;
```

## Class methods

```
+[FigVideoCaptureConnectionConfiguration cameraIntrinsicMatrixDeliveryEnabled:doingFaceTracking:];
+[FigVideoCaptureConnectionConfiguration videoStabilizationMethods:includeIris:];
```

## Instance methods

```
-[FigVideoCaptureConnectionConfiguration portraitAutoSuggestEnabled];
-[FigVideoCaptureConnectionConfiguration outputHeight];
-[FigVideoCaptureConnectionConfiguration reasonForNotEqualingConfiguration:];
-[FigVideoCaptureConnectionConfiguration previewDepthFilterRenderingEnabled];
-[FigVideoCaptureConnectionConfiguration setOutputFormat:];
-[FigVideoCaptureConnectionConfiguration irisSDOFEnabled];
-[FigVideoCaptureConnectionConfiguration setZoomSmoothingEnabled:];
-[FigVideoCaptureConnectionConfiguration setVideoGreenGhostMitigationEnabled:];
-[FigVideoCaptureConnectionConfiguration rotationDegrees];
-[FigVideoCaptureConnectionConfiguration setRetainedBufferCount:];
-[FigVideoCaptureConnectionConfiguration timewarpDestinationFrameRate];
-[FigVideoCaptureConnectionConfiguration setStereoVideoCaptureEnabled:];
-[FigVideoCaptureConnectionConfiguration timewarpMode];
-[FigVideoCaptureConnectionConfiguration setVideoStabilizationMethod:];
-[FigVideoCaptureConnectionConfiguration additionalContentRotationDegrees];
-[FigVideoCaptureConnectionConfiguration irisVISMethod];
-[FigVideoCaptureConnectionConfiguration irisVISEnabled];
-[FigVideoCaptureConnectionConfiguration setMirroringEnabled:];
-[FigVideoCaptureConnectionConfiguration videoGreenGhostMitigationEnabled];
-[FigVideoCaptureConnectionConfiguration retainedBufferCount];
-[FigVideoCaptureConnectionConfiguration videoStabilizationType];
-[FigVideoCaptureConnectionConfiguration transform];
-[FigVideoCaptureConnectionConfiguration setCameraIntrinsicMatrixDeliveryEnabled:];
-[FigVideoCaptureConnectionConfiguration setPhysicalMirroringForMovieRecordingEnabled:];
-[FigVideoCaptureConnectionConfiguration setVideoStabilizationType:];
-[FigVideoCaptureConnectionConfiguration mirroringEnabled];
-[FigVideoCaptureConnectionConfiguration setOutputWidth:];
-[FigVideoCaptureConnectionConfiguration livePhotoMetadataWritingEnabled];
-[FigVideoCaptureConnectionConfiguration requiresScalingForInputTransForm:nodeName:];
-[FigVideoCaptureConnectionConfiguration setCoreMediaFaceTrackingEnabled:];
-[FigVideoCaptureConnectionConfiguration attachMetadataToVideoBuffers];
-[FigVideoCaptureConnectionConfiguration videoStabilizationMethod];
-[FigVideoCaptureConnectionConfiguration setOutputHeight:];
-[FigVideoCaptureConnectionConfiguration depthDataTransformWithSourceDimensions];
-[FigVideoCaptureConnectionConfiguration zoomSmoothingEnabled];
-[FigVideoCaptureConnectionConfiguration physicalMirroringForMovieRecordingEnabled];
-[FigVideoCaptureConnectionConfiguration deviceOrientationCorrectionEnabled];
-[FigVideoCaptureConnectionConfiguration setRotationDegrees:];
-[FigVideoCaptureConnectionConfiguration setDeviceOrientationCorrectionEnabled:];
-[FigVideoCaptureConnectionConfiguration cameraIntrinsicMatrixDeliveryEnabled];
-[FigVideoCaptureConnectionConfiguration copyXPCEncoding];
-[FigVideoCaptureConnectionConfiguration description];
-[FigVideoCaptureConnectionConfiguration setAdditionalContentRotationDegrees:];
-[FigVideoCaptureConnectionConfiguration initWithXPCEncoding:];
-[FigVideoCaptureConnectionConfiguration outputWidth];
-[FigVideoCaptureConnectionConfiguration nonRotatedOutputDimensions];
-[FigVideoCaptureConnectionConfiguration lowLightVideoNoiseReductionEnabled];
-[FigVideoCaptureConnectionConfiguration stereoVideoCaptureEnabled];
-[FigVideoCaptureConnectionConfiguration coreMediaFaceTrackingEnabled];
-[FigVideoCaptureConnectionConfiguration setLivePhotoMetadataWritingEnabled:];
-[FigVideoCaptureConnectionConfiguration copyWithZone:];
-[FigVideoCaptureConnectionConfiguration setAttachMetadataToVideoBuffers:];
-[FigVideoCaptureConnectionConfiguration isEqual:];
-[FigVideoCaptureConnectionConfiguration setTimewarpDestinationFrameRate:];
-[FigVideoCaptureConnectionConfiguration depthDataTransform];
-[FigVideoCaptureConnectionConfiguration previewFilterRenderingEnabled];
-[FigVideoCaptureConnectionConfiguration outputFormat];
-[FigVideoCaptureConnectionConfiguration setLowLightVideoNoiseReductionEnabled:];
-[FigVideoCaptureConnectionConfiguration setTimewarpMode:];
-[FigVideoCaptureConnectionConfiguration previewDepthDataDeliveryEnabled];
```
