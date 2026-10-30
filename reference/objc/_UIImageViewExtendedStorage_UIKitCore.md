# `_UIImageViewExtendedStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIImageViewSimpleStorage`
- 9 instance variables, 0 properties, 54 instance methods, 1 class methods

## Instance variables

```
@"_UIImageViewImageProperties" _highlightedImageProperties;
@"_UIImageViewAnimationProperties" _animationProperties;
@"_UIImageViewImageLoadingProperties" _imageLoadingProperties;
@"_UIImageViewUncommonProperties" _uncommonProperties;
B highlighted;
B masksTemplateImages;
B adjustsImageSizeForAccessibilityContentSizeCategory;
@"UIImageSymbolConfiguration" preferredSymbolConfiguration;
@"UILayoutGuide" imageContentGuide;
```

## Class methods

```
+[_UIImageViewExtendedStorage storageFromSimpleStorage:];
```

## Instance methods

```
-[_UIImageViewExtendedStorage CIRenderer];
-[_UIImageViewExtendedStorage setDefaultRenderingMode:];
-[_UIImageViewExtendedStorage setDrawMode:];
-[_UIImageViewExtendedStorage setStartingLoad:];
-[_UIImageViewExtendedStorage isEnqueueingLoad];
-[_UIImageViewExtendedStorage setHighlightedImage:];
-[_UIImageViewExtendedStorage defaultRenderingMode];
-[_UIImageViewExtendedStorage loadingDelegate];
-[_UIImageViewExtendedStorage setEnqueueingLoad:];
-[_UIImageViewExtendedStorage overridingSymbolConfiguration];
-[_UIImageViewExtendedStorage setAnimationDuration:];
-[_UIImageViewExtendedStorage preferredSymbolConfiguration];
-[_UIImageViewExtendedStorage animationRepeatCount];
-[_UIImageViewExtendedStorage isStoppingLoad];
-[_UIImageViewExtendedStorage setLoadingDelegate:];
-[_UIImageViewExtendedStorage animationDuration];
-[_UIImageViewExtendedStorage setPlaceholderView:];
-[_UIImageViewExtendedStorage highlightedImageProperties];
-[_UIImageViewExtendedStorage uncommonProperties];
-[_UIImageViewExtendedStorage isHighlighted];
-[_UIImageViewExtendedStorage setAnimationImages:];
-[_UIImageViewExtendedStorage imageLoader];
-[_UIImageViewExtendedStorage setPreferredSymbolConfiguration:];
-[_UIImageViewExtendedStorage masksTemplateImages];
-[_UIImageViewExtendedStorage imageContentGuide];
-[_UIImageViewExtendedStorage setSystemIconAppearanceTraitRegistration:];
-[_UIImageViewExtendedStorage setImageContentGuide:];
-[_UIImageViewExtendedStorage setPreferredSymbolVariant:];
-[_UIImageViewExtendedStorage setCIRenderer:];
-[_UIImageViewExtendedStorage drawMode];
-[_UIImageViewExtendedStorage preferredSymbolVariant];
-[_UIImageViewExtendedStorage adjustsImageSizeForAccessibilityContentSizeCategory];
-[_UIImageViewExtendedStorage imageBeingSetByLoader];
-[_UIImageViewExtendedStorage animationProperties];
-[_UIImageViewExtendedStorage setImageLoader:];
-[_UIImageViewExtendedStorage setHighlighted:];
-[_UIImageViewExtendedStorage setImageBeingSetByLoader:];
-[_UIImageViewExtendedStorage setOverridingSymbolConfiguration:];
-[_UIImageViewExtendedStorage highlightedImage];
-[_UIImageViewExtendedStorage setAnimationPresetManager:];
-[_UIImageViewExtendedStorage systemIconAppearanceTraitRegistration];
-[_UIImageViewExtendedStorage setHighlightedAnimationImages:];
-[_UIImageViewExtendedStorage isStartingLoad];
-[_UIImageViewExtendedStorage animationImages];
-[_UIImageViewExtendedStorage highlightedAnimationImages];
-[_UIImageViewExtendedStorage setAnimationRepeatCount:];
-[_UIImageViewExtendedStorage setResolvedHighlightedImage:];
-[_UIImageViewExtendedStorage animationPresetManager];
-[_UIImageViewExtendedStorage setAdjustsImageSizeForAccessibilityContentSizeCategory:];
-[_UIImageViewExtendedStorage setStoppingLoad:];
-[_UIImageViewExtendedStorage resolvedHighlightedImage];
-[_UIImageViewExtendedStorage placeholderView];
-[_UIImageViewExtendedStorage imageLoadingProperties];
-[_UIImageViewExtendedStorage setMasksTemplateImages:];
```
