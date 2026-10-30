# `_UITextMagnifiedLoupeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UITextLoupeView`
- 14 instance variables, 18 properties, 43 instance methods, 2 class methods

## Instance variables

```
@"_UIGroupCompletion" _transitionGroupCompletion;
B _closeLoupeAnimationRunning;
B _visible;
{?="apertureOpen"B"floatingAbove"B} _animationState;
d _dismissalProgress;
@"UIView<_UITextSelectionWidgetAnimating>" _animatableSelectionWidget;
Q _orientation;
@"CADisplayLink" _displayLink;
@"UIView" _portalContainerView;
@"UIView" _containerView;
@"UIView" _glowView;
@"UIView" _coverView;
@"_UIPortalView" _portalView;
{CGPoint="x"d"y"d} _modelPosition;
```

## Properties

```
@property (T{?=BB},N,V_animationState) animationState;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@"UIView",&,N,V_portalContainerView) portalContainerView;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_glowView) glowView;
@property (T@"UIView",&,N,V_coverView) coverView;
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
+[_UITextMagnifiedLoupeView loupeZoomOutScale];
+[_UITextMagnifiedLoupeView loupeZoomScale];
```

## Instance methods

```
-[_UITextMagnifiedLoupeView animationState];
-[_UITextMagnifiedLoupeView _displayLinkFired:];
-[_UITextMagnifiedLoupeView displayLink];
-[_UITextMagnifiedLoupeView setOrientation:];
-[_UITextMagnifiedLoupeView portalView];
-[_UITextMagnifiedLoupeView setContainerView:];
-[_UITextMagnifiedLoupeView visible];
-[_UITextMagnifiedLoupeView setPortalView:];
-[_UITextMagnifiedLoupeView setVisible:];
-[_UITextMagnifiedLoupeView setModelPosition:];
-[_UITextMagnifiedLoupeView orientation];
-[_UITextMagnifiedLoupeView initWithSourceView:];
-[_UITextMagnifiedLoupeView layoutSubviews];
-[_UITextMagnifiedLoupeView setDisplayLink:];
-[_UITextMagnifiedLoupeView containerView];
-[_UITextMagnifiedLoupeView removeFromSuperview];
-[_UITextMagnifiedLoupeView setAnimationState:];
-[_UITextMagnifiedLoupeView _isVertical];
-[_UITextMagnifiedLoupeView preferredSize];
-[_UITextMagnifiedLoupeView _stopDisplayLink];
-[_UITextMagnifiedLoupeView needsHideLoupe:];
-[_UITextMagnifiedLoupeView setVisible:animated:completion:];
-[_UITextMagnifiedLoupeView _animatableSelectionWidget];
-[_UITextMagnifiedLoupeView _configuredGroupCompletion:];
-[_UITextMagnifiedLoupeView _defaultOriginShadow];
-[_UITextMagnifiedLoupeView _defaultOriginShape];
-[_UITextMagnifiedLoupeView _resetAnimationState];
-[_UITextMagnifiedLoupeView _updateCloseLoupeAnimation:];
-[_UITextMagnifiedLoupeView _updateOpenLoupeAnimation:];
-[_UITextMagnifiedLoupeView _updatePortalViewTransformForPosition:zoomScale:];
-[_UITextMagnifiedLoupeView animatableSelectionWidget];
-[_UITextMagnifiedLoupeView constrainedModelPositionForPosition:];
-[_UITextMagnifiedLoupeView containerCoordinateSpace];
-[_UITextMagnifiedLoupeView coverView];
-[_UITextMagnifiedLoupeView dismissalProgress];
-[_UITextMagnifiedLoupeView glowView];
-[_UITextMagnifiedLoupeView modelPosition];
-[_UITextMagnifiedLoupeView portalContainerView];
-[_UITextMagnifiedLoupeView setAnimatableSelectionWidget:];
-[_UITextMagnifiedLoupeView setCoverView:];
-[_UITextMagnifiedLoupeView setDismissalProgress:];
-[_UITextMagnifiedLoupeView setGlowView:];
-[_UITextMagnifiedLoupeView setPortalContainerView:];
```
