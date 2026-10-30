# `_UIPlatterTransformView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _hidesSourceView;
B _forwardsHitTestingToSourceView;
B _matchesAlpha;
B _appliesMinificationFilter;
B _allowsUserInteraction;
B _shouldTakeOwnershipOfSourceView;
@"UITargetedPreview" _sourcePreview;
@"_UIPortalView" _portalView;
@"_UIPortalView" _backgroundPortalView;
@"_UIMorphingPlatterBackgroundCaptureView" _backgroundCaptureView;
```

## Properties

```
@property (T@"_UIPortalView",&,N,V_portalView) portalView;
@property (T@"UIView",R,N) sourceView;
@property (TB,N,V_shouldTakeOwnershipOfSourceView) shouldTakeOwnershipOfSourceView;
@property (T@"_UIPortalView",&,N,V_backgroundPortalView) backgroundPortalView;
@property (T@"_UIMorphingPlatterBackgroundCaptureView",&,N,V_backgroundCaptureView) backgroundCaptureView;
@property (TB,N,V_hidesSourceView) hidesSourceView;
@property (TB,N,V_forwardsHitTestingToSourceView) forwardsHitTestingToSourceView;
@property (TB,N,V_matchesAlpha) matchesAlpha;
@property (TB,N,V_appliesMinificationFilter) appliesMinificationFilter;
@property (TB,N,V_allowsUserInteraction) allowsUserInteraction;
@property (T@"UITargetedPreview",&,N,V_sourcePreview) sourcePreview;
```

## Instance methods

```
-[_UIPlatterTransformView portalView];
-[_UIPlatterTransformView didMoveToWindow];
-[_UIPlatterTransformView setPortalView:];
-[_UIPlatterTransformView hidesSourceView];
-[_UIPlatterTransformView sourcePreview];
-[_UIPlatterTransformView dealloc];
-[_UIPlatterTransformView layoutSubviews];
-[_UIPlatterTransformView setMatchesAlpha:];
-[_UIPlatterTransformView sizeThatFits:];
-[_UIPlatterTransformView setHidesSourceView:];
-[_UIPlatterTransformView setSourcePreview:];
-[_UIPlatterTransformView initWithFrame:];
-[_UIPlatterTransformView allowsUserInteraction];
-[_UIPlatterTransformView matchesAlpha];
-[_UIPlatterTransformView sourceView];
-[_UIPlatterTransformView shouldTakeOwnershipOfSourceView];
-[_UIPlatterTransformView _updateMinificationFilter];
-[_UIPlatterTransformView appliesMinificationFilter];
-[_UIPlatterTransformView backgroundCaptureView];
-[_UIPlatterTransformView backgroundPortalView];
-[_UIPlatterTransformView didTearOffForDrag];
-[_UIPlatterTransformView forwardsHitTestingToSourceView];
-[_UIPlatterTransformView setAllowsUserInteraction:];
-[_UIPlatterTransformView setAppliesMinificationFilter:];
-[_UIPlatterTransformView setBackgroundCaptureView:];
-[_UIPlatterTransformView setBackgroundPortalView:];
-[_UIPlatterTransformView setForwardsHitTestingToSourceView:];
-[_UIPlatterTransformView setShouldTakeOwnershipOfSourceView:];
```
