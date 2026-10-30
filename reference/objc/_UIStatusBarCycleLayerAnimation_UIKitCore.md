# `_UIStatusBarCycleLayerAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"CALayer" _layer;
@"CAAnimation" _animation;
@"CAAnimation" _originalAnimation;
@"NSString" _key;
```

## Properties

```
@property (T@"CALayer",&,N,V_layer) layer;
@property (T@"CAAnimation",&,N,V_animation) animation;
@property (T@"CAAnimation",&,N,V_originalAnimation) originalAnimation;
@property (T@"NSString",C,N,V_key) key;
```

## Class methods

```
+[_UIStatusBarCycleLayerAnimation cycleAnimationWithLayer:animation:key:];
```

## Instance methods

```
-[_UIStatusBarCycleLayerAnimation layer];
-[_UIStatusBarCycleLayerAnimation setKey:];
-[_UIStatusBarCycleLayerAnimation setAnimation:];
-[_UIStatusBarCycleLayerAnimation description];
-[_UIStatusBarCycleLayerAnimation animation];
-[_UIStatusBarCycleLayerAnimation key];
-[_UIStatusBarCycleLayerAnimation setLayer:];
-[_UIStatusBarCycleLayerAnimation originalAnimation];
-[_UIStatusBarCycleLayerAnimation setOriginalAnimation:];
```
