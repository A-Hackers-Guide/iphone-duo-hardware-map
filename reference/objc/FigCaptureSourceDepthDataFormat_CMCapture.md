# `FigCaptureSourceDepthDataFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSourceFormat`
- 0 instance variables, 5 properties, 13 instance methods, 0 class methods

## Properties

```
@property (Tf,R) fieldOfView;
@property (Tf,R) sensorOrientation;
@property (TB,R) isPrivate;
@property (T{?=ii},R) streamingNetworkDimensions;
@property (T{?=ii},R) stillNetworkDimensions;
```

## Instance methods

```
-[FigCaptureSourceDepthDataFormat isPrivate];
-[FigCaptureSourceDepthDataFormat copyWithNewPixelFormat:];
-[FigCaptureSourceDepthDataFormat depthEngineOutputDimensions];
-[FigCaptureSourceDepthDataFormat isStillImageOnlyDepthData];
-[FigCaptureSourceDepthDataFormat highResStillImageDimensions];
-[FigCaptureSourceDepthDataFormat gainMapSupported];
-[FigCaptureSourceDepthDataFormat streamingNetworkDimensions];
-[FigCaptureSourceDepthDataFormat RGBIRStereoFusionSupported];
-[FigCaptureSourceDepthDataFormat sensorOrientation];
-[FigCaptureSourceDepthDataFormat isStreamingOnlyDepthData];
-[FigCaptureSourceDepthDataFormat mediaType];
-[FigCaptureSourceDepthDataFormat fieldOfView];
-[FigCaptureSourceDepthDataFormat stillNetworkDimensions];
```
