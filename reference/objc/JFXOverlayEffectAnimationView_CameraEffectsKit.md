# `JFXOverlayEffectAnimationView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"JFXOverlayEffectFrame" _fromEffectFrame;
@"JFXOverlayEffectFrame" _toEffectFrame;
@"JFXEffectAnimationDelegate" _animationDelegate;
@"CALayer" _transformLayer;
@"CALayer" _additionalTransformLayer;
@"CALayer" _trackingTransformLayer;
@"CALayer" _cameraTransformLayer;
```

## Properties

```
@property (T@"JFXOverlayEffectFrame",&,N,V_fromEffectFrame) fromEffectFrame;
@property (T@"JFXOverlayEffectFrame",&,N,V_toEffectFrame) toEffectFrame;
@property (T@"JFXEffectAnimationDelegate",&,N,V_animationDelegate) animationDelegate;
@property (T@"CALayer",&,N,V_transformLayer) transformLayer;
@property (T@"CALayer",&,N,V_additionalTransformLayer) additionalTransformLayer;
@property (T@"CALayer",&,N,V_trackingTransformLayer) trackingTransformLayer;
@property (T@"CALayer",&,N,V_cameraTransformLayer) cameraTransformLayer;
@property (Td,R,N) fractionComplete;
@property (T@"JFXOverlayEffectTransforms",R,N) currentEffectTransforms;
```

## Instance methods

```
-[JFXOverlayEffectAnimationView fractionComplete];
-[JFXOverlayEffectAnimationView animationDelegate];
-[JFXOverlayEffectAnimationView setAnimationDelegate:];
-[JFXOverlayEffectAnimationView animate:completion:];
-[JFXOverlayEffectAnimationView setTransformLayer:];
-[JFXOverlayEffectAnimationView transformLayer];
-[JFXOverlayEffectAnimationView fromEffectFrame];
-[JFXOverlayEffectAnimationView additionalTransformLayer];
-[JFXOverlayEffectAnimationView cameraTransformLayer];
-[JFXOverlayEffectAnimationView currentEffectTransforms];
-[JFXOverlayEffectAnimationView initWithEffectFrame:toEffectFrame:];
-[JFXOverlayEffectAnimationView setAdditionalTransformLayer:];
-[JFXOverlayEffectAnimationView setCameraTransformLayer:];
-[JFXOverlayEffectAnimationView setFromEffectFrame:];
-[JFXOverlayEffectAnimationView setToEffectFrame:];
-[JFXOverlayEffectAnimationView setTrackingTransformLayer:];
-[JFXOverlayEffectAnimationView toEffectFrame];
-[JFXOverlayEffectAnimationView trackingTransformLayer];
```
