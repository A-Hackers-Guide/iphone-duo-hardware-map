# `_UIBarButtonItemAppearanceStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarItemAppearanceStorage`
- 7 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" backgroundImages;
@"NSMutableDictionary" miniBackgroundImages;
@"UIColor" tintColor;
@"NSValue" titlePositionOffset;
@"NSValue" miniTitlePositionOffset;
@"NSMutableDictionary" backgroundVerticalAdjustmentsForBarMetrics;
@"_UIBarBackButtonItemAppearanceStorage" backButtonAppearance;
```

## Properties

```
@property (T@"UIColor",&,N,VtintColor) tintColor;
@property (T@"NSValue",&,N,VtitlePositionOffset) titlePositionOffset;
@property (T@"NSValue",&,N,VminiTitlePositionOffset) miniTitlePositionOffset;
@property (T@"NSValue",&,N) backButtonTitlePositionOffset;
@property (T@"NSValue",&,N) miniBackButtonTitlePositionOffset;
```

## Instance methods

```
-[_UIBarButtonItemAppearanceStorage backButtonTitlePositionOffset];
-[_UIBarButtonItemAppearanceStorage titlePositionOffset];
-[_UIBarButtonItemAppearanceStorage backButtonBackgroundVerticalAdjustmentForBarMetrics:];
-[_UIBarButtonItemAppearanceStorage miniTitlePositionOffset];
-[_UIBarButtonItemAppearanceStorage setTitlePositionOffset:];
-[_UIBarButtonItemAppearanceStorage setBackgroundVerticalAdjustment:forBarMetrics:];
-[_UIBarButtonItemAppearanceStorage setTintColor:];
-[_UIBarButtonItemAppearanceStorage setBackgroundImage:forState:style:isMini:];
-[_UIBarButtonItemAppearanceStorage backgroundVerticalAdjustmentForBarMetrics:];
-[_UIBarButtonItemAppearanceStorage anyBackgroundImage];
-[_UIBarButtonItemAppearanceStorage backButtonBackgroundImageForState:isMini:];
-[_UIBarButtonItemAppearanceStorage backgroundImageForState:style:isMini:];
-[_UIBarButtonItemAppearanceStorage anyBackButtonBackgroundImage];
-[_UIBarButtonItemAppearanceStorage tintColor];
-[_UIBarButtonItemAppearanceStorage miniBackButtonTitlePositionOffset];
-[_UIBarButtonItemAppearanceStorage setMiniTitlePositionOffset:];
-[_UIBarButtonItemAppearanceStorage setBackButtonTitlePositionOffset:];
-[_UIBarButtonItemAppearanceStorage setBackButtonBackgroundImage:forState:isMini:];
-[_UIBarButtonItemAppearanceStorage setBackButtonBackgroundVerticalAdjustment:forBarMetrics:];
-[_UIBarButtonItemAppearanceStorage setMiniBackButtonTitlePositionOffset:];
```
