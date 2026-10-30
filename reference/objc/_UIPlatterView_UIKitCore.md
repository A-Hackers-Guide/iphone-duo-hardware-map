# `_UIPlatterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 28 instance variables, 31 properties, 74 instance methods, 0 class methods

## Instance variables

```
B _lifted;
B _backgroundVisible;
B _shadowVisible;
B _transformAppliedExternally;
B _constrainSize;
B _constrainSizeWhenNotLifted;
B _appliesOriginalRotation;
B _flipped;
B _precisionMode;
B _hasAppliedMasking;
@"_DUIPreview" _preview;
@"UIView" _componentView;
@"_UIDragPreviewShadowProperties" _shadowProperties;
d _orientationRotation;
d _stackRotation;
@"NSValue" _anchorPointValueToAdjustToOnMoveToWindow;
@"UIView" _backgroundView;
@"_UIShapeView" _platterMaskView;
@"_UIShapeView" _portalMaskView;
@"_UIPortalView" _portalView;
@"UIView" _portalWrapperView;
@"UIView" _shadowView;
{CGSize="width"d"height"d} _overrideSize;
{CGPoint="x"d"y"d} _offset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _appliedTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _additionalTransform;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _containerCounterTransform;
```

## Properties

```
@property (T@"UIView",R,N,V_backgroundView) backgroundView;
@property (T@"_UIShapeView",R,N,V_platterMaskView) platterMaskView;
@property (T@"_UIShapeView",R,N,V_portalMaskView) portalMaskView;
@property (T@"_UIPortalView",&,N,V_portalView) portalView;
@property (T@"UIView",R,N,V_portalWrapperView) portalWrapperView;
@property (T@"UIView",R,N,V_shadowView) shadowView;
@property (T{CATransform3D=dddddddddddddddd},N,V_containerCounterTransform) containerCounterTransform;
@property (TB,N,V_hasAppliedMasking) hasAppliedMasking;
@property (T@"_DUIPreview",R,C,N,V_preview) preview;
@property (T@"UIView",W,N) sourceView;
@property (T@"UIView",&,N,V_componentView) componentView;
@property (T@"_UIDragPreviewShadowProperties",&,N,V_shadowProperties) shadowProperties;
@property (T{CGPoint=dd},R,N) badgeLocation;
@property (TB,N,GisLifted,V_lifted) lifted;
@property (TB,N,GisBackgroundVisible,V_backgroundVisible) backgroundVisible;
@property (TB,N,GisShadowVisible,V_shadowVisible) shadowVisible;
@property (TB,N,V_transformAppliedExternally) transformAppliedExternally;
@property (TB,N,V_constrainSize) constrainSize;
@property (TB,N,V_constrainSizeWhenNotLifted) constrainSizeWhenNotLifted;
@property (T{CGSize=dd},N,V_overrideSize) overrideSize;
@property (T{UIEdgeInsets=dddd},R,N,V_contentInsets) contentInsets;
@property (T{CGPoint=dd},R,N) contentOffset;
@property (T{CGPoint=dd},N,V_offset) offset;
@property (Td,N,V_orientationRotation) orientationRotation;
@property (TB,N,V_appliesOriginalRotation) appliesOriginalRotation;
@property (Td,N,V_stackRotation) stackRotation;
@property (T{CGAffineTransform=dddddd},N,V_appliedTransform) appliedTransform;
@property (T{CGAffineTransform=dddddd},N,V_additionalTransform) additionalTransform;
@property (T@"NSValue",&,N,V_anchorPointValueToAdjustToOnMoveToWindow) anchorPointValueToAdjustToOnMoveToWindow;
@property (TB,N,GisFlipped,V_flipped) flipped;
@property (TB,N,V_precisionMode) precisionMode;
```

## Instance methods

```
-[_UIPlatterView preview];
-[_UIPlatterView overrideSize];
-[_UIPlatterView additionalTransform];
-[_UIPlatterView isLifted];
-[_UIPlatterView setOverrideSize:];
-[_UIPlatterView portalView];
-[_UIPlatterView setBackgroundVisible:];
-[_UIPlatterView didMoveToWindow];
-[_UIPlatterView _applyMaskPath:toView:bounds:];
-[_UIPlatterView setPortalView:];
-[_UIPlatterView appliedTransform];
-[_UIPlatterView shadowProperties];
-[_UIPlatterView contentOffset];
-[_UIPlatterView componentView];
-[_UIPlatterView setAppliesOriginalRotation:];
-[_UIPlatterView setFlipped:];
-[_UIPlatterView isShadowVisible];
-[_UIPlatterView precisionMode];
-[_UIPlatterView setShadowProperties:];
-[_UIPlatterView initWithDroppedItem:];
-[_UIPlatterView portalMaskView];
-[_UIPlatterView setOrientationRotation:];
-[_UIPlatterView setLifted:];
-[_UIPlatterView updateTransform];
-[_UIPlatterView transformAppliedExternally];
-[_UIPlatterView initWithDUIPreview:imageComponent:sourceView:];
-[_UIPlatterView setPrecisionMode:];
-[_UIPlatterView stackRotation];
-[_UIPlatterView constrainSize];
-[_UIPlatterView _isLivePreviewContainer];
-[_UIPlatterView targetTransformIncludingAppliedTransform:];
-[_UIPlatterView constrainSizeWhenNotLifted];
-[_UIPlatterView scaleTransform];
-[_UIPlatterView initialBadgeLocation];
-[_UIPlatterView sizeThatFits:];
-[_UIPlatterView setConstrainSize:];
-[_UIPlatterView targetTransform];
-[_UIPlatterView portalWrapperView];
-[_UIPlatterView isBackgroundVisible];
-[_UIPlatterView containerCounterTransform];
-[_UIPlatterView _updateShadowViewState];
-[_UIPlatterView _hasRadiosityShadow];
-[_UIPlatterView setStackRotation:];
-[_UIPlatterView anchorPointValueToAdjustToOnMoveToWindow];
-[_UIPlatterView _configureRadiosityShadowIfNeededWithSourceView:];
-[_UIPlatterView setHasAppliedMasking:];
-[_UIPlatterView isFlipped];
-[_UIPlatterView setContainerCounterTransform:];
-[_UIPlatterView shadowView];
-[_UIPlatterView scaleFactor];
-[_UIPlatterView platterMaskView];
-[_UIPlatterView setSourceView:];
-[_UIPlatterView contentInsets];
-[_UIPlatterView badgeLocation];
-[_UIPlatterView setComponentView:];
-[_UIPlatterView backgroundView];
-[_UIPlatterView _isEligibleForFocusOcclusion];
-[_UIPlatterView hasAppliedMasking];
-[_UIPlatterView setTransformAppliedExternally:];
-[_UIPlatterView setAppliedTransform:];
-[_UIPlatterView appliesOriginalRotation];
-[_UIPlatterView setOffset:];
-[_UIPlatterView initWithDUIPreview:];
-[_UIPlatterView pointInside:withEvent:];
-[_UIPlatterView takeCounterTransformsToAddToContainer:];
-[_UIPlatterView setConstrainSizeWhenNotLifted:];
-[_UIPlatterView didMoveToSuperview];
-[_UIPlatterView setAnchorPointValueToAdjustToOnMoveToWindow:];
-[_UIPlatterView setShadowVisible:];
-[_UIPlatterView orientationRotation];
-[_UIPlatterView offset];
-[_UIPlatterView setAdditionalTransform:];
-[_UIPlatterView _updateMasking];
-[_UIPlatterView sourceView];
```
