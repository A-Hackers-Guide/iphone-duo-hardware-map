# `FigCaptureStillImageSinkPipelineSessionStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 20 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _stillImageSinkPipelines;
@"FigCaptureSinkPipeline<FigCaptureStillImageSinkPipeline>" _primaryStillImageSinkPipeline;
@"NSArray" _cameraSourcePipelines;
@"BWImageQueueSinkNode" _previewSinkNode;
@"FigCapturePixelConverter" _pixelConverter;
@"NSDictionary" _colorInfo;
B _stillImagesAreOptimizedForOfflineVideoStabilization;
f _videoStabilizationOverscanCropMultiplier;
@"NSArray" _stillImageConnectionConfigurations;
^{opaqueCMFormatDescription=} _stillImageFormatDescription;
^{opaqueCMFormatDescription=} _previewFormatDescription;
^{opaqueCMFormatDescription=} _rawFormatDescription;
@"NSArray" _rawDNGColorCalibrations;
@"FigCaptureSessionPreparedBracket" _preparedBracket;
Q _currentUserInitiatedRequestHostTime;
{?="value"q"timescale"i"flags"I"epoch"q} _currentUserInitiatedRequestPTS;
q _mostRecentBurstSettingsID;
B _videoStabilizationOverscanCropEnabled;
```

## Properties

```
@property (T@"NSArray",R,N,V_stillImageSinkPipelines) stillImageSinkPipelines;
@property (T@"FigCaptureSinkPipeline<FigCaptureStillImageSinkPipeline>",R,N,V_primaryStillImageSinkPipeline) primaryStillImageSinkPipeline;
@property (T@"NSArray",R,N,V_stillImageConnectionConfigurations) stillImageConnectionConfigurations;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N) primaryStillImageConnectionConfiguration;
@property (T@"NSArray",R,N,V_cameraSourcePipelines) cameraSourcePipelines;
@property (T@"FigCaptureCameraSourcePipeline",R,N) primaryCameraSourcePipeline;
@property (T@"BWImageQueueSinkNode",R,N,V_previewSinkNode) previewSinkNode;
@property (T@"FigCapturePixelConverter",R,N,V_pixelConverter) pixelConverter;
@property (T@"NSDictionary",R,N,V_colorInfo) colorInfo;
@property (TB,R,N,V_stillImagesAreOptimizedForOfflineVideoStabilization) stillImagesAreOptimizedForOfflineVideoStabilization;
@property (Tf,N,V_videoStabilizationOverscanCropMultiplier) videoStabilizationOverscanCropMultiplier;
@property (Tr^^{opaqueCMFormatDescription},R,N) stillImageFormatDescriptionPtr;
@property (Tr^^{opaqueCMFormatDescription},R,N) previewFormatDescriptionPtr;
@property (Tr^^{opaqueCMFormatDescription},R,N) rawFormatDescriptionPtr;
@property (T@"FigCaptureSessionPreparedBracket",R,N) preparedBracket;
@property (T@"NSArray",&,N,V_rawDNGColorCalibrations) rawDNGColorCalibrations;
@property (TQ,N,V_currentUserInitiatedRequestHostTime) currentUserInitiatedRequestHostTime;
@property (T{?=qiIq},N,V_currentUserInitiatedRequestPTS) currentUserInitiatedRequestPTS;
@property (Tq,N,V_mostRecentBurstSettingsID) mostRecentBurstSettingsID;
@property (TB,N,V_videoStabilizationOverscanCropEnabled) videoStabilizationOverscanCropEnabled;
```

## Instance methods

```
-[FigCaptureStillImageSinkPipelineSessionStorage dealloc];
-[FigCaptureStillImageSinkPipelineSessionStorage cameraSourcePipelines];
-[FigCaptureStillImageSinkPipelineSessionStorage videoStabilizationOverscanCropMultiplier];
-[FigCaptureStillImageSinkPipelineSessionStorage colorInfo];
-[FigCaptureStillImageSinkPipelineSessionStorage setVideoStabilizationOverscanCropMultiplier:];
-[FigCaptureStillImageSinkPipelineSessionStorage preparedBracket];
-[FigCaptureStillImageSinkPipelineSessionStorage previewSinkNode];
-[FigCaptureStillImageSinkPipelineSessionStorage cameraSourcePipelineForStillImageSinkPipeline:];
-[FigCaptureStillImageSinkPipelineSessionStorage currentUserInitiatedRequestHostTime];
-[FigCaptureStillImageSinkPipelineSessionStorage currentUserInitiatedRequestPTS];
-[FigCaptureStillImageSinkPipelineSessionStorage initWithStillImageSinkPipelines:cameraSourcePipelines:previewSinkNode:pixelConverter:colorInfo:stillImagesAreOptimizedForOfflineVideoStabilization:videoStabilizationOverscanCropMultiplier:preparedBracket:stillImageConnectionConfigurations:];
-[FigCaptureStillImageSinkPipelineSessionStorage mostRecentBurstSettingsID];
-[FigCaptureStillImageSinkPipelineSessionStorage pixelConverter];
-[FigCaptureStillImageSinkPipelineSessionStorage previewFormatDescriptionPtr];
-[FigCaptureStillImageSinkPipelineSessionStorage primaryCameraSourcePipeline];
-[FigCaptureStillImageSinkPipelineSessionStorage primaryStillImageConnectionConfiguration];
-[FigCaptureStillImageSinkPipelineSessionStorage primaryStillImageSinkPipeline];
-[FigCaptureStillImageSinkPipelineSessionStorage rawDNGColorCalibrations];
-[FigCaptureStillImageSinkPipelineSessionStorage rawFormatDescriptionPtr];
-[FigCaptureStillImageSinkPipelineSessionStorage setCurrentUserInitiatedRequestHostTime:];
-[FigCaptureStillImageSinkPipelineSessionStorage setCurrentUserInitiatedRequestPTS:];
-[FigCaptureStillImageSinkPipelineSessionStorage setMostRecentBurstSettingsID:];
-[FigCaptureStillImageSinkPipelineSessionStorage setRawDNGColorCalibrations:];
-[FigCaptureStillImageSinkPipelineSessionStorage setVideoStabilizationOverscanCropEnabled:];
-[FigCaptureStillImageSinkPipelineSessionStorage stillImageConnectionConfigurationForStillImageSinkPipeline:];
-[FigCaptureStillImageSinkPipelineSessionStorage stillImageConnectionConfigurations];
-[FigCaptureStillImageSinkPipelineSessionStorage stillImageFormatDescriptionPtr];
-[FigCaptureStillImageSinkPipelineSessionStorage stillImageSinkPipelineWithStillImageCoordinator:];
-[FigCaptureStillImageSinkPipelineSessionStorage stillImageSinkPipelines];
-[FigCaptureStillImageSinkPipelineSessionStorage stillImagesAreOptimizedForOfflineVideoStabilization];
-[FigCaptureStillImageSinkPipelineSessionStorage videoStabilizationOverscanCropEnabled];
```
