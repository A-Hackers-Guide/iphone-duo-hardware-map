# `_UIVisualEffectEnvironment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _allowsDithering;
B _useSimpleVibrancy;
B _reducedTransperancy;
B _reducedMotion;
@"UIVisualEffectView" _effectView;
q _blurQuality;
@"UITraitCollection" _traitCollection;
```

## Properties

```
@property (T@"UIVisualEffectView",R,N,V_effectView) effectView;
@property (TB,N,V_allowsDithering) allowsDithering;
@property (TB,N) allowsBlurring;
@property (Tq,N,V_blurQuality) blurQuality;
@property (TB,N,V_useSimpleVibrancy) useSimpleVibrancy;
@property (TB,N,V_reducedTransperancy) reducedTransperancy;
@property (TB,N,V_reducedMotion) reducedMotion;
@property (T@"UITraitCollection",C,N,V_traitCollection) traitCollection;
```

## Instance methods

```
-[_UIVisualEffectEnvironment reducedTransperancy];
-[_UIVisualEffectEnvironment setTraitCollection:];
-[_UIVisualEffectEnvironment setReducedMotion:];
-[_UIVisualEffectEnvironment traitCollection];
-[_UIVisualEffectEnvironment blurQuality];
-[_UIVisualEffectEnvironment initWithHost:];
-[_UIVisualEffectEnvironment setAllowsBlurring:];
-[_UIVisualEffectEnvironment reducedMotion];
-[_UIVisualEffectEnvironment useSimpleVibrancy];
-[_UIVisualEffectEnvironment effectView];
-[_UIVisualEffectEnvironment setUseSimpleVibrancy:];
-[_UIVisualEffectEnvironment description];
-[_UIVisualEffectEnvironment allowsDithering];
-[_UIVisualEffectEnvironment setReducedTransperancy:];
-[_UIVisualEffectEnvironment copyWithZone:];
-[_UIVisualEffectEnvironment setBlurQuality:];
-[_UIVisualEffectEnvironment setAllowsDithering:];
-[_UIVisualEffectEnvironment _applyBlurQualityToConfigurationDictionary:];
-[_UIVisualEffectEnvironment allowsBlurring];
```
