# `UIVisualEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewMaterial`, `NSCopying`, `NSSecureCoding`
- 0 instance variables, 4 properties, 17 instance methods, 8 class methods

## Properties

```
@property (T@"_UIBackdropViewSettings",R,N) effectSettings;
@property (TB,R,N) _isATVStyle;
@property (TB,R,N) _isAutomaticStyle;
@property (T@"_UIVisualEffectConfig",R,N) effectConfig;
```

## Class methods

```
+[UIVisualEffect supportsSecureCoding];
+[UIVisualEffect _effectCopyingFromCaptureGroup:];
+[UIVisualEffect effectCombiningEffects:];
+[UIVisualEffect effectCompositingColor:];
+[UIVisualEffect effectCompositingColor:withMode:alpha:];
+[UIVisualEffect effectCompositingImage:];
+[UIVisualEffect effectCompositingImage:withMode:alpha:];
+[UIVisualEffect emptyEffect];
```

## Instance methods

```
-[UIVisualEffect _expectedUsage];
-[UIVisualEffect effectForUserInterfaceStyle:];
-[UIVisualEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[UIVisualEffect _isAutomaticStyle];
-[UIVisualEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:changedTraits:usage:];
-[UIVisualEffect effectConfig];
-[UIVisualEffect _isATVStyle];
-[UIVisualEffect _resolvedMaterialUsingTraitCollection:size:];
-[UIVisualEffect _updateEffectDescriptor:forEnvironment:usage:];
-[UIVisualEffect effectConfigForQuality:];
-[UIVisualEffect encodeWithCoder:];
-[UIVisualEffect initWithCoder:];
-[UIVisualEffect copyWithZone:];
-[UIVisualEffect _allEffects];
-[UIVisualEffect _enumerateEffects:];
-[UIVisualEffect _selectorOverridden:];
-[UIVisualEffect effectSettings];
```
