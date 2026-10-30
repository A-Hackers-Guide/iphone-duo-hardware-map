# `UIMorphingLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 27 instance variables, 10 properties, 64 instance methods, 1 class methods

## Instance variables

```
@"UIMorphingLabelGlyphSet" _srcGlyphSet;
@"UIMorphingLabelGlyphSet" _dstGlyphSet;
@"NSMutableArray" _hiddenGlyphViews;
@"UIView" _colorView;
[100Q] _alignmentSrc;
[100Q] _alignmentDst;
[100B] _alignmentIsEqual;
Q _alignmentSize;
[100d] _alignmentDelays;
@"_UIViewAnimationAttributes" _textAnimationAttributes;
d _lastUpdateTime;
d _slowdown;
d _rippleFactor;
d _scaleFactor;
B _isDoingFastAnimation;
B _textDidChange;
B _textColorDidChange;
B _suppressLayoutSubviews;
B _enableAnimation;
@"NSString" _text;
@"UIFont" _font;
@"UIColor" _textColor;
q _textAlignment;
d _initialScale;
d _glyphScaleAnimationSpeed;
d _rippleDuration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleRect;
```

## Properties

```
@property (T@"NSString",C,N,V_text) text;
@property (T@"UIFont",C,N,V_font) font;
@property (T@"UIColor",C,N,V_textColor) textColor;
@property (Tq,N,V_textAlignment) textAlignment;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visibleRect) visibleRect;
@property (TB,N,V_suppressLayoutSubviews) suppressLayoutSubviews;
@property (TB,N,V_enableAnimation) enableAnimation;
@property (Td,N,V_initialScale) initialScale;
@property (Td,N,V_glyphScaleAnimationSpeed) glyphScaleAnimationSpeed;
@property (Td,N,V_rippleDuration) rippleDuration;
```

## Class methods

```
+[UIMorphingLabel preferredFontWithSize:];
```

## Instance methods

```
-[UIMorphingLabel setVisibleRect:];
-[UIMorphingLabel currentMediaTime];
-[UIMorphingLabel setTextAlignment:];
-[UIMorphingLabel _isRTL];
-[UIMorphingLabel visibleRect];
-[UIMorphingLabel initMovementAlignmentHunkAtIndex:];
-[UIMorphingLabel flushAmount];
-[UIMorphingLabel initInsertionAlignmentHunkAtIndex:];
-[UIMorphingLabel textAlignment];
-[UIMorphingLabel text];
-[UIMorphingLabel animateAlignmentHunkAtIndex:];
-[UIMorphingLabel alphaForFrame:];
-[UIMorphingLabel textColor];
-[UIMorphingLabel attributedString];
-[UIMorphingLabel animateInsertionAlignmentHunkAtIndex:];
-[UIMorphingLabel baseInit];
-[UIMorphingLabel animateGlyph:toPosition:delay:];
-[UIMorphingLabel animateShowGlyph:alphaDuration:delay:];
-[UIMorphingLabel animateGlyph:toAlpha:duration:delay:];
-[UIMorphingLabel glyphViewWithImage:isColorGlyph:];
-[UIMorphingLabel contentSizeDidChange:];
-[UIMorphingLabel setTextColor:];
-[UIMorphingLabel canFitText:];
-[UIMorphingLabel initDeletionAlignmentHunkAtIndex:];
-[UIMorphingLabel enableAnimation];
-[UIMorphingLabel layoutSubviews];
-[UIMorphingLabel initAlignmentHunkAtIndex:];
-[UIMorphingLabel glyphScaleAnimationSpeed];
-[UIMorphingLabel dstRangeOfAlignmentHunkAtIndex:];
-[UIMorphingLabel animateHideGlyph:alphaDuration:delay:];
-[UIMorphingLabel initialScale];
-[UIMorphingLabel setInitialScale:];
-[UIMorphingLabel initSubstitutionAlignmentHunkAtIndex:];
-[UIMorphingLabel calculateHardAlignmentAtIndex:fromGlyphsInRange:toGlyphsInRange:];
-[UIMorphingLabel animateGlyph:toScale:delay:];
-[UIMorphingLabel animateChangeInWidthOutsideAlignmentHunkAtIndex:];
-[UIMorphingLabel animateMovementAlignmentHunkAtIndex:];
-[UIMorphingLabel rippleDuration];
-[UIMorphingLabel changeInWidthDueToAlignmentHunkAtIndex:];
-[UIMorphingLabel animateGlyphs];
-[UIMorphingLabel attributedStringForText:];
-[UIMorphingLabel setRippleDuration:];
-[UIMorphingLabel animateShowGlyph:alpha:alphaDuration:delay:];
-[UIMorphingLabel initWithCoder:];
-[UIMorphingLabel setText:];
-[UIMorphingLabel animateDeletionAlignmentHunkAtIndex:];
-[UIMorphingLabel calculateGlyphAlignment];
-[UIMorphingLabel setGlyphScaleAnimationSpeed:];
-[UIMorphingLabel font];
-[UIMorphingLabel hideGlyph:];
-[UIMorphingLabel copyStateFromGlyph:toGlyph:];
-[UIMorphingLabel animateGlyphsInRange:ofGlyphSet:byOffset:delay:];
-[UIMorphingLabel uniqueString];
-[UIMorphingLabel totalLeftOffsetForAlignmentHunkAtIndex:];
-[UIMorphingLabel srcRangeOfAlignmentHunkAtIndex:];
-[UIMorphingLabel totalRightOffsetForAlignmentHunkAtIndex:];
-[UIMorphingLabel requiredWidthForText:];
-[UIMorphingLabel suppressLayoutSubviews];
-[UIMorphingLabel initWithFrame:];
-[UIMorphingLabel animateSubstitutionAlignmentHunkAtIndex:];
-[UIMorphingLabel _rippleDurationForEndInsertion:];
-[UIMorphingLabel setEnableAnimation:];
-[UIMorphingLabel setSuppressLayoutSubviews:];
-[UIMorphingLabel setFont:];
```
