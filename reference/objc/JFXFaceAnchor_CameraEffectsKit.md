# `JFXFaceAnchor`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 10 properties, 24 instance methods, 3 class methods

## Instance variables

```
d _focalLength;
q _preferredAnchorOrientation;
q _captureInterfaceOrientation;
{CGSize="width"d"height"d} _imageResolution;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _faceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _normalizedFaceRect;
{?="columns"[4]} _transform;
{?="columns"[4]} _cameraTransform;
```

## Properties

```
@property (T{?=[4]},N,V_transform) transform;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_faceRect) faceRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedFaceRect) normalizedFaceRect;
@property (Td,N,V_focalLength) focalLength;
@property (T,R,N) screenRelativePosition;
@property (Td,R,N) rollAngle;
@property (T{?=[4]},N,V_cameraTransform) cameraTransform;
@property (T{CGSize=dd},N,V_imageResolution) imageResolution;
@property (Tq,N,V_preferredAnchorOrientation) preferredAnchorOrientation;
@property (Tq,N,V_captureInterfaceOrientation) captureInterfaceOrientation;
```

## Class methods

```
+[JFXFaceAnchor supportsSecureCoding];
+[JFXFaceAnchor CFX_mirrorPoseTransformLeftRight:];
+[JFXFaceAnchor faceAnchorWithARFrame:captureInterfaceOrientation:withFaceRectScaleFactor:];
```

## Instance methods

```
-[JFXFaceAnchor focalLength];
-[JFXFaceAnchor debugDescription];
-[JFXFaceAnchor setFocalLength:];
-[JFXFaceAnchor setTransform:];
-[JFXFaceAnchor transform];
-[JFXFaceAnchor encodeWithCoder:];
-[JFXFaceAnchor rollAngle];
-[JFXFaceAnchor initWithCoder:];
-[JFXFaceAnchor copyWithZone:];
-[JFXFaceAnchor faceRect];
-[JFXFaceAnchor setFaceRect:];
-[JFXFaceAnchor normalizedFaceRect];
-[JFXFaceAnchor imageResolution];
-[JFXFaceAnchor setNormalizedFaceRect:];
-[JFXFaceAnchor setImageResolution:];
-[JFXFaceAnchor cameraTransform];
-[JFXFaceAnchor setCameraTransform:];
-[JFXFaceAnchor setCaptureInterfaceOrientation:];
-[JFXFaceAnchor captureInterfaceOrientation];
-[JFXFaceAnchor focalLengthForViewport:];
-[JFXFaceAnchor initWithTransform:forFaceRect:needsMirroring:withFaceRectScaleFactor:frameImageResolution:captureInterfaceOrientation:preferredAnchorOrientation:];
-[JFXFaceAnchor preferredAnchorOrientation];
-[JFXFaceAnchor screenRelativePosition];
-[JFXFaceAnchor setPreferredAnchorOrientation:];
```
