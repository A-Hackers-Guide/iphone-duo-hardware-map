# `TPLCDTextView`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 15 instance variables, 0 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSString" _text;
@"UIFont" _font;
@"UIColor" _shadowColor;
@"UIColor" _textColor;
@"TPLCDTextViewScrollingView" _scrollingView;
d _fontSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _textRect;
@ _delegate;
d _minFontSize;
b1 _textRectIsValid;
b1 _centerText;
b1 _animates;
b1 _isAnimating;
b1 _leftTruncates;
@"UIFrameAnimation" _animation;
```

## Class methods

```
+[TPLCDTextView defaultMinimumFontSize];
```

## Instance methods

```
-[TPLCDTextView stopAnimating];
-[TPLCDTextView startAnimating];
-[TPLCDTextView text];
-[TPLCDTextView sizeToFit];
-[TPLCDTextView dealloc];
-[TPLCDTextView drawRect:];
-[TPLCDTextView setTextColor:];
-[TPLCDTextView setDelegate:];
-[TPLCDTextView setMinimumFontSize:];
-[TPLCDTextView setFrame:];
-[TPLCDTextView setText:];
-[TPLCDTextView setShadowColor:];
-[TPLCDTextView setCenterText:];
-[TPLCDTextView initWithFrame:];
-[TPLCDTextView setFont:];
-[TPLCDTextView _tearDownAnimation];
-[TPLCDTextView animates];
-[TPLCDTextView textRect];
-[TPLCDTextView _startScrolling];
-[TPLCDTextView setLCDTextFont:];
-[TPLCDTextView _drawTextInRect:verticallyOffset:];
-[TPLCDTextView _finishedScrolling];
-[TPLCDTextView _scheduleStartScrolling];
-[TPLCDTextView _setupForAnimationIfNecessary];
-[TPLCDTextView resetAnimation];
-[TPLCDTextView setAnimatesIfTruncated:];
-[TPLCDTextView setLeftTruncatesText:];
```
