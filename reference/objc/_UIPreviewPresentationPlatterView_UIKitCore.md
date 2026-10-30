# `_UIPreviewPresentationPlatterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _dropShadowEnabled;
@"UIView" _contentView;
@"_UIPreviewPresentationEffectView" _contentEffectView;
@"_UIPreviewPresentationEffectView" _contentClipView;
@"UIView" _contentTransformView;
@"UIView" _contentShadowView;
{CGSize="width"d"height"d} _contentSize;
{CGSize="width"d"height"d} _contentClippingSize;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"_UIPreviewPresentationEffectView",&,N,V_contentEffectView) contentEffectView;
@property (T@"_UIPreviewPresentationEffectView",&,N,V_contentClipView) contentClipView;
@property (T@"UIView",&,N,V_contentTransformView) contentTransformView;
@property (T@"UIView",&,N,V_contentShadowView) contentShadowView;
@property (T{CGSize=dd},N,V_contentSize) contentSize;
@property (T{CGSize=dd},N,V_contentClippingSize) contentClippingSize;
@property (Td,D,N) blurRadius;
@property (Td,D,N) cornerRadius;
@property (TB,N,GisDropShadowEnabled,V_dropShadowEnabled) dropShadowEnabled;
```

## Instance methods

```
-[_UIPreviewPresentationPlatterView initWithContentView:];
-[_UIPreviewPresentationPlatterView setContentView:];
-[_UIPreviewPresentationPlatterView layoutSubviews];
-[_UIPreviewPresentationPlatterView contentSize];
-[_UIPreviewPresentationPlatterView setCornerRadius:];
-[_UIPreviewPresentationPlatterView blurRadius];
-[_UIPreviewPresentationPlatterView cornerRadius];
-[_UIPreviewPresentationPlatterView contentView];
-[_UIPreviewPresentationPlatterView setContentSize:];
-[_UIPreviewPresentationPlatterView setBlurRadius:];
-[_UIPreviewPresentationPlatterView contentClipView];
-[_UIPreviewPresentationPlatterView _shouldEnclosedScrollViewFlashIndicators:];
-[_UIPreviewPresentationPlatterView contentClippingSize];
-[_UIPreviewPresentationPlatterView contentEffectView];
-[_UIPreviewPresentationPlatterView contentShadowView];
-[_UIPreviewPresentationPlatterView contentTransformView];
-[_UIPreviewPresentationPlatterView isDropShadowEnabled];
-[_UIPreviewPresentationPlatterView setContentClipView:];
-[_UIPreviewPresentationPlatterView setContentClippingSize:];
-[_UIPreviewPresentationPlatterView setContentEffectView:];
-[_UIPreviewPresentationPlatterView setContentShadowView:];
-[_UIPreviewPresentationPlatterView setContentTransformView:];
-[_UIPreviewPresentationPlatterView setDropShadowEnabled:];
```
