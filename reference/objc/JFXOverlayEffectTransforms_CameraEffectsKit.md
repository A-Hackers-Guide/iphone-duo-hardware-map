# `JFXOverlayEffectTransforms`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXTextEffectTransforms`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"PVTransformAnimation" _transformAnimation;
@"JFXFaceTrackedEffectTransform" _faceTrackingTransform;
```

## Properties

```
@property (T@"PVTransformAnimation",C,N,V_transformAnimation) transformAnimation;
@property (T@"JFXFaceTrackedEffectTransform",C,N,V_faceTrackingTransform) faceTrackingTransform;
```

## Class methods

```
+[JFXOverlayEffectTransforms transformsWithEffect:];
+[JFXOverlayEffectTransforms transformsWithTransform:transformAnimation:faceTrackingTransform:];
```

## Instance methods

```
-[JFXOverlayEffectTransforms initWithEffect:];
-[JFXOverlayEffectTransforms transformAnimation];
-[JFXOverlayEffectTransforms applyToEffect:];
-[JFXOverlayEffectTransforms faceTrackingTransform];
-[JFXOverlayEffectTransforms initWithTransform:transformAnimation:faceTrackingTransform:];
-[JFXOverlayEffectTransforms setFaceTrackingTransform:];
-[JFXOverlayEffectTransforms setTransformAnimation:];
```
