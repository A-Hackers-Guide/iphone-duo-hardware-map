# `FigCaptureSessionParsedMovieFileSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _videoConnectionConfigurations;
@"FigAudioCaptureConnectionConfiguration" _audioConnectionConfiguration;
@"FigMetadataItemCaptureConnectionConfiguration" _cameraDebugInfoMetadataConnectionConfiguration;
@"NSArray" _detectedObjectMetadataConnectionConfigurations;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _stillImageConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sceneClassifierConnectionConfiguration;
```

## Properties

```
@property (T@"FigVideoCaptureConnectionConfiguration",R,N) primaryVideoConnectionConfiguration;
@property (T@"NSArray",R,N,V_videoConnectionConfigurations) videoConnectionConfigurations;
@property (T@"FigAudioCaptureConnectionConfiguration",R,N,V_audioConnectionConfiguration) audioConnectionConfiguration;
@property (T@"FigMetadataItemCaptureConnectionConfiguration",R,N,V_cameraDebugInfoMetadataConnectionConfiguration) cameraDebugInfoMetadataConnectionConfiguration;
@property (T@"NSArray",R,N,V_detectedObjectMetadataConnectionConfigurations) detectedObjectMetadataConnectionConfigurations;
@property (T@"FigDepthDataCaptureConnectionConfiguration",R,N,V_depthDataConnectionConfiguration) depthDataConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_stillImageConnectionConfiguration) stillImageConnectionConfiguration;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_sceneClassifierConnectionConfiguration) sceneClassifierConnectionConfiguration;
```

## Instance methods

```
-[FigCaptureSessionParsedMovieFileSinkConfiguration dealloc];
-[FigCaptureSessionParsedMovieFileSinkConfiguration sceneClassifierConnectionConfiguration];
-[FigCaptureSessionParsedMovieFileSinkConfiguration stillImageConnectionConfiguration];
-[FigCaptureSessionParsedMovieFileSinkConfiguration depthDataConnectionConfiguration];
-[FigCaptureSessionParsedMovieFileSinkConfiguration audioConnectionConfiguration];
-[FigCaptureSessionParsedMovieFileSinkConfiguration cameraDebugInfoMetadataConnectionConfiguration];
-[FigCaptureSessionParsedMovieFileSinkConfiguration detectedObjectMetadataConnectionConfigurations];
-[FigCaptureSessionParsedMovieFileSinkConfiguration primaryVideoConnectionConfiguration];
-[FigCaptureSessionParsedMovieFileSinkConfiguration videoConnectionConfigurations];
```
