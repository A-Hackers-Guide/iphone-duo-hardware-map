# `_UITextLightLoupeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UITextLoupeView`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"UIView" _sourceView;
@"UIView" _maskView;
@"UIView" _backgroundView;
@"UIView" _glowView;
@"UIView" _portalContainerView;
{CGPoint="x"d"y"d} _modelPosition;
@"CADisplayLink" _displayLink;
@"_UIPortalView" _portalView;
B _visible;
d _dismissalProgress;
```

## Properties

```
@property (T{CGSize=dd},R,N) preferredSize;
@property (T@"<UICoordinateSpace>",R,N) containerCoordinateSpace;
@property (TB,N,V_visible) visible;
@property (Td,N,V_dismissalProgress) dismissalProgress;
@property (T{CGPoint=dd},N,V_modelPosition) modelPosition;
@property (T@"UIView<_UITextSelectionWidgetAnimating>",W,N) animatableSelectionWidget;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextLightLoupeView _displayLinkFired:];
-[_UITextLightLoupeView visible];
-[_UITextLightLoupeView setVisible:];
-[_UITextLightLoupeView setModelPosition:];
-[_UITextLightLoupeView initWithSourceView:];
-[_UITextLightLoupeView layoutSubviews];
-[_UITextLightLoupeView removeFromSuperview];
-[_UITextLightLoupeView preferredSize];
-[_UITextLightLoupeView _stopDisplayLink];
-[_UITextLightLoupeView needsHideLoupe:];
-[_UITextLightLoupeView setVisible:animated:completion:];
-[_UITextLightLoupeView _backgroundColorIfNecessary];
-[_UITextLightLoupeView _updateColorsForCurrentTraitCollection];
-[_UITextLightLoupeView _visualOffset];
-[_UITextLightLoupeView animatableSelectionWidget];
-[_UITextLightLoupeView constrainedModelPositionForPosition:];
-[_UITextLightLoupeView containerCoordinateSpace];
-[_UITextLightLoupeView dismissalProgress];
-[_UITextLightLoupeView modelPosition];
-[_UITextLightLoupeView setAnimatableSelectionWidget:];
-[_UITextLightLoupeView setDismissalProgress:];
```
