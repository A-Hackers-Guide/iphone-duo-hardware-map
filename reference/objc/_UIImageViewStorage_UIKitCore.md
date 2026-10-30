# `_UIImageViewStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`, `_UIImageViewStorage`
- 2 instance variables, 36 properties, 59 instance methods, 1 class methods

## Instance variables

```
@"UIImageView" _imageView;
@"<_UIImageViewStorage>" _storage;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIImage",&,N) image;
@property (T@"UIImage",&,N) highlightedImage;
@property (T@"UIImage",&,N) resolvedImage;
@property (T@"UIImage",&,N) resolvedHighlightedImage;
@property (T@"UIImageSymbolConfiguration",&,N) preferredSymbolConfiguration;
@property (T@"UIImageSymbolConfiguration",&,N) overridingSymbolConfiguration;
@property (T@"_UIImageSymbolVariant",&,N) preferredSymbolVariant;
@property (T@"NSArray",&,N) animationImages;
@property (T@"NSArray",&,N) highlightedAnimationImages;
@property (Td,N) animationDuration;
@property (Tq,N) animationRepeatCount;
@property (Tq,N) defaultRenderingMode;
@property (T@"<UITraitChangeRegistration>",&,N) systemIconAppearanceTraitRegistration;
@property (T@"_UIImageCIImageRenderer",&,N) CIRenderer;
@property (T@"UILayoutGuide",&,N) imageContentGuide;
@property (T@"_UIImageViewSymbolAnimationPresetManager",&,N) animationPresetManager;
@property (T@"NSMapTable",&,N) layouts;
@property (TI,N) drawMode;
@property (T@"_UIImageLoader",&,N) imageLoader;
@property (T@"<_UIImageViewLoadingDelegate>",&,N) loadingDelegate;
@property (T@"UIImage",&,N) imageBeingSetByLoader;
@property (T@"UIView",&,N) placeholderView;
@property (TB,N,GisHighlighted) highlighted;
@property (TB,N) masksTemplateImages;
@property (TB,N) adjustsImageSizeForAccessibilityContentSizeCategory;
@property (TB,N,GisStartingLoad) startingLoad;
@property (TB,N,GisEnqueueingLoad) enqueueingLoad;
@property (TB,N,GisStoppingLoad) stoppingLoad;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIImageViewStorage storageForImageView:];
```

## Instance methods

```
-[_UIImageViewStorage CIRenderer];
-[_UIImageViewStorage setDefaultRenderingMode:];
-[_UIImageViewStorage setDrawMode:];
-[_UIImageViewStorage setStartingLoad:];
-[_UIImageViewStorage isEnqueueingLoad];
-[_UIImageViewStorage setHighlightedImage:];
-[_UIImageViewStorage defaultRenderingMode];
-[_UIImageViewStorage loadingDelegate];
-[_UIImageViewStorage setEnqueueingLoad:];
-[_UIImageViewStorage overridingSymbolConfiguration];
-[_UIImageViewStorage setAnimationDuration:];
-[_UIImageViewStorage preferredSymbolConfiguration];
-[_UIImageViewStorage animationDidStop:finished:];
-[_UIImageViewStorage setLayouts:];
-[_UIImageViewStorage animationRepeatCount];
-[_UIImageViewStorage isStoppingLoad];
-[_UIImageViewStorage setLoadingDelegate:];
-[_UIImageViewStorage animationDuration];
-[_UIImageViewStorage setPlaceholderView:];
-[_UIImageViewStorage isHighlighted];
-[_UIImageViewStorage setAnimationImages:];
-[_UIImageViewStorage imageLoader];
-[_UIImageViewStorage setPreferredSymbolConfiguration:];
-[_UIImageViewStorage layouts];
-[_UIImageViewStorage masksTemplateImages];
-[_UIImageViewStorage extendedStorage];
-[_UIImageViewStorage imageContentGuide];
-[_UIImageViewStorage setSystemIconAppearanceTraitRegistration:];
-[_UIImageViewStorage setImageContentGuide:];
-[_UIImageViewStorage simpleStorage];
-[_UIImageViewStorage setPreferredSymbolVariant:];
-[_UIImageViewStorage setCIRenderer:];
-[_UIImageViewStorage drawMode];
-[_UIImageViewStorage preferredSymbolVariant];
-[_UIImageViewStorage adjustsImageSizeForAccessibilityContentSizeCategory];
-[_UIImageViewStorage imageBeingSetByLoader];
-[_UIImageViewStorage setImageLoader:];
-[_UIImageViewStorage setHighlighted:];
-[_UIImageViewStorage setImageBeingSetByLoader:];
-[_UIImageViewStorage resolvedImage];
-[_UIImageViewStorage setOverridingSymbolConfiguration:];
-[_UIImageViewStorage highlightedImage];
-[_UIImageViewStorage setAnimationPresetManager:];
-[_UIImageViewStorage systemIconAppearanceTraitRegistration];
-[_UIImageViewStorage setHighlightedAnimationImages:];
-[_UIImageViewStorage isStartingLoad];
-[_UIImageViewStorage image];
-[_UIImageViewStorage animationImages];
-[_UIImageViewStorage highlightedAnimationImages];
-[_UIImageViewStorage setAnimationRepeatCount:];
-[_UIImageViewStorage setResolvedHighlightedImage:];
-[_UIImageViewStorage animationPresetManager];
-[_UIImageViewStorage setAdjustsImageSizeForAccessibilityContentSizeCategory:];
-[_UIImageViewStorage setStoppingLoad:];
-[_UIImageViewStorage setResolvedImage:];
-[_UIImageViewStorage resolvedHighlightedImage];
-[_UIImageViewStorage placeholderView];
-[_UIImageViewStorage setMasksTemplateImages:];
-[_UIImageViewStorage setImage:];
```
