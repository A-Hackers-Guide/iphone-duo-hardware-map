# `SBFluidSwitcherButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIPointerInteractionDelegate`
- 8 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"UIView" _backgroundView;
@"UIImageView" _glyphImageView;
@"UIImageView" _xPlusDView;
@"UIView" _highlightView;
@"UIImage" _image;
@"NSString" _backdropGroupName;
q _buttonStyle;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _extendedEdgeInsets;
```

## Properties

```
@property (T@"UIImage",&,N,V_image) image;
@property (T{UIEdgeInsets=dddd},N,V_extendedEdgeInsets) extendedEdgeInsets;
@property (T@"NSString",&,N,V_backdropGroupName) backdropGroupName;
@property (Tq,N,V_buttonStyle) buttonStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherButton pointerInteraction:styleForRegion:];
-[SBFluidSwitcherButton setButtonStyle:];
-[SBFluidSwitcherButton backdropGroupName];
-[SBFluidSwitcherButton layoutSubviews];
-[SBFluidSwitcherButton setBackdropGroupName:];
-[SBFluidSwitcherButton gestureRecognizerShouldBegin:];
-[SBFluidSwitcherButton setHighlighted:];
-[SBFluidSwitcherButton pointerInteraction:regionForRequest:defaultRegion:];
-[SBFluidSwitcherButton _addHighlightViewIfNecessary];
-[SBFluidSwitcherButton image];
-[SBFluidSwitcherButton pointInside:withEvent:];
-[SBFluidSwitcherButton didMoveToSuperview];
-[SBFluidSwitcherButton initWithFrame:];
-[SBFluidSwitcherButton buttonStyle];
-[SBFluidSwitcherButton setImage:];
-[SBFluidSwitcherButton _invalidateBackgroundView];
-[SBFluidSwitcherButton _backgroundMaterialView];
-[SBFluidSwitcherButton _configureBackgroundViewIfNecessaryForStyle:];
-[SBFluidSwitcherButton _configureGlyphImageViewIfNecessaryForStyle:];
-[SBFluidSwitcherButton _configureXPlusDViewIfNecessaryForStyle:];
-[SBFluidSwitcherButton _invalidateXPlusDView];
-[SBFluidSwitcherButton extendedEdgeInsets];
-[SBFluidSwitcherButton setExtendedEdgeInsets:];
```
