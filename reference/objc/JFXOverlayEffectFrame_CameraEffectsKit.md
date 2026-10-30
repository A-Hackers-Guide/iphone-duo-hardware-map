# `JFXOverlayEffectFrame`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXTextEffectFrame`
- 2 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
q _trackingType;
{CGPoint="x"d"y"d} _overlayCenter;
```

## Properties

```
@property (Tq,N,V_trackingType) trackingType;
@property (T@"JFXOverlayEffectTransforms",&,D,N) transforms;
@property (T{CGPoint=dd},N,V_overlayCenter) overlayCenter;
@property (TB,R,N) isTrackedButTrackingUnavailable;
```

## Class methods

```
+[JFXOverlayEffectFrame frameWithEffect:relativeToSize:origin:time:forcePosterFrame:includeDropShadow:includeTextFrames:];
```

## Instance methods

```
-[JFXOverlayEffectFrame description];
-[JFXOverlayEffectFrame setTrackingType:];
-[JFXOverlayEffectFrame trackingType];
-[JFXOverlayEffectFrame isTrackedButTrackingUnavailable];
-[JFXOverlayEffectFrame initWithEffect:relativeToSize:origin:time:forcePosterFrame:includeDropShadow:includeTextFrames:];
-[JFXOverlayEffectFrame overlayCenter];
-[JFXOverlayEffectFrame setOverlayCenter:];
```
