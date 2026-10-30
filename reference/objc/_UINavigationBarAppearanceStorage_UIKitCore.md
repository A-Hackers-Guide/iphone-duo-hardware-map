# `_UINavigationBarAppearanceStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarAppearanceStorage`
- 14 instance variables, 17 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" textAttributes;
@"NSMutableDictionary" titleVerticalAdjustmentsForBarMetrics;
@"UIImage" shadowImage;
B hidesShadow;
q barMetrics;
@"UIImage" backIndicatorImage;
@"UIImage" backIndicatorTransitionMaskImage;
@"NSNumber" backIndicatorLeftMargin;
B reversesShadowOffset;
@"_UIBarButtonItemAppearanceStorage" buttonAppearanceStorage;
B _deferShadowToSearchBar;
q defaultBarMetrics;
q activeBarMetrics;
@"NSString" _backdropViewGroupName;
```

## Properties

```
@property (T@"UIImage",R,N) backgroundImage;
@property (T@"UIImage",R,N) miniBackgroundImage;
@property (T@"UIImage",R,N) promptBackgroundImage;
@property (T@"UIImage",R,N) miniPromptBackgroundImage;
@property (T@"NSDictionary",C,N,VtextAttributes) textAttributes;
@property (T@"UIImage",&,N,VshadowImage) shadowImage;
@property (TB,N,VhidesShadow) hidesShadow;
@property (Tq,N,VdefaultBarMetrics) defaultBarMetrics;
@property (Tq,N,VactiveBarMetrics) activeBarMetrics;
@property (TB,N,VreversesShadowOffset) reversesShadowOffset;
@property (T@"_UIBarButtonItemAppearanceStorage",R,N) barButtonAppearanceStorage;
@property (T@"_UIBarButtonItemAppearanceStorage",R,N) _barButtonAppearanceStorage;
@property (TB,N,V_deferShadowToSearchBar) deferShadowToSearchBar;
@property (T@"UIImage",&,N,VbackIndicatorImage) backIndicatorImage;
@property (T@"UIImage",&,N,VbackIndicatorTransitionMaskImage) backIndicatorTransitionMaskImage;
@property (T@"NSNumber",&,N,VbackIndicatorLeftMargin) backIndicatorLeftMargin;
@property (T@"NSString",&,N,V_backdropViewGroupName) backdropViewGroupName;
```

## Class methods

```
+[_UINavigationBarAppearanceStorage typicalBarPosition];
```

## Instance methods

```
-[_UINavigationBarAppearanceStorage setBackIndicatorImage:];
-[_UINavigationBarAppearanceStorage shadowImage];
-[_UINavigationBarAppearanceStorage backgroundImage];
-[_UINavigationBarAppearanceStorage setShadowImage:];
-[_UINavigationBarAppearanceStorage backIndicatorTransitionMaskImage];
-[_UINavigationBarAppearanceStorage backIndicatorImage];
-[_UINavigationBarAppearanceStorage setHidesShadow:];
-[_UINavigationBarAppearanceStorage _barButtonAppearanceStorage];
-[_UINavigationBarAppearanceStorage activeBarMetrics];
-[_UINavigationBarAppearanceStorage backIndicatorLeftMargin];
-[_UINavigationBarAppearanceStorage backdropViewGroupName];
-[_UINavigationBarAppearanceStorage barButtonAppearanceStorage];
-[_UINavigationBarAppearanceStorage defaultBarMetrics];
-[_UINavigationBarAppearanceStorage deferShadowToSearchBar];
-[_UINavigationBarAppearanceStorage hidesShadow];
-[_UINavigationBarAppearanceStorage miniBackgroundImage];
-[_UINavigationBarAppearanceStorage miniPromptBackgroundImage];
-[_UINavigationBarAppearanceStorage promptBackgroundImage];
-[_UINavigationBarAppearanceStorage representativeImageForIdiom:];
-[_UINavigationBarAppearanceStorage reversesShadowOffset];
-[_UINavigationBarAppearanceStorage setActiveBarMetrics:];
-[_UINavigationBarAppearanceStorage setBackIndicatorLeftMargin:];
-[_UINavigationBarAppearanceStorage setBackIndicatorTransitionMaskImage:];
-[_UINavigationBarAppearanceStorage setBackdropViewGroupName:];
-[_UINavigationBarAppearanceStorage setDefaultBarMetrics:];
-[_UINavigationBarAppearanceStorage setDeferShadowToSearchBar:];
-[_UINavigationBarAppearanceStorage setReversesShadowOffset:];
-[_UINavigationBarAppearanceStorage setTextAttributes:];
-[_UINavigationBarAppearanceStorage setTitleVerticalAdjustment:forBarMetrics:];
-[_UINavigationBarAppearanceStorage textAttributes];
-[_UINavigationBarAppearanceStorage titleVerticalAdjustmentForBarMetrics:];
```
