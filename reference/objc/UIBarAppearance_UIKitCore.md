# `UIBarAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 13 properties, 60 instance methods, 1 class methods

## Instance variables

```
@"<_UIBarAppearanceChangeObserver>" _changeObserver;
q _idiom;
@"_UIBarBackgroundAppearanceData" _backgroundData;
q _batchedChanges;
B _batchingChanges;
q _overrideUserInterfaceStyle;
```

## Properties

```
@property (TB,R) _hasTransparentBackground;
@property (T@"UIVibrancyEffect",C,N,S_setSelectedItemVibrancyEffect:) _selectedItemVibrancyEffect;
@property (T@"NSArray",C,N) backgroundEffects;
@property (T@"UIVibrancyEffect",C,N) shadowEffect;
@property (Tq,N,S_setOverrideUserInterfaceStyle:) _overrideUserInterfaceStyle;
@property (Tq,R,N,V_idiom) idiom;
@property (T@"UIBlurEffect",C,N) backgroundEffect;
@property (T@"UIColor",C,N) backgroundColor;
@property (T@"UIImage",&,N) backgroundImage;
@property (Tq,N) backgroundImageContentMode;
@property (T@"UIColor",C,N) shadowColor;
@property (T@"UIImage",&,N) shadowImage;
@property (Tq,N,V_overrideUserInterfaceStyle) overrideUserInterfaceStyle;
```

## Class methods

```
+[UIBarAppearance supportsSecureCoding];
```

## Instance methods

```
-[UIBarAppearance _defaultBackgroundData];
-[UIBarAppearance _setSelectedItemVibrancyEffect:];
-[UIBarAppearance setBackgroundImageContentMode:];
-[UIBarAppearance setBackgroundEffect:];
-[UIBarAppearance _selectedItemVibrancyEffect];
-[UIBarAppearance backgroundEffects];
-[UIBarAppearance setBackgroundImage:];
-[UIBarAppearance shadowImage];
-[UIBarAppearance backgroundImage];
-[UIBarAppearance init];
-[UIBarAppearance _stackedTabButtonAppearanceData];
-[UIBarAppearance configureWithDefaultBackground];
-[UIBarAppearance copy];
-[UIBarAppearance configureWithDefaultShadow];
-[UIBarAppearance _backgroundData];
-[UIBarAppearance _backButtonAppearance];
-[UIBarAppearance _checkEqualTo:];
-[UIBarAppearance _prominentButtonAppearance];
-[UIBarAppearance initWithIdiom:];
-[UIBarAppearance _applyOverrideUserInterfaceStyle:];
-[UIBarAppearance _barTitleData];
-[UIBarAppearance _overrideUserInterfaceStyle];
-[UIBarAppearance setShadowEffect:];
-[UIBarAppearance shadowColor];
-[UIBarAppearance backgroundEffect];
-[UIBarAppearance setBackgroundColor:];
-[UIBarAppearance _describeInto:];
-[UIBarAppearance _decodeFromCoder:];
-[UIBarAppearance setShadowImage:];
-[UIBarAppearance _setupDefaults];
-[UIBarAppearance _plainButtonAppearanceData];
-[UIBarAppearance _hasTransparentBackground];
-[UIBarAppearance setOverrideUserInterfaceStyle:];
-[UIBarAppearance _inlineTabButtonAppearanceData];
-[UIBarAppearance configureWithoutShadow];
-[UIBarAppearance encodeWithCoder:];
-[UIBarAppearance setBackgroundEffects:];
-[UIBarAppearance initWithBarAppearance:];
-[UIBarAppearance _setOverrideUserInterfaceStyle:];
-[UIBarAppearance hash];
-[UIBarAppearance backgroundColor];
-[UIBarAppearance description];
-[UIBarAppearance _tabLayoutAppearanceData];
-[UIBarAppearance initWithCoder:];
-[UIBarAppearance _plainButtonAppearance];
-[UIBarAppearance setShadowColor:];
-[UIBarAppearance _backButtonAppearanceData];
-[UIBarAppearance configureWithOpaqueBackground];
-[UIBarAppearance shadowEffect];
-[UIBarAppearance copyWithZone:];
-[UIBarAppearance overrideUserInterfaceStyle];
-[UIBarAppearance _prominentButtonAppearanceData];
-[UIBarAppearance isEqual:];
-[UIBarAppearance _completeInit];
-[UIBarAppearance _hashInto:];
-[UIBarAppearance configureWithTransparentBackground];
-[UIBarAppearance _compactInlineTabButtonAppearanceData];
-[UIBarAppearance _copyFromAppearance:];
-[UIBarAppearance backgroundImageContentMode];
-[UIBarAppearance idiom];
```
