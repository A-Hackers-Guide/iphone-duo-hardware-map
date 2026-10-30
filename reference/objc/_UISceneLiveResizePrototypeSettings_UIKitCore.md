# `_UISceneLiveResizePrototypeSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _snapshottingEnabled;
B _stretchingEnabled;
B _transparentTearingEnabled;
B _animationFenceEnabled;
@"NSNumber" _animationMode;
@"NSNumber" _throttlingMode;
```

## Properties

```
@property (TB,N,V_snapshottingEnabled) snapshottingEnabled;
@property (TB,N,V_stretchingEnabled) stretchingEnabled;
@property (TB,N,V_transparentTearingEnabled) transparentTearingEnabled;
@property (T@"NSNumber",&,N,V_animationMode) animationMode;
@property (T@"NSNumber",&,N,V_throttlingMode) throttlingMode;
@property (TB,N,V_animationFenceEnabled) animationFenceEnabled;
```

## Class methods

```
+[_UISceneLiveResizePrototypeSettings settingsControllerModule];
```

## Instance methods

```
-[_UISceneLiveResizePrototypeSettings setDefaultValues];
-[_UISceneLiveResizePrototypeSettings initWithDefaultValues];
-[_UISceneLiveResizePrototypeSettings _effectiveThrottlingMode];
-[_UISceneLiveResizePrototypeSettings animationFenceEnabled];
-[_UISceneLiveResizePrototypeSettings animationMode];
-[_UISceneLiveResizePrototypeSettings setAnimationFenceEnabled:];
-[_UISceneLiveResizePrototypeSettings setAnimationMode:];
-[_UISceneLiveResizePrototypeSettings setSnapshottingEnabled:];
-[_UISceneLiveResizePrototypeSettings setStretchingEnabled:];
-[_UISceneLiveResizePrototypeSettings setThrottlingMode:];
-[_UISceneLiveResizePrototypeSettings setTransparentTearingEnabled:];
-[_UISceneLiveResizePrototypeSettings snapshottingEnabled];
-[_UISceneLiveResizePrototypeSettings stretchingEnabled];
-[_UISceneLiveResizePrototypeSettings throttlingMode];
-[_UISceneLiveResizePrototypeSettings transparentTearingEnabled];
```
