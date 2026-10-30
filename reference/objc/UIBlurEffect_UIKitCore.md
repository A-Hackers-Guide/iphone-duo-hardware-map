# `UIBlurEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- 1 instance variables, 5 properties, 20 instance methods, 13 class methods

## Instance variables

```
@"_UIBlurEffectImpl" _impl;
```

## Properties

```
@property (TB,R,N) _canProvideVibrancyEffect;
@property (TB,R,N) _canProvideCoreMaterialVibrancyEffect;
@property (Tq,R,N) _style;
@property (T@"UIColor",R,N) _tintColor;
@property (TB,R,N) _invertAutomaticStyle;
```

## Class methods

```
+[UIBlurEffect supportsSecureCoding];
+[UIBlurEffect _effectWithInfiniteRadiusScale:];
+[UIBlurEffect _effectForLightMaterial:darkMaterial:bundle:];
+[UIBlurEffect _effectWithBlurRadius:scale:];
+[UIBlurEffect _effectWithInfiniteRadius];
+[UIBlurEffect _effectWithStyle:invertAutomaticStyle:];
+[UIBlurEffect _effectWithStyle:tintColor:invertAutomaticStyle:];
+[UIBlurEffect _effectWithTintColor:];
+[UIBlurEffect _effectWithVariableBlurRadius:imageMask:scale:];
+[UIBlurEffect _effectWithVariableBlurRadius:imageMask:scale:allowingAXAdaptation:];
+[UIBlurEffect effectWithBlurRadius:];
+[UIBlurEffect effectWithStyle:];
+[UIBlurEffect effectWithVariableBlurRadius:imageMask:];
```

## Instance methods

```
-[UIBlurEffect _tintColor];
-[UIBlurEffect _expectedUsage];
-[UIBlurEffect effectForUserInterfaceStyle:];
-[UIBlurEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[UIBlurEffect init];
-[UIBlurEffect _initWithImplementation:];
-[UIBlurEffect _isAutomaticStyle];
-[UIBlurEffect _isATVStyle];
-[UIBlurEffect _updateEffectDescriptor:forEnvironment:usage:];
-[UIBlurEffect encodeWithCoder:];
-[UIBlurEffect hash];
-[UIBlurEffect description];
-[UIBlurEffect _style];
-[UIBlurEffect initWithCoder:];
-[UIBlurEffect copyWithZone:];
-[UIBlurEffect isEqual:];
-[UIBlurEffect _canProvideCoreMaterialVibrancyEffect];
-[UIBlurEffect _canProvideVibrancyEffect];
-[UIBlurEffect _invertAutomaticStyle];
-[UIBlurEffect effectSettings];
```
