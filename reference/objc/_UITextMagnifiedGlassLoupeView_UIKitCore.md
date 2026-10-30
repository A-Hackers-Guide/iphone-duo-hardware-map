# `_UITextMagnifiedGlassLoupeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UITextLoupeView`
- 19 instance variables, 21 properties, 51 instance methods, 2 class methods

## Instance variables

```
@"_UIGroupCompletion" _transitionGroupCompletion;
B _closeLoupeAnimationRunning;
@"_UIPortalView" _contentOffsetPortalView;
@"UIView" _contentOffsetPortalContainerView;
B _visible;
{?="apertureOpen"B"floatingAbove"B} _animationState;
d _dismissalProgress;
@"UIView<_UITextSelectionWidgetAnimating>" _animatableSelectionWidget;
Q _orientation;
@"CADisplayLink" _displayLink;
@"UIView" _portalContainerView;
@"UIView" _containerView;
@"UIView" _glassView;
@"UIView" _innerShadowView;
@"UIView" _highlightView;
@"UIView" _highlightDarkView;
@"UIView" _highlightLightView;
@"_UIPortalView" _portalView;
{CGPoint="x"d"y"d} _modelPosition;
```

## Properties

```
@property (T{?=BB},N,V_animationState) animationState;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@"UIView",&,N,V_portalContainerView) portalContainerView;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_glassView) glassView;
@property (T@"UIView",&,N,V_innerShadowView) innerShadowView;
@property (T@"UIView",&,N,V_highlightView) highlightView;
@property (T@"UIView",&,N,V_highlightDarkView) highlightDarkView;
@property (T@"UIView",&,N,V_highlightLightView) highlightLightView;
@property (T@"_UIPortalView",&,N,V_portalView) portalView;
@property (T@"UIView<_UITextSelectionWidgetAnimating>",W,N,V_animatableSelectionWidget) animatableSelectionWidget;
@property (TQ,N,V_orientation) orientation;
@property (T{CGSize=dd},R,N) preferredSize;
@property (T@"<UICoordinateSpace>",R,N) containerCoordinateSpace;
@property (TB,N,V_visible) visible;
@property (Td,N,V_dismissalProgress) dismissalProgress;
@property (T{CGPoint=dd},N,V_modelPosition) modelPosition;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITextMagnifiedGlassLoupeView loupeZoomOutScale];
+[_UITextMagnifiedGlassLoupeView loupeZoomScale];
```

## Instance methods

```
-[_UITextMagnifiedGlassLoupeView animationState];
-[_UITextMagnifiedGlassLoupeView _displayLinkFired:];
-[_UITextMagnifiedGlassLoupeView displayLink];
-[_UITextMagnifiedGlassLoupeView setOrientation:];
-[_UITextMagnifiedGlassLoupeView portalView];
-[_UITextMagnifiedGlassLoupeView setContainerView:];
-[_UITextMagnifiedGlassLoupeView visible];
-[_UITextMagnifiedGlassLoupeView setPortalView:];
-[_UITextMagnifiedGlassLoupeView setHighlightView:];
-[_UITextMagnifiedGlassLoupeView setVisible:];
-[_UITextMagnifiedGlassLoupeView setModelPosition:];
-[_UITextMagnifiedGlassLoupeView orientation];
-[_UITextMagnifiedGlassLoupeView initWithSourceView:];
-[_UITextMagnifiedGlassLoupeView layoutSubviews];
-[_UITextMagnifiedGlassLoupeView setDisplayLink:];
-[_UITextMagnifiedGlassLoupeView containerView];
-[_UITextMagnifiedGlassLoupeView removeFromSuperview];
-[_UITextMagnifiedGlassLoupeView setAnimationState:];
-[_UITextMagnifiedGlassLoupeView didMoveToSuperview];
-[_UITextMagnifiedGlassLoupeView _isVertical];
-[_UITextMagnifiedGlassLoupeView highlightView];
-[_UITextMagnifiedGlassLoupeView preferredSize];
-[_UITextMagnifiedGlassLoupeView _stopDisplayLink];
-[_UITextMagnifiedGlassLoupeView innerShadowView];
-[_UITextMagnifiedGlassLoupeView needsHideLoupe:];
-[_UITextMagnifiedGlassLoupeView setVisible:animated:completion:];
-[_UITextMagnifiedGlassLoupeView _animatableSelectionWidget];
-[_UITextMagnifiedGlassLoupeView _applyClearGlassBackgroundToSubview:];
-[_UITextMagnifiedGlassLoupeView _configuredGroupCompletion:];
-[_UITextMagnifiedGlassLoupeView _defaultOriginShape];
-[_UITextMagnifiedGlassLoupeView _resetAnimationState];
-[_UITextMagnifiedGlassLoupeView _updateCloseLoupeAnimation:];
-[_UITextMagnifiedGlassLoupeView _updateOpenLoupeAnimation:];
-[_UITextMagnifiedGlassLoupeView _updatePortalViewTransformForPosition:zoomScale:];
-[_UITextMagnifiedGlassLoupeView animatableSelectionWidget];
-[_UITextMagnifiedGlassLoupeView configureHighlightAndShadow];
-[_UITextMagnifiedGlassLoupeView constrainedModelPositionForPosition:];
-[_UITextMagnifiedGlassLoupeView containerCoordinateSpace];
-[_UITextMagnifiedGlassLoupeView dismissalProgress];
-[_UITextMagnifiedGlassLoupeView glassView];
-[_UITextMagnifiedGlassLoupeView highlightDarkView];
-[_UITextMagnifiedGlassLoupeView highlightLightView];
-[_UITextMagnifiedGlassLoupeView modelPosition];
-[_UITextMagnifiedGlassLoupeView portalContainerView];
-[_UITextMagnifiedGlassLoupeView setAnimatableSelectionWidget:];
-[_UITextMagnifiedGlassLoupeView setDismissalProgress:];
-[_UITextMagnifiedGlassLoupeView setGlassView:];
-[_UITextMagnifiedGlassLoupeView setHighlightDarkView:];
-[_UITextMagnifiedGlassLoupeView setHighlightLightView:];
-[_UITextMagnifiedGlassLoupeView setInnerShadowView:];
-[_UITextMagnifiedGlassLoupeView setPortalContainerView:];
```
