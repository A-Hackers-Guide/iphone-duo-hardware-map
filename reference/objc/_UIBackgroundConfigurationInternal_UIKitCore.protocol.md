# `_UIBackgroundConfigurationInternal` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 26 properties, 51 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",&,N) customView;
@property (Td,N) cornerRadius;
@property (T{NSDirectionalEdgeInsets=dddd},N) backgroundInsets;
@property (TQ,N) edgesAddingLayoutMarginsToBackgroundInsets;
@property (T@"UIColor",&,N) backgroundColor;
@property (TB,R,N) isTintBackgroundColor;
@property (T@"UIVisualEffect",C,N) visualEffect;
@property (T@"UIImage",&,N) image;
@property (Tq,N) imageContentMode;
@property (T@"UIColor",&,N) strokeColor;
@property (Td,N) strokeWidth;
@property (Td,N) strokeOutset;
@property (Tq,N,G_strokeLocation,S_setStrokeLocation:) strokeLocation;
@property (TQ,N,S__setMaskedCorners:) __maskedCorners;
@property (T@"NSString",C,N,S__setVisualEffectGroupName:) __visualEffectGroupName;
@property (Td,N,S_setCornerRadius:) _cornerRadius;
@property (T@"UIShadowProperties",R,N) _shadowProperties;
@property (TB,R,N,G_hasBackgroundColor) hasBackgroundColor;
@property (TB,R,N,G_hasStroke) hasStroke;
@property (TB,R,N,G_hasBackgroundFill) hasBackgroundFill;
@property (TQ,N,S__setVisualEffectblurClippingMode:) __visualEffectblurClippingMode;
@property (TB,R,N,G_hasMaterial) hasMaterial;
@property (T@"<_UIViewMaterial>",&,N,S_setMaterial:) _material;
@property (TB,R,N,G_hasContentView) hasContentView;
@property (T@"UIView",&,N,S_setContentView:) _contentView;
@property (TB,N,S_setContentViewIgnoresBackgroundInsets:) _contentViewIgnoresBackgroundInsets;
```

## Instance methods

```
-[_UIBackgroundConfigurationInternal imageContentMode];
-[_UIBackgroundConfigurationInternal setImageContentMode:];
-[_UIBackgroundConfigurationInternal resolvedStrokeColorForTintColor:];
-[_UIBackgroundConfigurationInternal customView];
-[_UIBackgroundConfigurationInternal _setCornerRadius:];
-[_UIBackgroundConfigurationInternal _hasBackgroundFill];
-[_UIBackgroundConfigurationInternal _setMaterial:];
-[_UIBackgroundConfigurationInternal _hasBackgroundColor];
-[_UIBackgroundConfigurationInternal _setContentView:];
-[_UIBackgroundConfigurationInternal setStrokeWidth:];
-[_UIBackgroundConfigurationInternal _setStrokeLocation:];
-[_UIBackgroundConfigurationInternal _cornerRadius];
-[_UIBackgroundConfigurationInternal _hasMaterial];
-[_UIBackgroundConfigurationInternal strokeWidth];
-[_UIBackgroundConfigurationInternal strokeOutset];
-[_UIBackgroundConfigurationInternal _contentViewIgnoresBackgroundInsets];
-[_UIBackgroundConfigurationInternal setStrokeColor:];
-[_UIBackgroundConfigurationInternal _contentView];
-[_UIBackgroundConfigurationInternal setEdgesAddingLayoutMarginsToBackgroundInsets:];
-[_UIBackgroundConfigurationInternal __setVisualEffectblurClippingMode:];
-[_UIBackgroundConfigurationInternal visualEffect];
-[_UIBackgroundConfigurationInternal _strokeLocation];
-[_UIBackgroundConfigurationInternal strokeColor];
-[_UIBackgroundConfigurationInternal setCornerRadius:];
-[_UIBackgroundConfigurationInternal _backgroundFillIsEqual:withTintColor:];
-[_UIBackgroundConfigurationInternal __setVisualEffectGroupName:];
-[_UIBackgroundConfigurationInternal _updatedConfigurationForState:];
-[_UIBackgroundConfigurationInternal setBackgroundColor:];
-[_UIBackgroundConfigurationInternal _material];
-[_UIBackgroundConfigurationInternal __maskedCorners];
-[_UIBackgroundConfigurationInternal __visualEffectblurClippingMode];
-[_UIBackgroundConfigurationInternal setStrokeOutset:];
-[_UIBackgroundConfigurationInternal _isEqualToInternalConfigurationLayoutOnly:];
-[_UIBackgroundConfigurationInternal cornerRadius];
-[_UIBackgroundConfigurationInternal setCustomView:];
-[_UIBackgroundConfigurationInternal __setMaskedCorners:];
-[_UIBackgroundConfigurationInternal backgroundColor];
-[_UIBackgroundConfigurationInternal _setContentViewIgnoresBackgroundInsets:];
-[_UIBackgroundConfigurationInternal __visualEffectGroupName];
-[_UIBackgroundConfigurationInternal _hasContentView];
-[_UIBackgroundConfigurationInternal setBackgroundInsets:];
-[_UIBackgroundConfigurationInternal _isEqualToInternalConfigurationQuick:];
-[_UIBackgroundConfigurationInternal _shadowProperties];
-[_UIBackgroundConfigurationInternal isTintBackgroundColor];
-[_UIBackgroundConfigurationInternal image];
-[_UIBackgroundConfigurationInternal _hasStroke];
-[_UIBackgroundConfigurationInternal edgesAddingLayoutMarginsToBackgroundInsets];
-[_UIBackgroundConfigurationInternal backgroundInsets];
-[_UIBackgroundConfigurationInternal resolvedBackgroundColorForTintColor:];
-[_UIBackgroundConfigurationInternal setVisualEffect:];
-[_UIBackgroundConfigurationInternal setImage:];
```
