# `CEKExpandingSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `CEKAdditiveAnimatorDelegate`, `UIGestureRecognizerDelegate`
- 28 instance variables, 36 properties, 76 instance methods, 0 class methods

## Instance variables

```
B _expanded;
B _valueLabelHidden;
B _markedValueDotHidden;
@"<CEKExpandingSliderDelegate>" _delegate;
d _markedValue;
d _titleAlpha;
d _collapsedCenterX;
@"UIColor" _valueLabelColor;
d _valueLabelFontSize;
d _valueLabelTopPadding;
@"NSString" _leadingAccessoryText;
@"NSString" _trailingAccessoryText;
@"NSArray" _tickColorGradient;
@"UIColor" _selectedTickColor;
d _postInteractionCollapseDelay;
@"UILabel" __titleLabel;
@"UILabel" __valueLabel;
@"UIView" __levelIndicatorView;
@"CEKExpandingTickMarksView" __ticksView;
@"CEKSlider" __slider;
@"UILabel" __leadingAccessoryLabel;
@"UILabel" __trailingAccessoryLabel;
@"UILongPressGestureRecognizer" __gestureRecognizer;
@"CEKAdditiveAnimator" __animator;
Q __expansionAnimationCounter;
@"NSTimer" __expansionAnimationTimer;
@"NSTimer" __markedValueAnimationTimer;
d __range;
```

## Properties

```
@property (T@"UILabel",R,N,V__titleLabel) _titleLabel;
@property (T@"UILabel",R,N,V__valueLabel) _valueLabel;
@property (T@"UIView",R,N,V__levelIndicatorView) _levelIndicatorView;
@property (T@"CEKExpandingTickMarksView",R,N,V__ticksView) _ticksView;
@property (T@"CEKSlider",R,N,V__slider) _slider;
@property (T@"UILabel",R,N,V__leadingAccessoryLabel) _leadingAccessoryLabel;
@property (T@"UILabel",R,N,V__trailingAccessoryLabel) _trailingAccessoryLabel;
@property (T@"UILongPressGestureRecognizer",R,N,V__gestureRecognizer) _gestureRecognizer;
@property (T@"CEKAdditiveAnimator",R,N,V__animator) _animator;
@property (TQ,N,S_setExpansionAnimationCounter:,V__expansionAnimationCounter) _expansionAnimationCounter;
@property (T@"NSTimer",&,N,S_setExpansionAnimationTimer:,V__expansionAnimationTimer) _expansionAnimationTimer;
@property (T@"NSTimer",&,N,S_setMarkedValueAnimationTimer:,V__markedValueAnimationTimer) _markedValueAnimationTimer;
@property (Td,R,N,V__range) _range;
@property (T@"<CEKExpandingSliderDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N) title;
@property (Td,N,V_markedValue) markedValue;
@property (Td,N,V_titleAlpha) titleAlpha;
@property (Td,N) value;
@property (TB,N,V_expanded) expanded;
@property (Td,N,V_collapsedCenterX) collapsedCenterX;
@property (TB,N,V_valueLabelHidden) valueLabelHidden;
@property (T@"UIColor",&,N,V_valueLabelColor) valueLabelColor;
@property (Td,N,V_valueLabelFontSize) valueLabelFontSize;
@property (Td,N,V_valueLabelTopPadding) valueLabelTopPadding;
@property (T@"NSString",C,N,V_leadingAccessoryText) leadingAccessoryText;
@property (T@"NSString",C,N,V_trailingAccessoryText) trailingAccessoryText;
@property (T@"NSArray",C,N,V_tickColorGradient) tickColorGradient;
@property (T@"UIColor",&,N,V_selectedTickColor) selectedTickColor;
@property (TB,N,V_markedValueDotHidden) markedValueDotHidden;
@property (Td,N) mainTickHeight;
@property (Td,N) secondaryTickHeight;
@property (Td,N,V_postInteractionCollapseDelay) postInteractionCollapseDelay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CEKExpandingSlider _handlePress:];
-[CEKExpandingSlider setValue:animated:];
-[CEKExpandingSlider _updateSubviewVisibility];
-[CEKExpandingSlider setExpanded:];
-[CEKExpandingSlider intrinsicContentSize];
-[CEKExpandingSlider initWithTitle:];
-[CEKExpandingSlider _updateColors];
-[CEKExpandingSlider _animator];
-[CEKExpandingSlider value];
-[CEKExpandingSlider layoutSubviews];
-[CEKExpandingSlider hitTest:withEvent:];
-[CEKExpandingSlider setTitleAlpha:];
-[CEKExpandingSlider selectedTickColor];
-[CEKExpandingSlider setDelegate:];
-[CEKExpandingSlider tintColorDidChange];
-[CEKExpandingSlider setValue:];
-[CEKExpandingSlider setTickColorGradient:];
-[CEKExpandingSlider titleAlpha];
-[CEKExpandingSlider title];
-[CEKExpandingSlider setSelectedTickColor:];
-[CEKExpandingSlider gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[CEKExpandingSlider delegate];
-[CEKExpandingSlider _gestureRecognizer];
-[CEKExpandingSlider tickColorGradient];
-[CEKExpandingSlider _ticksView];
-[CEKExpandingSlider setTitle:];
-[CEKExpandingSlider animator:didUpdateValuesForKeys:];
-[CEKExpandingSlider setExpanded:animated:];
-[CEKExpandingSlider expanded];
-[CEKExpandingSlider _range];
-[CEKExpandingSlider _titleLabel];
-[CEKExpandingSlider setMarkedValue:];
-[CEKExpandingSlider _expansionAnimationCounter];
-[CEKExpandingSlider _handleSliderDidChangeValue:];
-[CEKExpandingSlider setCollapsedCenterX:];
-[CEKExpandingSlider valueLabelColor];
-[CEKExpandingSlider _slider];
-[CEKExpandingSlider _expansionAnimationTimer];
-[CEKExpandingSlider _handleExpansionAnimationTimerFired:];
-[CEKExpandingSlider _handleMarkedValueAnimationTimerFired:];
-[CEKExpandingSlider _leadingAccessoryLabel];
-[CEKExpandingSlider _levelIndicatorView];
-[CEKExpandingSlider _markedValueAnimationTimer];
-[CEKExpandingSlider _setExpanded:animated:shouldNotify:];
-[CEKExpandingSlider _setExpansionAnimationCounter:];
-[CEKExpandingSlider _setExpansionAnimationTimer:];
-[CEKExpandingSlider _setMarkedValueAnimationTimer:];
-[CEKExpandingSlider _trailingAccessoryLabel];
-[CEKExpandingSlider _updateLabelColorsForProgress:];
-[CEKExpandingSlider _updateMarkedValueAnimated:];
-[CEKExpandingSlider _updateTickViewFrameForProgress:];
-[CEKExpandingSlider _updateUIForValue:animated:];
-[CEKExpandingSlider _valueLabel];
-[CEKExpandingSlider collapsedCenterX];
-[CEKExpandingSlider initWithTitle:minimumValue:maximumValue:defaultValue:];
-[CEKExpandingSlider initWithTitle:minimumValue:maximumValue:defaultValue:tickMarkStyle:];
-[CEKExpandingSlider leadingAccessoryText];
-[CEKExpandingSlider mainTickHeight];
-[CEKExpandingSlider markedValue];
-[CEKExpandingSlider markedValueDotHidden];
-[CEKExpandingSlider postInteractionCollapseDelay];
-[CEKExpandingSlider secondaryTickHeight];
-[CEKExpandingSlider setLeadingAccessoryText:];
-[CEKExpandingSlider setMainTickHeight:];
-[CEKExpandingSlider setMarkedValueDotHidden:];
-[CEKExpandingSlider setPostInteractionCollapseDelay:];
-[CEKExpandingSlider setSecondaryTickHeight:];
-[CEKExpandingSlider setTrailingAccessoryText:];
-[CEKExpandingSlider setValueLabelColor:];
-[CEKExpandingSlider setValueLabelFontSize:];
-[CEKExpandingSlider setValueLabelHidden:];
-[CEKExpandingSlider setValueLabelTopPadding:];
-[CEKExpandingSlider trailingAccessoryText];
-[CEKExpandingSlider valueLabelFontSize];
-[CEKExpandingSlider valueLabelHidden];
-[CEKExpandingSlider valueLabelTopPadding];
```
