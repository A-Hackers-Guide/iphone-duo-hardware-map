# `UIKeyboardCandidateInlineFloatingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 12 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _reducedWidth;
B _tewObserverIsSet;
B _inlineRectIsVertical;
i _position;
i _adjustMode;
@"NSString" _inlineText;
d _maxX;
d _extendedStateAdditionalHeight;
{CGSize="width"d"height"d} _preferredSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inlineRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previousCollapsedFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _extraInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _cellPadding;
```

## Properties

```
@property (T@"NSString",C,N,V_inlineText) inlineText;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inlineRect) inlineRect;
@property (TB,N,V_inlineRectIsVertical) inlineRectIsVertical;
@property (Td,N,V_maxX) maxX;
@property (Td,N,V_extendedStateAdditionalHeight) extendedStateAdditionalHeight;
@property (T{CGSize=dd},N,V_preferredSize) preferredSize;
@property (TB,R,N,GisReducedWidth,V_reducedWidth) reducedWidth;
@property (Ti,N,V_position) position;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_previousCollapsedFrame) previousCollapsedFrame;
@property (Ti,N,V_adjustMode) adjustMode;
@property (T{UIEdgeInsets=dddd},N,V_extraInsets) extraInsets;
@property (T{UIEdgeInsets=dddd},N,V_cellPadding) cellPadding;
```

## Instance methods

```
-[UIKeyboardCandidateInlineFloatingView position];
-[UIKeyboardCandidateInlineFloatingView traitCollection];
-[UIKeyboardCandidateInlineFloatingView dealloc];
-[UIKeyboardCandidateInlineFloatingView layoutSubviews];
-[UIKeyboardCandidateInlineFloatingView inlineRectIsVertical];
-[UIKeyboardCandidateInlineFloatingView inlineText];
-[UIKeyboardCandidateInlineFloatingView inlineRect];
-[UIKeyboardCandidateInlineFloatingView setInlineRect:];
-[UIKeyboardCandidateInlineFloatingView setInlineText:];
-[UIKeyboardCandidateInlineFloatingView setPreferredSize:];
-[UIKeyboardCandidateInlineFloatingView setInlineRectIsVertical:];
-[UIKeyboardCandidateInlineFloatingView setPosition:];
-[UIKeyboardCandidateInlineFloatingView pointInside:withEvent:];
-[UIKeyboardCandidateInlineFloatingView initWithFrame:];
-[UIKeyboardCandidateInlineFloatingView preferredSize];
-[UIKeyboardCandidateInlineFloatingView setCellPadding:];
-[UIKeyboardCandidateInlineFloatingView setExtraInsets:];
-[UIKeyboardCandidateInlineFloatingView adjustFrameForInlineText:inlineRect:maxX:];
-[UIKeyboardCandidateInlineFloatingView adjustMode];
-[UIKeyboardCandidateInlineFloatingView adjustedFrameFromDesiredFrame:textHeight:];
-[UIKeyboardCandidateInlineFloatingView adjustedFrameFromDesiredFrame:textWidth:];
-[UIKeyboardCandidateInlineFloatingView adjustedInlineRectFromInlineText:inlineRect:];
-[UIKeyboardCandidateInlineFloatingView cellPadding];
-[UIKeyboardCandidateInlineFloatingView extendedStateAdditionalHeight];
-[UIKeyboardCandidateInlineFloatingView extraInsets];
-[UIKeyboardCandidateInlineFloatingView isAcceptableFrame:afterScrollBy:];
-[UIKeyboardCandidateInlineFloatingView isReducedWidth];
-[UIKeyboardCandidateInlineFloatingView maxX];
-[UIKeyboardCandidateInlineFloatingView previousCollapsedFrame];
-[UIKeyboardCandidateInlineFloatingView setAdjustMode:];
-[UIKeyboardCandidateInlineFloatingView setExtendedStateAdditionalHeight:];
-[UIKeyboardCandidateInlineFloatingView setInlineText:inlineRect:maxX:layout:];
-[UIKeyboardCandidateInlineFloatingView setMaxX:];
-[UIKeyboardCandidateInlineFloatingView setPreviousCollapsedFrame:];
-[UIKeyboardCandidateInlineFloatingView shouldExtendUpwards];
```
