# `_UIActionSlider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIGestureRecognizerDelegate`
- 26 instance variables, 28 properties, 77 instance methods, 0 class methods

## Instance variables

```
@"UIView" _contentView;
@"UIView" _trackDodgeView;
@"UIView" _trackBackgroundView;
@"_UIBackdropView" _trackBlurView;
@"UIView" _trackSolidView;
@"_UIActionSliderKnob" _knobView;
@"UIImageView" _knobImageView;
@"UIView<_UIActionSliderLabel>" _trackLabel;
@"UIPanGestureRecognizer" _slideGestureRecognizer;
{CGPoint="x"d"y"d} _slideGestureInitialPoint;
d _knobPosition;
d _trackWidthProportion;
B _showingTrackLabel;
B _animating;
q _style;
q _textStyle;
@"NSString" _trackText;
@"UIFont" _trackFont;
d _trackTextBaselineFromBottom;
@"<_UIActionSliderDelegate>" _delegate;
d _knobWidth;
d _cachedTrackMaskWidth;
@"_UIVibrantSettings" _vibrantSettings;
{CGSize="width"d"height"d} _knobImageOffset;
{CGSize="width"d"height"d} _trackSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _knobInsets;
```

## Properties

```
@property (Td,N,V_trackWidthProportion) trackWidthProportion;
@property (TB,N,GisShowingTrackLabel,V_showingTrackLabel) showingTrackLabel;
@property (TB,N,GisAnimating,V_animating) animating;
@property (Td,N,V_cachedTrackMaskWidth) cachedTrackMaskWidth;
@property (T@"UIView",R,N,G_knobView,V_knobView) knobView;
@property (T@"_UIVibrantSettings",&,N,V_vibrantSettings) vibrantSettings;
@property (Tq,N,V_style) style;
@property (Tq,N,V_textStyle) textStyle;
@property (T@"UIImage",&,N) knobImage;
@property (T@"UIColor",&,N) knobColor;
@property (T{CGSize=dd},N,V_knobImageOffset) knobImageOffset;
@property (T@"NSString",C,N,V_trackText) trackText;
@property (T@"UIFont",&,N,V_trackFont) trackFont;
@property (T{CGSize=dd},N,V_trackSize) trackSize;
@property (Td,N,V_trackTextBaselineFromBottom) trackTextBaselineFromBottom;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) trackTextRect;
@property (T@"UILabel",R,&,N) trackLabel;
@property (T@"UIPanGestureRecognizer",R,N,V_slideGestureRecognizer) slideGestureRecognizer;
@property (T@"<_UIActionSliderDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_knobPosition) knobPosition;
@property (Td,N,V_knobWidth) knobWidth;
@property (T{UIEdgeInsets=dddd},N,V_knobInsets) knobInsets;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) knobRect;
@property (T@"UIBezierPath",R,N) knobMaskPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIActionSlider didMoveToWindow];
-[_UIActionSlider layoutSubviews];
-[_UIActionSlider trackSize];
-[_UIActionSlider style];
-[_UIActionSlider setStyle:];
-[_UIActionSlider setBackgroundColor:];
-[_UIActionSlider sizeThatFits:];
-[_UIActionSlider setDelegate:];
-[_UIActionSlider gestureRecognizerShouldBegin:];
-[_UIActionSlider vibrantSettings];
-[_UIActionSlider delegate];
-[_UIActionSlider backgroundColor];
-[_UIActionSlider setTextStyle:];
-[_UIActionSlider initWithCoder:];
-[_UIActionSlider didMoveToSuperview];
-[_UIActionSlider textStyle];
-[_UIActionSlider isAnimating];
-[_UIActionSlider setAnimating:];
-[_UIActionSlider initWithFrame:];
-[_UIActionSlider setVibrantSettings:];
-[_UIActionSlider _knobAvailableX];
-[_UIActionSlider _knobRightMostX];
-[_UIActionSlider knobImageOffset];
-[_UIActionSlider _makeTrackLabel];
-[_UIActionSlider _showTrackLabel];
-[_UIActionSlider setTrackTextBaselineFromBottom:];
-[_UIActionSlider _hideTrackLabel:];
-[_UIActionSlider _knobHorizontalPosition];
-[_UIActionSlider _knobLeftMostX];
-[_UIActionSlider _knobMaxX];
-[_UIActionSlider _knobMaxXInset];
-[_UIActionSlider _knobMinX];
-[_UIActionSlider _knobMinXInset];
-[_UIActionSlider _knobPanGesture:];
-[_UIActionSlider _knobVerticalInset];
-[_UIActionSlider _knobView];
-[_UIActionSlider _knobWidth];
-[_UIActionSlider _slideCompleted:];
-[_UIActionSlider _trackFrame];
-[_UIActionSlider cachedTrackMaskWidth];
-[_UIActionSlider closeTrackAnimated:];
-[_UIActionSlider initWithFrame:vibrantSettings:];
-[_UIActionSlider isShowingTrackLabel];
-[_UIActionSlider knobColor];
-[_UIActionSlider knobImage];
-[_UIActionSlider knobInsets];
-[_UIActionSlider knobMaskPath];
-[_UIActionSlider knobPosition];
-[_UIActionSlider knobRect];
-[_UIActionSlider knobWidth];
-[_UIActionSlider openTrackAnimated:];
-[_UIActionSlider setCachedTrackMaskWidth:];
-[_UIActionSlider setKnobColor:];
-[_UIActionSlider setKnobImage:];
-[_UIActionSlider setKnobImageOffset:];
-[_UIActionSlider setKnobInsets:];
-[_UIActionSlider setKnobPosition:];
-[_UIActionSlider setKnobWidth:];
-[_UIActionSlider setMaskFromImage:onView:];
-[_UIActionSlider setMaskPath:onView:];
-[_UIActionSlider setShowingTrackLabel:];
-[_UIActionSlider setTrackFont:];
-[_UIActionSlider setTrackSize:];
-[_UIActionSlider setTrackText:];
-[_UIActionSlider setTrackWidthProportion:];
-[_UIActionSlider shouldHideTrackLabelForXPoint:];
-[_UIActionSlider slideGestureRecognizer];
-[_UIActionSlider trackFont];
-[_UIActionSlider trackLabel];
-[_UIActionSlider trackMaskImage];
-[_UIActionSlider trackMaskPath];
-[_UIActionSlider trackText];
-[_UIActionSlider trackTextBaselineFromBottom];
-[_UIActionSlider trackTextRect];
-[_UIActionSlider trackWidthProportion];
-[_UIActionSlider updateAllTrackMasks];
-[_UIActionSlider xPointIsWithinTrack:];
```
