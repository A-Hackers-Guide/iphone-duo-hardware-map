# `BWStillImageCoordinatorRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
i _type;
@"FigCaptureStillImageSettings" _requestedSettings;
@"BWStillImageCaptureAssetBundle" _assetBundle;
B _shouldServiceBeforeGraphStop;
```

## Properties

```
@property (Ti,R,N,V_type) type;
@property (T@"FigCaptureStillImageSettings",R,N) requestedSettings;
@property (T@"BWStillImageCaptureAssetBundle",R,N,V_assetBundle) assetBundle;
@property (TB,N,V_shouldServiceBeforeGraphStop) shouldServiceBeforeGraphStop;
```

## Class methods

```
+[BWStillImageCoordinatorRequest requestWithRequestedSettings:];
```

## Instance methods

```
-[BWStillImageCoordinatorRequest dealloc];
-[BWStillImageCoordinatorRequest type];
-[BWStillImageCoordinatorRequest description];
-[BWStillImageCoordinatorRequest assetBundle];
-[BWStillImageCoordinatorRequest initCalibrationWithRequestedSettings:];
-[BWStillImageCoordinatorRequest initWithAssetBundle:];
-[BWStillImageCoordinatorRequest initWithRequestedSettings:];
-[BWStillImageCoordinatorRequest requestedSettings];
-[BWStillImageCoordinatorRequest setShouldServiceBeforeGraphStop:];
-[BWStillImageCoordinatorRequest shouldServiceBeforeGraphStop];
```
