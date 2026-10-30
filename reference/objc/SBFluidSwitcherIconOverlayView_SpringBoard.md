# `SBFluidSwitcherIconOverlayView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSUIOrientationTransformWrapperView`
- 10 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIView<SBFSwitcherIconZooming>" _iconOverlayView;
@"UIView" _iconCrossfadeView;
@"UIView" _iconOverlayContainerView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialIconOverlayViewBounds;
@"NSArray" _crossfadeViews;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _crossfadeViewFrame;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _iconCrossfadeC2ThreadLock;
@"UIViewFloatAnimatableProperty" _iconCrossfadeAnimatableProperty;
@"CAMediaTimingFunction" _iconCrossfadeTimingFunction;
d _cornerRadius;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) crossfadeViewFrame;
@property (T@"UIView<SBFSwitcherIconZooming>",R,N) iconView;
@property (Td,N,V_cornerRadius) cornerRadius;
```

## Instance methods

```
-[SBFluidSwitcherIconOverlayView _currentFadeValue];
-[SBFluidSwitcherIconOverlayView initWithIconView:crossfadeViews:crossfadeViewFrame:contentOrientation:containerOrientation:];
-[SBFluidSwitcherIconOverlayView iconView];
-[SBFluidSwitcherIconOverlayView crossfadeViewFrame];
-[SBFluidSwitcherIconOverlayView dealloc];
-[SBFluidSwitcherIconOverlayView layoutSubviews];
-[SBFluidSwitcherIconOverlayView _alphaForIconOverlayView:crossfadeFraction:];
-[SBFluidSwitcherIconOverlayView _applyIconOverlayViewOverlayScaleProperties];
-[SBFluidSwitcherIconOverlayView setCornerRadius:];
-[SBFluidSwitcherIconOverlayView setUpAnimatableProperties];
-[SBFluidSwitcherIconOverlayView invalidate];
-[SBFluidSwitcherIconOverlayView cornerRadius];
-[SBFluidSwitcherIconOverlayView _iconOverlayScale];
-[SBFluidSwitcherIconOverlayView _setCrossfadeViewsAlpha:];
-[SBFluidSwitcherIconOverlayView _setUpIconCrossfadeAnimatableProperty];
-[SBFluidSwitcherIconOverlayView _setUpIconCrossfadeView];
```
