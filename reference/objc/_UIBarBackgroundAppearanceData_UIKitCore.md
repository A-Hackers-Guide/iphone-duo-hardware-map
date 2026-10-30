# `_UIBarBackgroundAppearanceData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarAppearanceData`
- 13 instance variables, 17 properties, 38 instance methods, 4 class methods

## Instance variables

```
{?="backgroundEffectsAreSingular"b1"hasBackground"b1"hasShadow"b1"needsToCalculateVibrantEffect"b1} _flags;
@"UIVibrancyEffect" _shadowViewEffect;
@"UIVibrancyEffect" _tabBarVibrancyEffect;
@"NSArray" _backgroundEffects;
@"UIColor" _backgroundColor;
@"UIImage" _backgroundImage;
q _backgroundImageContentMode;
@"UIVibrancyEffect" _overrideTabBarVibrancyEffect;
@"UIColor" _shadowColor;
@"UIImage" _shadowImage;
@"UIVibrancyEffect" _shadowEffect;
q _visibility;
d _visibilityOnScrollDistance;
```

## Properties

```
@property (T@"UIBlurEffect",C,N) backgroundEffect;
@property (T@"NSArray",C,N,V_backgroundEffects) backgroundEffects;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
@property (T@"UIImage",&,N,V_backgroundImage) backgroundImage;
@property (Tq,N,V_backgroundImageContentMode) backgroundImageContentMode;
@property (T@"UIVibrancyEffect",&,N,V_overrideTabBarVibrancyEffect) overrideTabBarVibrancyEffect;
@property (T@"UIColor",C,N,V_shadowColor) shadowColor;
@property (T@"UIImage",&,N,V_shadowImage) shadowImage;
@property (T@"UIVibrancyEffect",C,N,V_shadowEffect) shadowEffect;
@property (TB,R,N) hasBackground;
@property (TB,R,N) hasShadow;
@property (T@"UIVibrancyEffect",R,N,V_shadowViewEffect) shadowViewEffect;
@property (T@"UIColor",R,N) shadowViewBackgroundColor;
@property (T@"UIColor",R,N) shadowViewTintColor;
@property (T@"UIVibrancyEffect",R,N,V_tabBarVibrancyEffect) tabBarVibrancyEffect;
@property (Tq,N,V_visibility) visibility;
@property (Td,N,V_visibilityOnScrollDistance) visibilityOnScrollDistance;
```

## Class methods

```
+[_UIBarBackgroundAppearanceData decodeFromCoder:prefix:];
+[_UIBarBackgroundAppearanceData opaqueBackgroundData];
+[_UIBarBackgroundAppearanceData standardBackgroundData];
+[_UIBarBackgroundAppearanceData transparentBackgroundData];
```

## Instance methods

```
-[_UIBarBackgroundAppearanceData describeInto:];
-[_UIBarBackgroundAppearanceData hasShadow];
-[_UIBarBackgroundAppearanceData hashInto:];
-[_UIBarBackgroundAppearanceData setBackgroundImageContentMode:];
-[_UIBarBackgroundAppearanceData setBackgroundEffect:];
-[_UIBarBackgroundAppearanceData setVisibility:];
-[_UIBarBackgroundAppearanceData backgroundEffects];
-[_UIBarBackgroundAppearanceData setBackgroundImage:];
-[_UIBarBackgroundAppearanceData encodeToCoder:prefix:];
-[_UIBarBackgroundAppearanceData setOverrideTabBarVibrancyEffect:];
-[_UIBarBackgroundAppearanceData shadowImage];
-[_UIBarBackgroundAppearanceData backgroundImage];
-[_UIBarBackgroundAppearanceData visibility];
-[_UIBarBackgroundAppearanceData configureWithDefaultShadow];
-[_UIBarBackgroundAppearanceData behaviorForTransitioningTo:];
-[_UIBarBackgroundAppearanceData shadowViewBackgroundColor];
-[_UIBarBackgroundAppearanceData shadowViewEffect];
-[_UIBarBackgroundAppearanceData setShadowEffect:];
-[_UIBarBackgroundAppearanceData shadowColor];
-[_UIBarBackgroundAppearanceData backgroundEffect];
-[_UIBarBackgroundAppearanceData setBackgroundColor:];
-[_UIBarBackgroundAppearanceData _updateBackgroundFlags];
-[_UIBarBackgroundAppearanceData setShadowImage:];
-[_UIBarBackgroundAppearanceData shadowViewTintColor];
-[_UIBarBackgroundAppearanceData tabBarVibrancyEffect];
-[_UIBarBackgroundAppearanceData visibilityOnScrollDistance];
-[_UIBarBackgroundAppearanceData configureWithoutShadow];
-[_UIBarBackgroundAppearanceData setBackgroundEffects:];
-[_UIBarBackgroundAppearanceData backgroundColor];
-[_UIBarBackgroundAppearanceData overrideTabBarVibrancyEffect];
-[_UIBarBackgroundAppearanceData setShadowColor:];
-[_UIBarBackgroundAppearanceData checkEqualTo:];
-[_UIBarBackgroundAppearanceData shadowEffect];
-[_UIBarBackgroundAppearanceData _updateShadowFlags];
-[_UIBarBackgroundAppearanceData replicate];
-[_UIBarBackgroundAppearanceData setVisibilityOnScrollDistance:];
-[_UIBarBackgroundAppearanceData backgroundImageContentMode];
-[_UIBarBackgroundAppearanceData hasBackground];
```
