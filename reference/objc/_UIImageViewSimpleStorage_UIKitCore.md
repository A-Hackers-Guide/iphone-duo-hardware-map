# `_UIImageViewSimpleStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIImageViewStorage`
- 2 instance variables, 32 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"_UIImageViewImageProperties" _imageProperties;
@"NSMapTable" layouts;
```

## Properties

```
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
@property (T@"NSMapTable",&,N,Vlayouts) layouts;
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

## Instance methods

```
-[_UIImageViewSimpleStorage CIRenderer];
-[_UIImageViewSimpleStorage setDefaultRenderingMode:];
-[_UIImageViewSimpleStorage setDrawMode:];
-[_UIImageViewSimpleStorage setStartingLoad:];
-[_UIImageViewSimpleStorage isEnqueueingLoad];
-[_UIImageViewSimpleStorage setHighlightedImage:];
-[_UIImageViewSimpleStorage defaultRenderingMode];
-[_UIImageViewSimpleStorage loadingDelegate];
-[_UIImageViewSimpleStorage imageProperties];
-[_UIImageViewSimpleStorage setEnqueueingLoad:];
-[_UIImageViewSimpleStorage overridingSymbolConfiguration];
-[_UIImageViewSimpleStorage setAnimationDuration:];
-[_UIImageViewSimpleStorage preferredSymbolConfiguration];
-[_UIImageViewSimpleStorage setLayouts:];
-[_UIImageViewSimpleStorage animationRepeatCount];
-[_UIImageViewSimpleStorage isStoppingLoad];
-[_UIImageViewSimpleStorage setLoadingDelegate:];
-[_UIImageViewSimpleStorage animationDuration];
-[_UIImageViewSimpleStorage setPlaceholderView:];
-[_UIImageViewSimpleStorage isHighlighted];
-[_UIImageViewSimpleStorage setAnimationImages:];
-[_UIImageViewSimpleStorage imageLoader];
-[_UIImageViewSimpleStorage setPreferredSymbolConfiguration:];
-[_UIImageViewSimpleStorage layouts];
-[_UIImageViewSimpleStorage masksTemplateImages];
-[_UIImageViewSimpleStorage imageContentGuide];
-[_UIImageViewSimpleStorage setSystemIconAppearanceTraitRegistration:];
-[_UIImageViewSimpleStorage setImageContentGuide:];
-[_UIImageViewSimpleStorage setPreferredSymbolVariant:];
-[_UIImageViewSimpleStorage setCIRenderer:];
-[_UIImageViewSimpleStorage drawMode];
-[_UIImageViewSimpleStorage preferredSymbolVariant];
-[_UIImageViewSimpleStorage adjustsImageSizeForAccessibilityContentSizeCategory];
-[_UIImageViewSimpleStorage imageBeingSetByLoader];
-[_UIImageViewSimpleStorage setImageLoader:];
-[_UIImageViewSimpleStorage setHighlighted:];
-[_UIImageViewSimpleStorage setImageBeingSetByLoader:];
-[_UIImageViewSimpleStorage resolvedImage];
-[_UIImageViewSimpleStorage setOverridingSymbolConfiguration:];
-[_UIImageViewSimpleStorage highlightedImage];
-[_UIImageViewSimpleStorage setAnimationPresetManager:];
-[_UIImageViewSimpleStorage systemIconAppearanceTraitRegistration];
-[_UIImageViewSimpleStorage setHighlightedAnimationImages:];
-[_UIImageViewSimpleStorage isStartingLoad];
-[_UIImageViewSimpleStorage image];
-[_UIImageViewSimpleStorage animationImages];
-[_UIImageViewSimpleStorage highlightedAnimationImages];
-[_UIImageViewSimpleStorage setAnimationRepeatCount:];
-[_UIImageViewSimpleStorage setResolvedHighlightedImage:];
-[_UIImageViewSimpleStorage animationPresetManager];
-[_UIImageViewSimpleStorage setAdjustsImageSizeForAccessibilityContentSizeCategory:];
-[_UIImageViewSimpleStorage setStoppingLoad:];
-[_UIImageViewSimpleStorage setResolvedImage:];
-[_UIImageViewSimpleStorage resolvedHighlightedImage];
-[_UIImageViewSimpleStorage placeholderView];
-[_UIImageViewSimpleStorage setMasksTemplateImages:];
-[_UIImageViewSimpleStorage setImage:];
```
