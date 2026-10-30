# `_UIPreviewPresentationContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 10 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _shouldLayoutForCommitPhase;
@"UIView" _contentView;
d _cornerRadius;
@"_UIPreviewPresentationEffectView" _platterClippingView;
@"UIView" _platterShadowView;
@"UIView" _contentTransformView;
@"_UIPreviewPresentationEffectView" _platterView;
{CGSize="width"d"height"d} _preferredContentSize;
```

## Properties

```
@property (T@"_UIPreviewPresentationEffectView",&,N,V_platterClippingView) platterClippingView;
@property (T@"UIView",&,N,V_platterShadowView) platterShadowView;
@property (T@"UIView",&,N,V_contentTransformView) contentTransformView;
@property (T@"_UIPreviewPresentationEffectView",&,N,V_platterView) platterView;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T{CGSize=dd},N,V_preferredContentSize) preferredContentSize;
@property (Td,D,N) blurRadius;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TB,D,N) shouldRasterizeForTransition;
@property (TB,N,V_shouldLayoutForCommitPhase) shouldLayoutForCommitPhase;
```

## Instance methods

```
-[_UIPreviewPresentationContainerView platterView];
-[_UIPreviewPresentationContainerView setContentView:];
-[_UIPreviewPresentationContainerView setPreferredContentSize:];
-[_UIPreviewPresentationContainerView setPlatterView:];
-[_UIPreviewPresentationContainerView layoutSubviews];
-[_UIPreviewPresentationContainerView setCornerRadius:];
-[_UIPreviewPresentationContainerView blurRadius];
-[_UIPreviewPresentationContainerView cornerRadius];
-[_UIPreviewPresentationContainerView contentView];
-[_UIPreviewPresentationContainerView preferredContentSize];
-[_UIPreviewPresentationContainerView setBlurRadius:];
-[_UIPreviewPresentationContainerView initWithFrame:];
-[_UIPreviewPresentationContainerView _preferredPlatterRectForContainerRect:];
-[_UIPreviewPresentationContainerView _shouldEnclosedScrollViewFlashIndicators:];
-[_UIPreviewPresentationContainerView _standardPreferredContentSize];
-[_UIPreviewPresentationContainerView contentTransformView];
-[_UIPreviewPresentationContainerView initPlatterViewsIfNeeded];
-[_UIPreviewPresentationContainerView platterClippingView];
-[_UIPreviewPresentationContainerView platterShadowView];
-[_UIPreviewPresentationContainerView setContentTransformView:];
-[_UIPreviewPresentationContainerView setPlatterClippingView:];
-[_UIPreviewPresentationContainerView setPlatterShadowView:];
-[_UIPreviewPresentationContainerView setShouldLayoutForCommitPhase:];
-[_UIPreviewPresentationContainerView setShouldRasterizeForTransition:];
-[_UIPreviewPresentationContainerView shouldLayoutForCommitPhase];
-[_UIPreviewPresentationContainerView shouldRasterizeForTransition];
```
