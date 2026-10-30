# `LAUIPhysicalButtonView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 23 instance variables, 10 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _export;
B _disablePortraitWorkaround;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originalFrame;
B _exporting;
@"<SBSHardwareButtonHintViewContentVisibilityControlling><BSInvalidatable>" _exportedHandle;
Q _visibilityAnimationCount;
B _indeterminateFrame;
@"<UICoordinateSpace>" _fixedCoordinateSpace;
@"<UICoordinateSpace>" _coordinateSpace;
I _edge;
B _onScreen;
@"UIView" _containerView;
@"LAUIPhysicalButtonLabel" _instructionLabel;
@"UIView" _buttonView;
B _animating;
@"LAUIPhysicalButtonViewAnimation" _animation;
B _workaroundsDisabled;
q _lastInterfaceOrientation;
B _isInstructionHidden;
q _style;
q _animationStyle;
@"NSString" _instruction;
d _inset;
```

## Properties

```
@property (Tq,N,V_style) style;
@property (Tq,N,V_animationStyle) animationStyle;
@property (TB,N,GisAnimating,V_animating) animating;
@property (TB,R,N,GwillPortal) portal;
@property (TI,R,N,V_edge) edge;
@property (T@"NSString",C,N,V_instruction) instruction;
@property (TB,N,V_isInstructionHidden) isInstructionHidden;
@property (Td,N,V_inset) inset;
@property (TB,R,N) showsInstructionBackdrop;
@property (T@"UIColor",&,N) instructionBackdropColor;
```

## Instance methods

```
-[LAUIPhysicalButtonView didMoveToWindow];
-[LAUIPhysicalButtonView edge];
-[LAUIPhysicalButtonView _updateFont];
-[LAUIPhysicalButtonView init];
-[LAUIPhysicalButtonView dealloc];
-[LAUIPhysicalButtonView animationStyle];
-[LAUIPhysicalButtonView layoutSubviews];
-[LAUIPhysicalButtonView hitTest:withEvent:];
-[LAUIPhysicalButtonView initWithStyle:];
-[LAUIPhysicalButtonView style];
-[LAUIPhysicalButtonView setStyle:];
-[LAUIPhysicalButtonView contentSizeCategoryDidChange:];
-[LAUIPhysicalButtonView setAnimationStyle:];
-[LAUIPhysicalButtonView pointInside:withEvent:];
-[LAUIPhysicalButtonView _colorForStyle:];
-[LAUIPhysicalButtonView isAnimating];
-[LAUIPhysicalButtonView setAnimating:];
-[LAUIPhysicalButtonView initWithFrame:];
-[LAUIPhysicalButtonView inset];
-[LAUIPhysicalButtonView setInset:];
-[LAUIPhysicalButtonView _updateOnScreen];
-[LAUIPhysicalButtonView setInstruction:];
-[LAUIPhysicalButtonView instruction];
-[LAUIPhysicalButtonView _physicalButtonNormalizedFrame];
-[LAUIPhysicalButtonView updateFrame];
-[LAUIPhysicalButtonView setInstructionBackdropColor:];
-[LAUIPhysicalButtonView setShowsInstructionBackdrop:animated:];
-[LAUIPhysicalButtonView _purgeExportedHandle];
-[LAUIPhysicalButtonView _updateExportState];
-[LAUIPhysicalButtonView disableWorkarounds];
-[LAUIPhysicalButtonView instructionBackdropColor];
-[LAUIPhysicalButtonView interfaceOrientationDidChange:];
-[LAUIPhysicalButtonView isInstructionHidden];
-[LAUIPhysicalButtonView setIsInstructionHidden:];
-[LAUIPhysicalButtonView showsInstructionBackdrop];
-[LAUIPhysicalButtonView willPortal];
```
