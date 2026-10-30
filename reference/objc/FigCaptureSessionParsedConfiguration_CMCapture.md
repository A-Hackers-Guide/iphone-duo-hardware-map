# `FigCaptureSessionParsedConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 33 instance variables, 33 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _empty;
B _isMultiCamSession;
B _continuityCameraIsWired;
i _continuityCameraClientDeviceClass;
B _clientIsVOIP;
B _useOfflineVISPipeline;
B _smartStyleRenderingEnabled;
q _smartStyleControlMode;
@"FigCaptureSmartStyle" _smartStyle;
B _textureStyleEnabled;
@"FigCaptureTextureStyle" _textureStyle;
B _visualIntelligenceCameraEnabled;
B _isAudioOnlyRecordingSession;
@"NSArray" _connectionConfigurationsToBuild;
@"NSArray" _parsedCameraSourceConfigurations;
@"FigCaptureSessionParsedMicSourceConfiguration" _parsedMicSourceConfiguration;
@"NSArray" _metadataSourceConfigurations;
@"NSArray" _parsedPreviewSinkConfigurations;
@"NSArray" _videoThumbnailSinkConfigurations;
@"NSArray" _parsedStillImageSinkConfigurations;
@"NSArray" _parsedVideoDataSinkConfigurations;
@"NSArray" _parsedVisionDataSinkConfigurations;
@"NSArray" _parsedDepthDataSinkConfigurations;
@"NSArray" _parsedMetadataSinkConfigurations;
@"NSArray" _parsedMovieFileSinkConfigurations;
@"NSArray" _audioFileSinkConnectionConfigurations;
@"NSArray" _audioDataSinkConnectionConfigurations;
@"NSArray" _pointCloudDataSinkConnectionConfigurations;
@"NSArray" _cameraCalibrationDataSinkConnectionConfigurations;
@"NSArray" _parsedLiDARDepthPipelineConfigurations;
@"NSArray" _parsedSecureVideoDataSinkConfigurations;
@"NSArray" _parsedBroadcastVideoSinkConfigurations;
@"NSArray" _parsedCinematographyConfigurations;
```

## Properties

```
@property (TB,R,N,V_empty) empty;
@property (TB,R,N,GisMultiCamSession,V_isMultiCamSession) multiCamSession;
@property (TB,R,N,V_continuityCameraIsWired) continuityCameraIsWired;
@property (Ti,R,N,V_continuityCameraClientDeviceClass) continuityCameraClientDeviceClass;
@property (TB,R,N,V_clientIsVOIP) clientIsVOIP;
@property (TB,R,N,V_useOfflineVISPipeline) useOfflineVISPipeline;
@property (TB,R,N,V_smartStyleRenderingEnabled) smartStyleRenderingEnabled;
@property (Tq,R,N,V_smartStyleControlMode) smartStyleControlMode;
@property (T@"FigCaptureSmartStyle",R,N,V_smartStyle) smartStyle;
@property (TB,R,N,V_textureStyleEnabled) textureStyleEnabled;
@property (T@"FigCaptureTextureStyle",R,N,V_textureStyle) textureStyle;
@property (TB,R,N,GisVisualIntelligenceCameraEnabled,V_visualIntelligenceCameraEnabled) visualIntelligenceCameraEnabled;
@property (TB,R,N,GisAudioOnlyRecordingSession,V_isAudioOnlyRecordingSession) audioOnlyRecordingSession;
@property (T@"NSArray",R,N,V_connectionConfigurationsToBuild) connectionConfigurationsToBuild;
@property (T@"NSArray",R,N,V_parsedCameraSourceConfigurations) parsedCameraSourceConfigurations;
@property (T@"FigCaptureSessionParsedMicSourceConfiguration",R,N,V_parsedMicSourceConfiguration) parsedMicSourceConfiguration;
@property (T@"NSArray",R,N,V_metadataSourceConfigurations) metadataSourceConfigurations;
@property (T@"NSArray",R,N,V_parsedPreviewSinkConfigurations) parsedPreviewSinkConfigurations;
@property (T@"NSArray",R,N,V_videoThumbnailSinkConfigurations) videoThumbnailSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedStillImageSinkConfigurations) parsedStillImageSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedVideoDataSinkConfigurations) parsedVideoDataSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedVisionDataSinkConfigurations) parsedVisionDataSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedDepthDataSinkConfigurations) parsedDepthDataSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedMetadataSinkConfigurations) parsedMetadataSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedMovieFileSinkConfigurations) parsedMovieFileSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedSecureVideoDataSinkConfigurations) parsedSecureVideoDataSinkConfigurations;
@property (T@"NSArray",R,N,V_parsedBroadcastVideoSinkConfigurations) parsedBroadcastVideoSinkConfigurations;
@property (T@"NSArray",R,N,V_audioFileSinkConnectionConfigurations) audioFileSinkConnectionConfigurations;
@property (T@"NSArray",R,N,V_audioDataSinkConnectionConfigurations) audioDataSinkConnectionConfigurations;
@property (T@"NSArray",R,N,V_pointCloudDataSinkConnectionConfigurations) pointCloudDataSinkConnectionConfigurations;
@property (T@"NSArray",R,N,V_cameraCalibrationDataSinkConnectionConfigurations) cameraCalibrationDataSinkConnectionConfigurations;
@property (T@"NSArray",R,N,V_parsedCinematographyConfigurations) parsedCinematographyConfigurations;
@property (T@"NSArray",R,N,V_parsedLiDARDepthPipelineConfigurations) parsedLiDARDepthPipelineConfigurations;
```

## Class methods

```
+[FigCaptureSessionParsedConfiguration initialize];
```

## Instance methods

```
-[FigCaptureSessionParsedConfiguration empty];
-[FigCaptureSessionParsedConfiguration continuityCameraIsWired];
-[FigCaptureSessionParsedConfiguration clientIsVOIP];
-[FigCaptureSessionParsedConfiguration parsedMovieFileSinkConfigurations];
-[FigCaptureSessionParsedConfiguration isMultiCamSession];
-[FigCaptureSessionParsedConfiguration smartStyleRenderingEnabled];
-[FigCaptureSessionParsedConfiguration parsedLiDARDepthPipelineConfigurations];
-[FigCaptureSessionParsedConfiguration parsedMetadataSinkConfigurations];
-[FigCaptureSessionParsedConfiguration textureStyle];
-[FigCaptureSessionParsedConfiguration smartStyle];
-[FigCaptureSessionParsedConfiguration audioDataSinkConnectionConfigurations];
-[FigCaptureSessionParsedConfiguration smartStyleControlMode];
-[FigCaptureSessionParsedConfiguration cameraCalibrationDataSinkConnectionConfigurations];
-[FigCaptureSessionParsedConfiguration parsedPreviewSinkConfigurations];
-[FigCaptureSessionParsedConfiguration dealloc];
-[FigCaptureSessionParsedConfiguration pointCloudDataSinkConnectionConfigurations];
-[FigCaptureSessionParsedConfiguration useOfflineVISPipeline];
-[FigCaptureSessionParsedConfiguration videoThumbnailSinkConfigurations];
-[FigCaptureSessionParsedConfiguration parsedSecureVideoDataSinkConfigurations];
-[FigCaptureSessionParsedConfiguration connectionConfigurationsToBuild];
-[FigCaptureSessionParsedConfiguration textureStyleEnabled];
-[FigCaptureSessionParsedConfiguration isAudioOnlyRecordingSession];
-[FigCaptureSessionParsedConfiguration parsedStillImageSinkConfigurations];
-[FigCaptureSessionParsedConfiguration continuityCameraClientDeviceClass];
-[FigCaptureSessionParsedConfiguration audioFileSinkConnectionConfigurations];
-[FigCaptureSessionParsedConfiguration parsedVideoDataSinkConfigurations];
-[FigCaptureSessionParsedConfiguration parsedMicSourceConfiguration];
-[FigCaptureSessionParsedConfiguration metadataSourceConfigurations];
-[FigCaptureSessionParsedConfiguration parsedCinematographyConfigurations];
-[FigCaptureSessionParsedConfiguration parsedBroadcastVideoSinkConfigurations];
-[FigCaptureSessionParsedConfiguration parsedVisionDataSinkConfigurations];
-[FigCaptureSessionParsedConfiguration isVisualIntelligenceCameraEnabled];
-[FigCaptureSessionParsedConfiguration parsedCameraSourceConfigurations];
-[FigCaptureSessionParsedConfiguration initWithSessionConfiguration:clientSetsUserInitiatedCaptureRequestTime:restrictions:];
-[FigCaptureSessionParsedConfiguration parsedDepthDataSinkConfigurations];
```
