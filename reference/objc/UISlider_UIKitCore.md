# `UISlider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `NSCoding`
- 7 instance variables, 25 properties, 120 instance methods, 3 class methods

## Instance variables

```
@"UIView<_UISliderVisualElement>" _visualElement;
@"UISliderDataModel" _data;
@"NSArray" _dummyViews;
@"<_UISliderConfiguration>" _sliderConfiguration;
q _sliderStyle;
Q _preferredBehavioralStyle;
{?="visualElementIsFluid"b1"visualElementRespondsToDidUpdateConfiguration"b1"visualElementRespondsToDidUpdateSliderStyle"b1"visualElementRespondsToDidSetUserInteractionEnabled"b1"visualElementRespondsToOverrideTrackingState"b1"visualElementRespondsToDidSetSpeedMultiplier"b1"visualElementRespondsToAdditionalTrackingViews"b1"visualElementDefersFinalActions"b1"visualElementNeedsReevaluationForTrackImages"b1} _visualElementFlags;
```

## Properties

```
@property (TB,N,S_setTrackEnabled:) _trackEnabled;
@property (Tf,N,S_setMinimumEnabledValue:) _minimumEnabledValue;
@property (Tf,N,S_setMaximumEnabledValue:) _maximumEnabledValue;
@property (Tf,N,S_setSliderSpeedMultiplier:) _sliderSpeedMultiplier;
@property (Tq,N,S_setSliderStyle:) _sliderStyle;
@property (T@"<_UISliderConfiguration>",C,N,G_sliderConfiguration,S_setSliderConfiguration:) sliderConfiguration;
@property (T@"_UIEdgeFeedbackGenerator",&,N,G_edgeFeedbackGenerator,S_setEdgeFeedbackGenerator:) edgeFeedbackGenerator;
@property (T@"_UIModulationFeedbackGenerator",&,N,G_modulationFeedbackGenerator,S_setModulationFeedbackGenerator:) modulationFeedbackGenerator;
@property (T@"_UIEdgeFeedbackGenerator",&,N,G_edgeFeedbackBehavior,S_setEdgeFeedbackBehavior:) edgeFeedbackBehavior;
@property (TQ,R,N) behavioralStyle;
@property (TQ,N) preferredBehavioralStyle;
@property (Tf,D,N) value;
@property (Tf,D,N) minimumValue;
@property (Tf,D,N) maximumValue;
@property (T@"UIImage",&,N) minimumValueImage;
@property (T@"UIImage",&,N) maximumValueImage;
@property (TB,N,GisContinuous) continuous;
@property (T@"UISliderTrackConfiguration",C,D,N) trackConfiguration;
@property (Tq,D,N) sliderStyle;
@property (T@"UIColor",&,N) minimumTrackTintColor;
@property (T@"UIColor",&,N) maximumTrackTintColor;
@property (T@"UIColor",&,N) thumbTintColor;
@property (T@"UIImage",R,N) currentThumbImage;
@property (T@"UIImage",R,N) currentMinimumTrackImage;
@property (T@"UIImage",R,N) currentMaximumTrackImage;
```

## Class methods

```
+[UISlider _setAllowsUnsupportedMacIdiomBehavior:];
+[UISlider _allowsUnsupportedMacIdiomBehavior];
+[UISlider _allowActionsToQueue];
```

## Instance methods

```
-[UISlider _controlEventsForActionTriggered];
-[UISlider setUserInteractionEnabled:];
-[UISlider cancelTouchTracking];
-[UISlider setValue:animated:];
-[UISlider setSelected:];
-[UISlider _intrinsicContentSizeInvalidatedForChildView:];
-[UISlider setMaximumValue:];
-[UISlider minimumValueImageRectForBounds:];
-[UISlider minimumTrackTintColor];
-[UISlider valueTextRectForBounds:];
-[UISlider _intrinsicSizeWithinSize:];
-[UISlider setTracking:];
-[UISlider setMaximumTrackImage:forState:];
-[UISlider setThumbImage:forState:];
-[UISlider init];
-[UISlider alignmentRectInsets];
-[UISlider createThumbView];
-[UISlider setContinuous:];
-[UISlider endTrackingWithTouch:withEvent:];
-[UISlider currentMaximumTrackImage];
-[UISlider continueTrackingWithTouch:withEvent:];
-[UISlider isAnimatingValueChange];
-[UISlider value];
-[UISlider setMinimumValueImage:];
-[UISlider currentMinimumTrackImage];
-[UISlider maximumTrackImageForState:];
-[UISlider layoutSubviews];
-[UISlider currentThumbImage];
-[UISlider maximumValueImage];
-[UISlider beginTrackingWithTouch:withEvent:];
-[UISlider setBounds:];
-[UISlider setMaximumValueImage:];
-[UISlider isContinuous];
-[UISlider setSemanticContentAttribute:];
-[UISlider thumbImageForState:];
-[UISlider sizeThatFits:];
-[UISlider isTracking];
-[UISlider _contentHuggingDefault_isUsuallyFixedHeight];
-[UISlider thumbTintColor];
-[UISlider setMaximumTrackImage:forStates:];
-[UISlider gestureRecognizerShouldBegin:];
-[UISlider setValue:];
-[UISlider setHighlighted:];
-[UISlider setMinimumValue:];
-[UISlider setShowValue:];
-[UISlider setEnabled:];
-[UISlider maximumValueImageRectForBounds:];
-[UISlider minimumValueImage];
-[UISlider minimumTrackImageForState:];
-[UISlider encodeWithCoder:];
-[UISlider setMinimumTrackTintColor:];
-[UISlider setThumbImage:forStates:];
-[UISlider setFrame:];
-[UISlider _controlTouchBegan:withEvent:];
-[UISlider isElementAccessibilityExposedToInterfaceBuilder];
-[UISlider description];
-[UISlider thumbRectForBounds:trackRect:value:];
-[UISlider initWithCoder:];
-[UISlider _populateArchivedSubviews:];
-[UISlider minimumValue];
-[UISlider trackRectForBounds:];
-[UISlider _controlTouchMoved:withEvent:];
-[UISlider setThumbTintColor:];
-[UISlider maximumTrackTintColor];
-[UISlider initWithFrame:];
-[UISlider cancelMouseTracking];
-[UISlider setMinimumTrackImage:forState:];
-[UISlider setMinimumTrackImage:forStates:];
-[UISlider maximumValue];
-[UISlider _controlTouchEnded:withEvent:];
-[UISlider setMaximumTrackTintColor:];
-[UISlider behavioralStyle];
-[UISlider _alwaysHandleScrollerMouseEvent];
-[UISlider _isThumbEnabled];
-[UISlider _reinstallVisualElementIfNeeded];
-[UISlider isAccessibilityElementByDefault];
-[UISlider setSliderStyle:];
-[UISlider _additionalTrackingViews];
-[UISlider _deferFinalActions];
-[UISlider _edgeFeedbackBehavior];
-[UISlider _edgeFeedbackGenerator];
-[UISlider _fluidTrackHidden];
-[UISlider _fluidUpdateSource];
-[UISlider _installVisualElement];
-[UISlider _installVisualElement:];
-[UISlider _maxTrackView];
-[UISlider _maxValueView];
-[UISlider _maximumEnabledValue];
-[UISlider _minTrackView];
-[UISlider _minValueView];
-[UISlider _minimumEnabledValue];
-[UISlider _modulationFeedbackGenerator];
-[UISlider _registerForTraitChanges];
-[UISlider _setEdgeFeedbackBehavior:];
-[UISlider _setEdgeFeedbackGenerator:];
-[UISlider _setFluidTrackHidden:];
-[UISlider _setMaxValue:];
-[UISlider _setMaximumEnabledValue:];
-[UISlider _setMinValue:];
-[UISlider _setMinimumEnabledValue:];
-[UISlider _setMinimumTrackVisible:withDuration:];
-[UISlider _setModulationFeedbackGenerator:];
-[UISlider _setSliderConfiguration:];
-[UISlider _setSliderSpeedMultiplier:];
-[UISlider _setSliderStyle:];
-[UISlider _setThumbEnabled:];
-[UISlider _setTrackEnabled:];
-[UISlider _setUseLookNeue:];
-[UISlider _sliderConfiguration];
-[UISlider _sliderSpeedMultiplier];
-[UISlider _sliderStyle];
-[UISlider _thumbHitEdgeInsets];
-[UISlider _thumbView];
-[UISlider _thumbViewNeue];
-[UISlider _trackEnabled];
-[UISlider preferredBehavioralStyle];
-[UISlider setPreferredBehavioralStyle:];
-[UISlider setTrackConfiguration:];
-[UISlider sliderStyle];
-[UISlider trackConfiguration];
```
