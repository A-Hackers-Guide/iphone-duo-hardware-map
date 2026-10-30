# `SBSwitcherHiddenWindowsPillView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 21 instance variables, 15 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"UIView" _glassView;
@"UIView" _contentView;
@"UIView" _leadingAccessoryView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
@"SBGradientView" _maskView;
@"UIImageView" _chevronView;
@"UIViewFloatAnimatableProperty" _maskProgressAnimatableProperty;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"UIPanGestureRecognizer" _swipeToDismissGestureRecognizer;
@"SBSwitcherHiddenWindowsPill" _hiddenWindowsPill;
@"<SBSwitcherHiddenWindowsPillViewDelegate>" _delegate;
q _pillMode;
d _pillScale;
d _pillScaleY;
d _contentAlpha;
d _contentScale;
d _contentScaleY;
d _contentBlurRadius;
Q _background;
{CGPoint="x"d"y"d} _pillOffset;
```

## Properties

```
@property (T@"SBSwitcherHiddenWindowsPill",R,N,V_hiddenWindowsPill) hiddenWindowsPill;
@property (T@"<SBSwitcherHiddenWindowsPillViewDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,N,V_pillMode) pillMode;
@property (T{CGPoint=dd},N,V_pillOffset) pillOffset;
@property (Td,N,V_pillScale) pillScale;
@property (Td,N,V_pillScaleY) pillScaleY;
@property (Td,N,V_contentAlpha) contentAlpha;
@property (Td,N,V_contentScale) contentScale;
@property (Td,N,V_contentScaleY) contentScaleY;
@property (Td,N,V_contentBlurRadius) contentBlurRadius;
@property (TQ,N,V_background) background;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherHiddenWindowsPillView intrinsicContentSize];
-[SBSwitcherHiddenWindowsPillView contentAlpha];
-[SBSwitcherHiddenWindowsPillView setBackground:];
-[SBSwitcherHiddenWindowsPillView _handleTap:];
-[SBSwitcherHiddenWindowsPillView setContentAlpha:];
-[SBSwitcherHiddenWindowsPillView dealloc];
-[SBSwitcherHiddenWindowsPillView layoutSubviews];
-[SBSwitcherHiddenWindowsPillView background];
-[SBSwitcherHiddenWindowsPillView updateProperties];
-[SBSwitcherHiddenWindowsPillView sizeThatFits:];
-[SBSwitcherHiddenWindowsPillView accessibilityIdentifier];
-[SBSwitcherHiddenWindowsPillView gestureRecognizerShouldBegin:];
-[SBSwitcherHiddenWindowsPillView setContentScale:];
-[SBSwitcherHiddenWindowsPillView contentScale];
-[SBSwitcherHiddenWindowsPillView delegate];
-[SBSwitcherHiddenWindowsPillView didMoveToSuperview];
-[SBSwitcherHiddenWindowsPillView contentScaleY];
-[SBSwitcherHiddenWindowsPillView setContentScaleY:];
-[SBSwitcherHiddenWindowsPillView contentBlurRadius];
-[SBSwitcherHiddenWindowsPillView setContentBlurRadius:];
-[SBSwitcherHiddenWindowsPillView _makeTitleLabel];
-[SBSwitcherHiddenWindowsPillView _effectiveGlassViewMaterial];
-[SBSwitcherHiddenWindowsPillView _handleSwipeToDismiss:];
-[SBSwitcherHiddenWindowsPillView _makeChevronView];
-[SBSwitcherHiddenWindowsPillView _makeContentView];
-[SBSwitcherHiddenWindowsPillView _makeGlass];
-[SBSwitcherHiddenWindowsPillView _makeGlassView];
-[SBSwitcherHiddenWindowsPillView _makeMaskProgressAnimatableProperty];
-[SBSwitcherHiddenWindowsPillView _makeMaskView];
-[SBSwitcherHiddenWindowsPillView _makeSubtitleLabel];
-[SBSwitcherHiddenWindowsPillView hiddenWindowsPill];
-[SBSwitcherHiddenWindowsPillView initWithHiddenWindowsPill:delegate:];
-[SBSwitcherHiddenWindowsPillView pillMode];
-[SBSwitcherHiddenWindowsPillView pillOffset];
-[SBSwitcherHiddenWindowsPillView pillScale];
-[SBSwitcherHiddenWindowsPillView pillScaleY];
-[SBSwitcherHiddenWindowsPillView setPillMode:];
-[SBSwitcherHiddenWindowsPillView setPillOffset:];
-[SBSwitcherHiddenWindowsPillView setPillScale:];
-[SBSwitcherHiddenWindowsPillView setPillScaleY:];
-[SBSwitcherHiddenWindowsPillView sizeForMode:];
-[SBSwitcherHiddenWindowsPillView sizeForMode:withContentSizeCategory:];
```
