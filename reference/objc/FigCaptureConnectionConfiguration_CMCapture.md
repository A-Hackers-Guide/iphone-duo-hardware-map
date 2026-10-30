# `FigCaptureConnectionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSCopying`
- 6 instance variables, 22 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSString" _connectionID;
I _mediaType;
i _underlyingDeviceType;
@"FigCaptureSourceConfiguration" _sourceConfiguration;
@"FigCaptureSinkConfiguration" _sinkConfiguration;
B _enabled;
```

## Properties

```
@property (TB,R) smartCameraRequired;
@property (T@"NSString",C,N,V_connectionID) connectionID;
@property (TI,N,V_mediaType) mediaType;
@property (Ti,N,V_underlyingDeviceType) underlyingDeviceType;
@property (T@"FigCaptureSourceConfiguration",&,N,V_sourceConfiguration) sourceConfiguration;
@property (T@"FigCaptureSinkConfiguration",&,N,V_sinkConfiguration) sinkConfiguration;
@property (TB,N,V_enabled) enabled;
@property (T@"FigCaptureIrisSinkConfiguration",R) irisSinkConfiguration;
@property (T@"FigCaptureStillImageSinkConfiguration",R) stillImageSinkConfiguration;
@property (T@"FigCaptureVideoDataSinkConfiguration",R) videoDataSinkConfiguration;
@property (T@"FigCaptureSecureVideoDataSinkConfiguration",R) secureVideoDataSinkConfiguration;
@property (T@"FigCaptureVideoPreviewSinkConfiguration",R) videoPreviewSinkConfiguration;
@property (T@"FigCaptureDepthDataSinkConfiguration",R) depthDataSinkConfiguration;
@property (T@"FigCaptureVideoThumbnailSinkConfiguration",R) thumbnailSinkConfiguration;
@property (T@"FigCapturePointCloudDataSinkConfiguration",R) pointCloudDataSinkConfiguration;
@property (T@"FigCaptureCameraCalibrationDataSinkConfiguration",R) cameraCalibrationDataSinkConfiguration;
@property (T@"FigCaptureMovieFileSinkConfiguration",R) movieFileSinkConfiguration;
@property (T@"FigCaptureInternalSinkConfiguration",R) internalSinkConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigCaptureConnectionConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureConnectionConfiguration enabled];
-[FigCaptureConnectionConfiguration init];
-[FigCaptureConnectionConfiguration dealloc];
-[FigCaptureConnectionConfiguration setMediaType:];
-[FigCaptureConnectionConfiguration setEnabled:];
-[FigCaptureConnectionConfiguration copyXPCEncoding];
-[FigCaptureConnectionConfiguration initWithXPCEncoding:];
-[FigCaptureConnectionConfiguration connectionID];
-[FigCaptureConnectionConfiguration copyWithZone:];
-[FigCaptureConnectionConfiguration mediaType];
-[FigCaptureConnectionConfiguration isEqual:];
-[FigCaptureConnectionConfiguration setConnectionID:];
-[FigCaptureConnectionConfiguration setSinkConfiguration:];
-[FigCaptureConnectionConfiguration setSourceConfiguration:];
-[FigCaptureConnectionConfiguration setUnderlyingDeviceType:];
-[FigCaptureConnectionConfiguration sinkConfiguration];
-[FigCaptureConnectionConfiguration sourceConfiguration];
-[FigCaptureConnectionConfiguration pointCloudDataSinkConfiguration];
-[FigCaptureConnectionConfiguration cameraCalibrationDataSinkConfiguration];
-[FigCaptureConnectionConfiguration depthDataSinkConfiguration];
-[FigCaptureConnectionConfiguration internalSinkConfiguration];
-[FigCaptureConnectionConfiguration irisSinkConfiguration];
-[FigCaptureConnectionConfiguration movieFileSinkConfiguration];
-[FigCaptureConnectionConfiguration secureVideoDataSinkConfiguration];
-[FigCaptureConnectionConfiguration smartCameraRequired];
-[FigCaptureConnectionConfiguration sourcesFromUnderlyingStream];
-[FigCaptureConnectionConfiguration stillImageSinkConfiguration];
-[FigCaptureConnectionConfiguration thumbnailSinkConfiguration];
-[FigCaptureConnectionConfiguration underlyingDeviceType];
-[FigCaptureConnectionConfiguration videoDataSinkConfiguration];
-[FigCaptureConnectionConfiguration videoPreviewSinkConfiguration];
```
