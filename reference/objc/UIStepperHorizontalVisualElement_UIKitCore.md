# `UIStepperHorizontalVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`, `UIStepperVisualElement`
- 24 instance variables, 13 properties, 60 instance methods, 5 class methods

## Instance variables

```
B _isRtoL;
@"UIImageView" _leftBackground;
@"UIImageView" _rightBackground;
@"UIImageView" _leftHighlight;
@"UIImageView" _rightHighlight;
@"UIImageView" _middleView;
@"UIButton" _plusButton;
@"UIButton" _minusButton;
@"NSTimer" _repeatTimer;
q _repeatCount;
@"NSMutableDictionary" _dividerImages;
@"UIViewPropertyAnimator" _leftAlphaAnimator;
@"UIViewPropertyAnimator" _rightAlphaAnimator;
@"UIViewPropertyAnimator" _leftFrameAnimator;
@"UIViewPropertyAnimator" _rightFrameAnimator;
B _autorepeat;
B _continuous;
B _enabled;
B _wraps;
d _value;
d _maximumValue;
d _minimumValue;
@"<UIStepperControl>" _stepperControl;
d _stepValue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Td,N,V_value) value;
@property (Td,N,V_minimumValue) minimumValue;
@property (Td,N,V_maximumValue) maximumValue;
@property (Td,N,V_stepValue) stepValue;
@property (TB,N,GisContinuous,V_continuous) continuous;
@property (TB,N,V_wraps) wraps;
@property (TB,N,V_autorepeat) autorepeat;
@property (T@"<UIStepperControl>",W,N,V_stepperControl) stepperControl;
```

## Class methods

```
+[UIStepperHorizontalVisualElement _highlightOpacityAnimation];
+[UIStepperHorizontalVisualElement _highlightSizeAnimation];
+[UIStepperHorizontalVisualElement initialAlignmentRectInsets];
+[UIStepperHorizontalVisualElement initialIntrinsicSize];
+[UIStepperHorizontalVisualElement initialSize];
```

## Instance methods

```
-[UIStepperHorizontalVisualElement setMaximumValue:];
-[UIStepperHorizontalVisualElement _dynamicUserInterfaceTraitDidChange];
-[UIStepperHorizontalVisualElement pointerInteraction:styleForRegion:];
-[UIStepperHorizontalVisualElement _intrinsicSizeWithinSize:];
-[UIStepperHorizontalVisualElement pointerInteraction:willEnterRegion:animator:];
-[UIStepperHorizontalVisualElement cancelTrackingWithEvent:];
-[UIStepperHorizontalVisualElement pointerInteraction:willExitRegion:animator:];
-[UIStepperHorizontalVisualElement setContinuous:];
-[UIStepperHorizontalVisualElement endTrackingWithTouch:withEvent:];
-[UIStepperHorizontalVisualElement continueTrackingWithTouch:withEvent:];
-[UIStepperHorizontalVisualElement value];
-[UIStepperHorizontalVisualElement layoutSubviews];
-[UIStepperHorizontalVisualElement hitTest:withEvent:];
-[UIStepperHorizontalVisualElement beginTrackingWithTouch:withEvent:];
-[UIStepperHorizontalVisualElement _startTimer];
-[UIStepperHorizontalVisualElement isContinuous];
-[UIStepperHorizontalVisualElement isEnabled];
-[UIStepperHorizontalVisualElement sizeThatFits:];
-[UIStepperHorizontalVisualElement backgroundImageForState:];
-[UIStepperHorizontalVisualElement setValue:];
-[UIStepperHorizontalVisualElement setTintColor:];
-[UIStepperHorizontalVisualElement setMinimumValue:];
-[UIStepperHorizontalVisualElement _stopTimer];
-[UIStepperHorizontalVisualElement setEnabled:];
-[UIStepperHorizontalVisualElement pointerInteraction:regionForRequest:defaultRegion:];
-[UIStepperHorizontalVisualElement minimumValue];
-[UIStepperHorizontalVisualElement initWithFrame:];
-[UIStepperHorizontalVisualElement maximumValue];
-[UIStepperHorizontalVisualElement setBackgroundImage:forState:];
-[UIStepperHorizontalVisualElement _alphaAnimator:];
-[UIStepperHorizontalVisualElement _updateBackgroundForButtonState];
-[UIStepperHorizontalVisualElement _commonStepperInit];
-[UIStepperHorizontalVisualElement _leftHighlightFrame];
-[UIStepperHorizontalVisualElement _leftHighlightInsetFrame];
-[UIStepperHorizontalVisualElement _rightHighlightFrame];
-[UIStepperHorizontalVisualElement _rightHighlightInsetFrame];
-[UIStepperHorizontalVisualElement _updateButton:backgroundView:highlightView:backgroundImage:highlightImage:onRight:];
-[UIStepperHorizontalVisualElement _updateButtonEnabled];
-[UIStepperHorizontalVisualElement _updateCount:];
-[UIStepperHorizontalVisualElement _updateDividerImageForButtonState];
-[UIStepperHorizontalVisualElement _updateHighlight:button:onRight:];
-[UIStepperHorizontalVisualElement _updateHighlightingAtPoint:withEvent:];
-[UIStepperHorizontalVisualElement alignmentRectInsetsForControl:];
-[UIStepperHorizontalVisualElement autorepeat];
-[UIStepperHorizontalVisualElement decrementImageForState:];
-[UIStepperHorizontalVisualElement dividerImageForLeftSegmentState:rightSegmentState:];
-[UIStepperHorizontalVisualElement incrementImageForState:];
-[UIStepperHorizontalVisualElement intrinsicSizeWithinSize:forControl:];
-[UIStepperHorizontalVisualElement pointMostlyInside:withEvent:];
-[UIStepperHorizontalVisualElement setAutorepeat:];
-[UIStepperHorizontalVisualElement setDecrementImage:forState:];
-[UIStepperHorizontalVisualElement setDividerImage:forLeftSegmentState:rightSegmentState:];
-[UIStepperHorizontalVisualElement setIncrementImage:forState:];
-[UIStepperHorizontalVisualElement setStepValue:];
-[UIStepperHorizontalVisualElement setStepperControl:];
-[UIStepperHorizontalVisualElement setWraps:];
-[UIStepperHorizontalVisualElement sizeThatFits:forControl:];
-[UIStepperHorizontalVisualElement stepValue];
-[UIStepperHorizontalVisualElement stepperControl];
-[UIStepperHorizontalVisualElement wraps];
```
