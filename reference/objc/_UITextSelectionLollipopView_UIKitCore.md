# `_UITextSelectionLollipopView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UITextSelectionWidgetAnimating`, `UITextSelectionHandleView`
- 9 instance variables, 20 properties, 42 instance methods, 1 class methods

## Instance variables

```
B _hiddenForLoupeAnimation;
B _portalsDotToContainerWindow;
B _engaged;
Q _direction;
@"UIBezierPath" _customShape;
d _shapeScale;
@"_UIContainerWindowPortalInteraction" _dotPortalInteraction;
@"UIView" _stemView;
@"UIView" _dotView;
```

## Properties

```
@property (T@"_UIContainerWindowPortalInteraction",&,N,V_dotPortalInteraction) dotPortalInteraction;
@property (TB,N,V_portalsDotToContainerWindow) portalsDotToContainerWindow;
@property (TB,N,GisEngaged,V_engaged) engaged;
@property (Td,N,S_setShapeScale:,V_shapeScale) _shapeScale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) dotViewFrame;
@property (T@"UIView",&,N,V_stemView) stemView;
@property (T@"UIView",&,N,V_dotView) dotView;
@property (T@"UIView",R,N) originView;
@property (T{?={CGPoint=dd}{CGRect={CGPoint=dd}{CGSize=dd}}d@},R,N) originShape;
@property (T{?=@dd{CGSize=dd}},R,N) originShadow;
@property (TB,N,V_hiddenForLoupeAnimation) hiddenForLoupeAnimation;
@property (TB,R,N) crossfadeOnDismissal;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_direction) direction;
@property (TB,R,N,GisVertical) vertical;
@property (T@"UIBezierPath",&,N,V_customShape) customShape;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
```

## Class methods

```
+[_UITextSelectionLollipopView _visualStyle];
```

## Instance methods

```
-[_UITextSelectionLollipopView originView];
-[_UITextSelectionLollipopView setHidden:];
-[_UITextSelectionLollipopView originShape:];
-[_UITextSelectionLollipopView visualStyle];
-[_UITextSelectionLollipopView _setShapeScale:];
-[_UITextSelectionLollipopView isVertical];
-[_UITextSelectionLollipopView originShape];
-[_UITextSelectionLollipopView setDirection:];
-[_UITextSelectionLollipopView layoutSubviews];
-[_UITextSelectionLollipopView crossfadeOnDismissal];
-[_UITextSelectionLollipopView direction];
-[_UITextSelectionLollipopView tintColorDidChange];
-[_UITextSelectionLollipopView accessibilityIdentifier];
-[_UITextSelectionLollipopView originShadow];
-[_UITextSelectionLollipopView setHiddenForLoupeAnimation:];
-[_UITextSelectionLollipopView pointInside:withEvent:];
-[_UITextSelectionLollipopView hiddenForLoupeAnimation];
-[_UITextSelectionLollipopView initWithFrame:];
-[_UITextSelectionLollipopView _shapeScale];
-[_UITextSelectionLollipopView _layoutStemView];
-[_UITextSelectionLollipopView dotView];
-[_UITextSelectionLollipopView setPortalsDotToContainerWindow:];
-[_UITextSelectionLollipopView setCustomShape:];
-[_UITextSelectionLollipopView _configuredStemPoint];
-[_UITextSelectionLollipopView _dotCenterForDotBounds:stemPoint:];
-[_UITextSelectionLollipopView _dotSize];
-[_UITextSelectionLollipopView _layoutDotView];
-[_UITextSelectionLollipopView _requiresHitTestForDownstreamExternalHitTestIDs];
-[_UITextSelectionLollipopView _updateFillColorsForTintColor:];
-[_UITextSelectionLollipopView _usePlainViewForStemView];
-[_UITextSelectionLollipopView _useShapeViewForStemView];
-[_UITextSelectionLollipopView customShape];
-[_UITextSelectionLollipopView dotPortalInteraction];
-[_UITextSelectionLollipopView dotViewFrame];
-[_UITextSelectionLollipopView isEngaged];
-[_UITextSelectionLollipopView portalsDotToContainerWindow];
-[_UITextSelectionLollipopView preferredFrameForRect:];
-[_UITextSelectionLollipopView setDotPortalInteraction:];
-[_UITextSelectionLollipopView setDotView:];
-[_UITextSelectionLollipopView setEngaged:];
-[_UITextSelectionLollipopView setStemView:];
-[_UITextSelectionLollipopView stemView];
```
