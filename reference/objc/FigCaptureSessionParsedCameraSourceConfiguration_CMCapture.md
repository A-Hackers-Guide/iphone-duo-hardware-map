# `FigCaptureSessionParsedCameraSourceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureSourceConfiguration" _cameraConfiguration;
@"NSArray" _connectionConfigurations;
@"FigVideoCaptureConnectionConfiguration" _videoPreviewSinkConnectionConfiguration;
@"NSArray" _previewDerivedConnectionConfigurations;
@"NSArray" _videoCaptureConnectionConfigurations;
@"NSArray" _videoDataConnectionConfigurations;
@"FigVideoCaptureConnectionConfiguration" _stillImageConnectionConfiguration;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
@"NSArray" _visionDataConnectionConfigurations;
@"NSArray" _metadataObjectConnectionConfigurations;
@"NSArray" _movieFileDetectedObjectMetadataConnectionConfigurations;
@"NSArray" _pointCloudDataConnectionConfigurations;
@"NSArray" _cameraCalibrationDataConnectionConfigurations;
@"NSArray" _secureVideoCaptureConnectionConfigurations;
i _multiCamClientCompositingPrimaryCameraVideoStabilizationStrength;
B _cinematicVideoMetadataDeliveryEnabled;
```

## Properties

```
@property (Ti,N,V_multiCamClientCompositingPrimaryCameraVideoStabilizationStrength) multiCamClientCompositingPrimaryCameraVideoStabilizationStrength;
@property (T@"FigCaptureSourceConfiguration",R,N,V_cameraConfiguration) cameraConfiguration;
@property (T@"NSArray",R,N,V_connectionConfigurations) connectionConfigurations;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_videoPreviewSinkConnectionConfiguration) videoPreviewSinkConnectionConfiguration;
@property (T@"NSArray",R,N,V_previewDerivedConnectionConfigurations) previewDerivedConnectionConfigurations;
@property (T@"NSArray",R,N,V_videoCaptureConnectionConfigurations) videoCaptureConnectionConfigurations;
@property (T@"NSArray",R,N,V_videoDataConnectionConfigurations) videoDataConnectionConfigurations;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_stillImageConnectionConfiguration) stillImageConnectionConfiguration;
@property (T@"FigDepthDataCaptureConnectionConfiguration",R,N,V_depthDataConnectionConfiguration) depthDataConnectionConfiguration;
@property (T@"NSArray",R,N,V_visionDataConnectionConfigurations) visionDataConnectionConfigurations;
@property (T@"NSArray",R,N,V_metadataObjectConnectionConfigurations) metadataObjectConnectionConfigurations;
@property (T@"NSArray",R,N,V_movieFileDetectedObjectMetadataConnectionConfigurations) movieFileDetectedObjectMetadataConnectionConfigurations;
@property (T@"NSArray",R,N,V_pointCloudDataConnectionConfigurations) pointCloudDataConnectionConfigurations;
@property (T@"NSArray",R,N,V_cameraCalibrationDataConnectionConfigurations) cameraCalibrationDataConnectionConfigurations;
@property (T@"NSArray",R,N,V_secureVideoCaptureConnectionConfigurations) secureVideoConnectionConfigurations;
@property (TB,R,N,V_cinematicVideoMetadataDeliveryEnabled) cinematicVideoMetadataDeliveryEnabled;
```

## Instance methods

```
-[FigCaptureSessionParsedCameraSourceConfiguration previewDerivedConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration videoCaptureConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration multiCamClientCompositingPrimaryCameraVideoStabilizationStrength];
-[FigCaptureSessionParsedCameraSourceConfiguration pointCloudDataConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration secureVideoConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration dealloc];
-[FigCaptureSessionParsedCameraSourceConfiguration setMultiCamClientCompositingPrimaryCameraVideoStabilizationStrength:];
-[FigCaptureSessionParsedCameraSourceConfiguration visionDataConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration cameraCalibrationDataConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration cinematicVideoMetadataDeliveryEnabled];
-[FigCaptureSessionParsedCameraSourceConfiguration connectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration metadataObjectConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration videoPreviewSinkConnectionConfiguration];
-[FigCaptureSessionParsedCameraSourceConfiguration stillImageConnectionConfiguration];
-[FigCaptureSessionParsedCameraSourceConfiguration videoDataConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration movieFileDetectedObjectMetadataConnectionConfigurations];
-[FigCaptureSessionParsedCameraSourceConfiguration cameraConfiguration];
-[FigCaptureSessionParsedCameraSourceConfiguration depthDataConnectionConfiguration];
```
