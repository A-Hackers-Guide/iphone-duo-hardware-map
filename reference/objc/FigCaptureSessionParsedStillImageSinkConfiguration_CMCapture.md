# `FigCaptureSessionParsedStillImageSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _stillImageConnectionConfigurations;
@"FigVideoCaptureConnectionConfiguration" _movieFileVideoConnectionConfiguration;
@"FigPointCloudDataCaptureConnectionConfiguration" _pointCloudDataConnectionConfiguration;
```

## Properties

```
@property (T@"FigVideoCaptureConnectionConfiguration",R,N) primaryStillImageConnectionConfiguration;
@property (T@"NSArray",R,N,V_stillImageConnectionConfigurations) stillImageConnectionConfigurations;
@property (T@"FigVideoCaptureConnectionConfiguration",R,N,V_movieFileVideoConnectionConfiguration) movieFileVideoConnectionConfiguration;
@property (T@"FigPointCloudDataCaptureConnectionConfiguration",R,N,V_pointCloudDataConnectionConfiguration) pointCloudDataConnectionConfiguration;
```

## Instance methods

```
-[FigCaptureSessionParsedStillImageSinkConfiguration dealloc];
-[FigCaptureSessionParsedStillImageSinkConfiguration movieFileVideoConnectionConfiguration];
-[FigCaptureSessionParsedStillImageSinkConfiguration pointCloudDataConnectionConfiguration];
-[FigCaptureSessionParsedStillImageSinkConfiguration primaryStillImageConnectionConfiguration];
-[FigCaptureSessionParsedStillImageSinkConfiguration stillImageConnectionConfigurations];
```
