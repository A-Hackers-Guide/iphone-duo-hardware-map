# `_UIWindowSceneActivationSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 9 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
d _pinchActivationScaleThreshold;
d _pinchEndingProjectionDuration;
d _pinchPlatterMaxShadowIntensity;
d _pinchEndPlatterVelocityMultiplier;
@"_UISpringAnimationPrototypeSettings" _pinchInteractiveScale;
@"_UISpringAnimationPrototypeSettings" _pinchSettle;
@"_UISpringAnimationPrototypeSettings" _pinchShadow;
@"_UISpringAnimationPrototypeSettings" _morph;
@"_UISpringAnimationPrototypeSettings" _morphMenuDismissal;
```

## Properties

```
@property (Td,N,V_pinchActivationScaleThreshold) pinchActivationScaleThreshold;
@property (Td,N,V_pinchEndingProjectionDuration) pinchEndingProjectionDuration;
@property (Td,N,V_pinchPlatterMaxShadowIntensity) pinchPlatterMaxShadowIntensity;
@property (Td,N,V_pinchEndPlatterVelocityMultiplier) pinchEndPlatterVelocityMultiplier;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_pinchInteractiveScale) pinchInteractiveScale;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_pinchSettle) pinchSettle;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_pinchShadow) pinchShadow;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_morph) morph;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_morphMenuDismissal) morphMenuDismissal;
```

## Class methods

```
+[_UIWindowSceneActivationSettings settingsControllerModule];
```

## Instance methods

```
-[_UIWindowSceneActivationSettings setDefaultValues];
-[_UIWindowSceneActivationSettings setPinchShadow:];
-[_UIWindowSceneActivationSettings setPinchSettle:];
-[_UIWindowSceneActivationSettings morph];
-[_UIWindowSceneActivationSettings morphMenuDismissal];
-[_UIWindowSceneActivationSettings pinchActivationScaleThreshold];
-[_UIWindowSceneActivationSettings pinchEndPlatterVelocityMultiplier];
-[_UIWindowSceneActivationSettings pinchEndingProjectionDuration];
-[_UIWindowSceneActivationSettings pinchInteractiveScale];
-[_UIWindowSceneActivationSettings pinchPlatterMaxShadowIntensity];
-[_UIWindowSceneActivationSettings pinchSettle];
-[_UIWindowSceneActivationSettings pinchShadow];
-[_UIWindowSceneActivationSettings setMorph:];
-[_UIWindowSceneActivationSettings setMorphMenuDismissal:];
-[_UIWindowSceneActivationSettings setPinchActivationScaleThreshold:];
-[_UIWindowSceneActivationSettings setPinchEndPlatterVelocityMultiplier:];
-[_UIWindowSceneActivationSettings setPinchEndingProjectionDuration:];
-[_UIWindowSceneActivationSettings setPinchInteractiveScale:];
-[_UIWindowSceneActivationSettings setPinchPlatterMaxShadowIntensity:];
```
