# `JFXExternalImageData`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _hasValidFaceData;
B _requiresFaceTracking;
d _timestamp;
^{__CVBuffer=} _pixelBuffer;
q _cameraPosition;
q _captureFramesPerSecond;
q _orientation;
d _rollAngle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _normalizedFaceRect;
{?="columns"[3]} _cameraIntrinsics;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (T{?=[3]},N,V_cameraIntrinsics) cameraIntrinsics;
@property (T^{__CVBuffer=},N,V_pixelBuffer) pixelBuffer;
@property (Tq,N,V_cameraPosition) cameraPosition;
@property (Tq,N,V_captureFramesPerSecond) captureFramesPerSecond;
@property (Tq,N,V_orientation) orientation;
@property (TB,N,V_hasValidFaceData) hasValidFaceData;
@property (TB,N,V_requiresFaceTracking) requiresFaceTracking;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedFaceRect) normalizedFaceRect;
@property (Td,N,V_rollAngle) rollAngle;
```

## Instance methods

```
-[JFXExternalImageData setOrientation:];
-[JFXExternalImageData pixelBuffer];
-[JFXExternalImageData setTimestamp:];
-[JFXExternalImageData setRollAngle:];
-[JFXExternalImageData orientation];
-[JFXExternalImageData dealloc];
-[JFXExternalImageData timestamp];
-[JFXExternalImageData rollAngle];
-[JFXExternalImageData setPixelBuffer:];
-[JFXExternalImageData normalizedFaceRect];
-[JFXExternalImageData cameraIntrinsics];
-[JFXExternalImageData setCameraIntrinsics:];
-[JFXExternalImageData setNormalizedFaceRect:];
-[JFXExternalImageData cameraPosition];
-[JFXExternalImageData setCameraPosition:];
-[JFXExternalImageData captureFramesPerSecond];
-[JFXExternalImageData hasValidFaceData];
-[JFXExternalImageData requiresFaceTracking];
-[JFXExternalImageData setCaptureFramesPerSecond:];
-[JFXExternalImageData setHasValidFaceData:];
-[JFXExternalImageData setRequiresFaceTracking:];
```
