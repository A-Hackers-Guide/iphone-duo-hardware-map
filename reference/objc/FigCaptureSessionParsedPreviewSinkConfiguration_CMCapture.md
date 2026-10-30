# `FigCaptureSessionParsedPreviewSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"FigVideoCaptureConnectionConfiguration" _videoPreviewSinkConnectionConfiguration;
@"NSArray" _secondaryVideoPreviewSinkConnectionConfigurations;
B _isSecondaryPreviewSink;
@"FigVideoCaptureConnectionConfiguration" _videoThumbnailConnectionConfiguration;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _previewTimeMachineConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sceneClassifierConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _previewSmartStyleCoefficientsTimeMachineConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sensitiveContentAnalyzerConnectionConfiguration;
@"FigMetadataObjectCaptureConnectionConfiguration" _metadataObjectConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _stillImageConnectionConfiguration;
@"FigCaptureSourceConfiguration" _cameraConfiguration;
i _sourceDeviceType;
```

## Properties

```
@property (T@"NSString",R,N) sinkID;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_videoPreviewSinkConnectionConfiguration) videoPreviewSinkConnectionConfiguration;
@property (T@"NSArray",R,N,V_secondaryVideoPreviewSinkConnectionConfigurations) secondaryVideoPreviewSinkConnectionConfigurations;
@property (TB,R,N,V_isSecondaryPreviewSink) isSecondaryPreviewSink;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_videoThumbnailConnectionConfiguration) videoThumbnailConnectionConfiguration;
@property (T@"FigDepthDataCaptureConnectionConfiguration",R,N,V_depthDataConnectionConfiguration) depthDataConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_previewSmartStyleCoefficientsTimeMachineConnectionConfiguration) previewSmartStyleCoefficientsTimeMachineConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_previewTimeMachineConnectionConfiguration) previewTimeMachineConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_sceneClassifierConnectionConfiguration) sceneClassifierConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_sensitiveContentAnalyzerConnectionConfiguration) sensitiveContentAnalyzerConnectionConfiguration;
@property (T@"FigMetadataObjectCaptureConnectionConfiguration",R,N,V_metadataObjectConnectionConfiguration) metadataObjectConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_stillImageConnectionConfiguration) stillImageConnectionConfiguration;
@property (T@"FigCaptureSourceConfiguration",R,N,V_cameraConfiguration) cameraConfiguration;
@property (Ti,R,N,V_sourceDeviceType) sourceDeviceType;
```

## Instance methods

```
-[FigCaptureSessionParsedPreviewSinkConfiguration sensitiveContentAnalyzerConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration secondaryVideoPreviewSinkConnectionConfigurations];
-[FigCaptureSessionParsedPreviewSinkConfiguration isSecondaryPreviewSink];
-[FigCaptureSessionParsedPreviewSinkConfiguration dealloc];
-[FigCaptureSessionParsedPreviewSinkConfiguration sourceDeviceType];
-[FigCaptureSessionParsedPreviewSinkConfiguration previewSmartStyleCoefficientsTimeMachineConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration sceneClassifierConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration videoPreviewSinkConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration previewTimeMachineConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration stillImageConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration videoThumbnailConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration sinkID];
-[FigCaptureSessionParsedPreviewSinkConfiguration metadataObjectConnectionConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration cameraConfiguration];
-[FigCaptureSessionParsedPreviewSinkConfiguration depthDataConnectionConfiguration];
```
