# `BWStillImageCaptureAssetBundle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureStillImageSettings" _requestedSettings;
@"NSArray" _assets;
Q _stillImageSceneFlags;
B _stillImageSceneFlagsValid;
@"BWFrameStatisticsByPortType" _frameStatisticsByPortType;
@"BWStillImageCaptureMetadata" _stillImageCaptureMetadata;
```

## Properties

```
@property (T@"FigCaptureStillImageSettings",R,N,V_requestedSettings) requestedSettings;
@property (T@"NSArray",R,N,V_assets) assets;
@property (TQ,R,N,V_stillImageSceneFlags) stillImageSceneFlags;
@property (TB,R,N,V_stillImageSceneFlagsValid) stillImageSceneFlagsValid;
@property (T@"BWFrameStatisticsByPortType",&,N,V_frameStatisticsByPortType) frameStatisticsByPortType;
@property (T@"BWStillImageCaptureMetadata",&,N,V_stillImageCaptureMetadata) stillImageCaptureMetadata;
@property (TB,R,N) containsSIFRFrame;
```

## Instance methods

```
-[BWStillImageCaptureAssetBundle dealloc];
-[BWStillImageCaptureAssetBundle assets];
-[BWStillImageCaptureAssetBundle description];
-[BWStillImageCaptureAssetBundle frameStatisticsByPortType];
-[BWStillImageCaptureAssetBundle addStillImageSceneFlags:];
-[BWStillImageCaptureAssetBundle containsSIFRFrame];
-[BWStillImageCaptureAssetBundle initWithRequestedSettings:sampleBuffers:];
-[BWStillImageCaptureAssetBundle requestedSettings];
-[BWStillImageCaptureAssetBundle setFrameStatisticsByPortType:];
-[BWStillImageCaptureAssetBundle setStillImageCaptureMetadata:];
-[BWStillImageCaptureAssetBundle stillImageCaptureMetadata];
-[BWStillImageCaptureAssetBundle stillImageSceneFlags];
-[BWStillImageCaptureAssetBundle stillImageSceneFlagsValid];
```
