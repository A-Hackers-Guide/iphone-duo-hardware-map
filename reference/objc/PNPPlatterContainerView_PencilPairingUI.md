# `PNPPlatterContainerView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"UIView" _contentViewContainerView;
@"PNPPlatterShadowView" _shadowView;
@"UIView" _dimmingView;
@"UIVisualEffectView" _effectView;
B _presented;
B _dismissUsingAlpha;
@"UIView" _contentView;
@? _autoDismissBlock;
@"NSDate" _autoDismissDate;
Q _edge;
d _preferredCornerRadius;
q _dimmingState;
d _pencilOffset;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _animationTranslation;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@?,C,N,V_autoDismissBlock) autoDismissBlock;
@property (T@"NSDate",&,N,V_autoDismissDate) autoDismissDate;
@property (TQ,N,V_edge) edge;
@property (Td,N,V_preferredCornerRadius) preferredCornerRadius;
@property (TB,N,V_presented) presented;
@property (Tq,N,V_dimmingState) dimmingState;
@property (Td,N,V_pencilOffset) pencilOffset;
@property (TB,N,V_dismissUsingAlpha) dismissUsingAlpha;
@property (T{CGAffineTransform=dddddd},N,V_animationTranslation) animationTranslation;
```

## Instance methods

```
-[PNPPlatterContainerView setEdge:];
-[PNPPlatterContainerView setPreferredCornerRadius:];
-[PNPPlatterContainerView setContentView:];
-[PNPPlatterContainerView edge];
-[PNPPlatterContainerView layoutSubviews];
-[PNPPlatterContainerView hitTest:withEvent:];
-[PNPPlatterContainerView animationTranslation];
-[PNPPlatterContainerView preferredCornerRadius];
-[PNPPlatterContainerView contentView];
-[PNPPlatterContainerView setAnimationTranslation:];
-[PNPPlatterContainerView initWithFrame:];
-[PNPPlatterContainerView presented];
-[PNPPlatterContainerView dimmingState];
-[PNPPlatterContainerView setDimmingState:];
-[PNPPlatterContainerView setPresented:];
-[PNPPlatterContainerView initDimmingView];
-[PNPPlatterContainerView autoDismissDate];
-[PNPPlatterContainerView _dismissedAlphaForEdge:];
-[PNPPlatterContainerView _dismissedTransformForEdge:];
-[PNPPlatterContainerView _updateShadowForCenteredPlatter:];
-[PNPPlatterContainerView autoDismissBlock];
-[PNPPlatterContainerView dismissUsingAlpha];
-[PNPPlatterContainerView dismissedFrameForViewWithSize:edge:inRect:];
-[PNPPlatterContainerView initEffectView];
-[PNPPlatterContainerView initShadowView];
-[PNPPlatterContainerView pencilOffset];
-[PNPPlatterContainerView presentedFrameForViewWithSize:edge:inRect:];
-[PNPPlatterContainerView setAutoDismissBlock:];
-[PNPPlatterContainerView setAutoDismissDate:];
-[PNPPlatterContainerView setDismissUsingAlpha:];
-[PNPPlatterContainerView setPencilOffset:];
```
