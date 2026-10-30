# `JFXARMetadata`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 9 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"ARFrame" _arFrame;
@"JFXFaceAnchor" _faceAnchor;
@"NSDictionary" _animojiPhysicsBlendShapes;
q _pvTransformOrientation;
{CGSize="width"d"height"d} _imageResolution;
{?="columns"[3]} _cameraIntrinsics;
{?="columns"[4]} _anchorTransform;
{?="columns"[4]} _cameraTransform;
```

## Properties

```
@property (T{?=[4]},R,N,V_cameraTransform) cameraTransform;
@property (T{?=[3]},R,N,V_cameraIntrinsics) cameraIntrinsics;
@property (Tq,R,N,V_pvTransformOrientation) pvTransformOrientation;
@property (T@"NSDictionary",C,N,V_animojiPhysicsBlendShapes) animojiPhysicsBlendShapes;
@property (T@"ARFrame",R,N,V_arFrame) arFrame;
@property (T@"JFXFaceAnchor",R,N,V_faceAnchor) faceAnchor;
@property (T{?=[4]},R,N,V_anchorTransform) anchorTransform;
@property (TB,R,N) hasTrackedFace;
@property (T{CGSize=dd},R,N,V_imageResolution) imageResolution;
```

## Class methods

```
+[JFXARMetadata supportsSecureCoding];
```

## Instance methods

```
-[JFXARMetadata encodeWithCoder:];
-[JFXARMetadata initWithCoder:];
-[JFXARMetadata copyWithZone:];
-[JFXARMetadata cameraIntrinsics];
-[JFXARMetadata imageResolution];
-[JFXARMetadata faceAnchor];
-[JFXARMetadata cameraTransform];
-[JFXARMetadata anchorTransform];
-[JFXARMetadata arFrame];
-[JFXARMetadata animojiPhysicsBlendShapes];
-[JFXARMetadata cameraProjectionForOutputSize:interfaceOrientation:zNear:zFar:];
-[JFXARMetadata cameraTransformForInterfaceOrientation:];
-[JFXARMetadata hasTrackedFace];
-[JFXARMetadata initWithARFrame:faceAnchor:];
-[JFXARMetadata initWithAnchorTransform:cameraTransform:cameraIntrinsics:cameraImageResolution:];
-[JFXARMetadata initWithFaceAnchor:cameraIntrinsics:];
-[JFXARMetadata pvTransformOrientation];
-[JFXARMetadata setAnimojiPhysicsBlendShapes:];
```
