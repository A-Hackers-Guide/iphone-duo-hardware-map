# `_UIMorphingPlatterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIMorphPlatterViewBase`
- 14 instance variables, 15 properties, 64 instance methods, 0 class methods

## Instance variables

```
B _allowsElasticMorph;
B _frozen;
B _contentSizeDidChange;
d _overrideCollapsedCornerRadius;
d _overrideExpandedCornerRadius;
@"_UIPlatterClippingView" _collapsedClippingView;
@"_UIPlatterTransformView" _collapsedTransformView;
@"_UIPlatterClippingView" _expandedClippingView;
@"_UIPlatterTransformView" _expandedTransformView;
@"NSMutableDictionary" _shadowViews;
@"_UIPlatterSoftShadowView" _pathShadowView;
@"_UIMorphingPlatterAnimatableFloat" _expansionProgress;
@"_UIMorphingPlatterAnimatableFloat" _platterWidth;
@"_UIMorphingPlatterAnimatableFloat" _platterHeight;
```

## Properties

```
@property (T@"_UIPlatterClippingView",&,N,V_collapsedClippingView) collapsedClippingView;
@property (T@"_UIPlatterTransformView",&,N,V_collapsedTransformView) collapsedTransformView;
@property (T@"_UIPlatterClippingView",&,N,V_expandedClippingView) expandedClippingView;
@property (T@"_UIPlatterTransformView",&,N,V_expandedTransformView) expandedTransformView;
@property (T@"NSMutableDictionary",&,N,V_shadowViews) shadowViews;
@property (T@"_UIPlatterSoftShadowView",&,N,V_pathShadowView) pathShadowView;
@property (TB,N,GisFrozen,V_frozen) frozen;
@property (TB,N,V_contentSizeDidChange) contentSizeDidChange;
@property (T@"_UIMorphingPlatterAnimatableFloat",&,N,V_expansionProgress) expansionProgress;
@property (T@"_UIMorphingPlatterAnimatableFloat",&,N,V_platterWidth) platterWidth;
@property (T@"_UIMorphingPlatterAnimatableFloat",&,N,V_platterHeight) platterHeight;
@property (TB,R,N) bothViewsAreLikelyOpaque;
@property (TB,N,V_allowsElasticMorph) allowsElasticMorph;
@property (Td,N,V_overrideCollapsedCornerRadius) overrideCollapsedCornerRadius;
@property (Td,N,V_overrideExpandedCornerRadius) overrideExpandedCornerRadius;
```

## Instance methods

```
-[_UIMorphingPlatterView isFrozen];
-[_UIMorphingPlatterView setFrozen:];
-[_UIMorphingPlatterView setExpanded:];
-[_UIMorphingPlatterView contentSizeDidChange];
-[_UIMorphingPlatterView layoutSubviews];
-[_UIMorphingPlatterView setPreventPreviewRasterization:];
-[_UIMorphingPlatterView initWithFrame:];
-[_UIMorphingPlatterView updateContentSize];
-[_UIMorphingPlatterView setShadowViews:];
-[_UIMorphingPlatterView _collapsedCornerRadius:maskedCorners:];
-[_UIMorphingPlatterView _collapsedShadowAlphaForExpansionProgress:];
-[_UIMorphingPlatterView _expandedCornerRadius:maskedCorners:ignoreLiftScale:];
-[_UIMorphingPlatterView _expandedShadowAlphaForExpansionProgress:];
-[_UIMorphingPlatterView _installPreview:inClippingView:transformView:];
-[_UIMorphingPlatterView _installShadowViewForStyleIfNecessary:];
-[_UIMorphingPlatterView _modelUpdates];
-[_UIMorphingPlatterView _prepareAnimatableProperties];
-[_UIMorphingPlatterView _previewPrefersApplyingMask:];
-[_UIMorphingPlatterView _updateClippingViews];
-[_UIMorphingPlatterView _updateCollapsedChrome];
-[_UIMorphingPlatterView _updatePathShadow];
-[_UIMorphingPlatterView _updatePathShadowTransform];
-[_UIMorphingPlatterView _updateShadowsWithExpansionProgress:contentBounds:center:forPresentation:];
-[_UIMorphingPlatterView allowsElasticMorph];
-[_UIMorphingPlatterView allowsUserInteractionInExpandedPreview];
-[_UIMorphingPlatterView bothViewsAreLikelyOpaque];
-[_UIMorphingPlatterView collapsedClippingView];
-[_UIMorphingPlatterView collapsedTransformView];
-[_UIMorphingPlatterView didTearOffForDrag];
-[_UIMorphingPlatterView expandedClippingView];
-[_UIMorphingPlatterView expandedTransformView];
-[_UIMorphingPlatterView expansionProgress];
-[_UIMorphingPlatterView freezeExpandedPreview];
-[_UIMorphingPlatterView hidesCollapsedSourceView];
-[_UIMorphingPlatterView overrideCollapsedCornerRadius];
-[_UIMorphingPlatterView overrideExpandedCornerRadius];
-[_UIMorphingPlatterView pathShadowView];
-[_UIMorphingPlatterView platterHeight];
-[_UIMorphingPlatterView platterWidth];
-[_UIMorphingPlatterView setAllowsElasticMorph:];
-[_UIMorphingPlatterView setAllowsUserInteractionInExpandedPreview:];
-[_UIMorphingPlatterView setAlwaysCompact:];
-[_UIMorphingPlatterView setCollapsedClippingView:];
-[_UIMorphingPlatterView setCollapsedPreview:];
-[_UIMorphingPlatterView setCollapsedShadowIntensity:];
-[_UIMorphingPlatterView setCollapsedShadowStyle:];
-[_UIMorphingPlatterView setCollapsedTransformView:];
-[_UIMorphingPlatterView setContentSizeDidChange:];
-[_UIMorphingPlatterView setExpandedClippingView:];
-[_UIMorphingPlatterView setExpandedPreview:];
-[_UIMorphingPlatterView setExpandedShadowIntensity:];
-[_UIMorphingPlatterView setExpandedShadowStyle:];
-[_UIMorphingPlatterView setExpandedTransformView:];
-[_UIMorphingPlatterView setExpansionProgress:];
-[_UIMorphingPlatterView setHideChromeWhenCollapsed:];
-[_UIMorphingPlatterView setHidesCollapsedSourceView:];
-[_UIMorphingPlatterView setOverrideCollapsedCornerRadius:];
-[_UIMorphingPlatterView setOverrideExpandedCornerRadius:];
-[_UIMorphingPlatterView setPathShadowView:];
-[_UIMorphingPlatterView setPlatterHeight:];
-[_UIMorphingPlatterView setPlatterWidth:];
-[_UIMorphingPlatterView setWantsEdgeAntialiasing:];
-[_UIMorphingPlatterView shadowViews];
-[_UIMorphingPlatterView wantsEdgeAntialiasing];
```
