# `UISwitchModernVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISwitchVisualElement`
- Protocols: `UIGestureRecognizerDelegate`, `UISwitchMVEGestureTrackingSessionElement`, `CAAnimationDelegate`, `UIPointerInteractionDelegate`
- 24 instance variables, 14 properties, 98 instance methods, 4 class methods

## Instance variables

```
@"UIView" _switchWellView;
@"UIView" _leftSwitchWellView;
@"UIView" _switchWellContainerView;
@"UIView" _leftSwitchWellContainerView;
@"UIImageView" _switchWellImageView;
@"UIView" _switchWellImageViewContainer;
@"UIImageView" _switchWellOffImageView;
@"UIImageView" _switchWellOnImageView;
@"UIView" _knobView;
@"UIColor" _onTintColor;
@"UIColor" _tintColor;
B _on;
B _pressed;
B _isAlwaysAccessible;
B _startedOn;
d _zeroOffset;
B _showsOnOffLabel;
@"UIColor" _thumbTintColor;
@"UIImage" _onImage;
@"UIImage" _offImage;
@"UISwitchMVEGestureTrackingSession" _gestureTrackingSession;
@"UILongPressGestureRecognizer" _longPress;
@"UIPanGestureRecognizer" _pan;
@"UITapGestureRecognizer" _selectGestureRecognizer;
```

## Properties

```
@property (T@"UIColor",&,N,V_thumbTintColor) thumbTintColor;
@property (T@"UIImage",&,N,V_onImage) onImage;
@property (T@"UIImage",&,N,V_offImage) offImage;
@property (TB,N,V_on) on;
@property (TB,N,V_pressed) pressed;
@property (TB,N,V_showsOnOffLabel) showsOnOffLabel;
@property (T@"UISwitchMVEGestureTrackingSession",&,N,V_gestureTrackingSession) gestureTrackingSession;
@property (T@"UILongPressGestureRecognizer",&,N,V_longPress) longPress;
@property (T@"UIPanGestureRecognizer",&,N,V_pan) pan;
@property (T@"UITapGestureRecognizer",&,N,V_selectGestureRecognizer) selectGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISwitchModernVisualElement _modernGradientImageWithOnColor:traitCollection:];
+[UISwitchModernVisualElement preferredContentSize];
+[UISwitchModernVisualElement preferredAlignmentRectInsets];
+[UISwitchModernVisualElement _modernThumbImageWithColor:mask:traitCollection:];
```

## Instance methods

```
-[UISwitchModernVisualElement _orderSubviews];
-[UISwitchModernVisualElement pan];
-[UISwitchModernVisualElement _transitionKnobToPressed:animated:];
-[UISwitchModernVisualElement displayedOn];
-[UISwitchModernVisualElement _settings];
-[UISwitchModernVisualElement setOnTintColor:];
-[UISwitchModernVisualElement _feedbackEnabled];
-[UISwitchModernVisualElement on];
-[UISwitchModernVisualElement gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UISwitchModernVisualElement _effectiveOnTintColor];
-[UISwitchModernVisualElement _switchTrackColorAnimationWithFromValue:toValue:];
-[UISwitchModernVisualElement setOnImage:];
-[UISwitchModernVisualElement animationDidStop:finished:];
-[UISwitchModernVisualElement _setPressed:on:animated:shouldAnimateLabels:completion:];
-[UISwitchModernVisualElement gestureTrackingSession];
-[UISwitchModernVisualElement _dynamicUserInterfaceTraitDidChange];
-[UISwitchModernVisualElement _uninstallSelectGestureRecognizer];
-[UISwitchModernVisualElement pointerInteraction:styleForRegion:];
-[UISwitchModernVisualElement _shouldUseLightTintOverColor:];
-[UISwitchModernVisualElement longPress];
-[UISwitchModernVisualElement _handleLongPress:];
-[UISwitchModernVisualElement _onImagePosition];
-[UISwitchModernVisualElement _wellColorOn:];
-[UISwitchModernVisualElement _leftSwitchWellContainerPositionOn:pressed:];
-[UISwitchModernVisualElement _effectiveOnImage];
-[UISwitchModernVisualElement offImage];
-[UISwitchModernVisualElement _handlePan:];
-[UISwitchModernVisualElement _installSelectGestureRecognizer];
-[UISwitchModernVisualElement _transitionKnobToOn:animated:];
-[UISwitchModernVisualElement _invalidateWell];
-[UISwitchModernVisualElement setOn:animated:];
-[UISwitchModernVisualElement _effectiveThumbImage];
-[UISwitchModernVisualElement _handlePanWithGestureLocationInBounds:horizontalTranslation:gestureState:resetPanTranslationBlock:];
-[UISwitchModernVisualElement _effectiveTintColor];
-[UISwitchModernVisualElement setSelectGestureRecognizer:];
-[UISwitchModernVisualElement _switchTrackPositionSpringAnimationFromValue:toValue:on:];
-[UISwitchModernVisualElement _updateDisplayAnimated:];
-[UISwitchModernVisualElement setSemanticContentAttribute:];
-[UISwitchModernVisualElement _effectiveGradientImage];
-[UISwitchModernVisualElement _switchSpringAnimationWithKeyPath:fromValue:toValue:pressed:];
-[UISwitchModernVisualElement _accessibleOnImage];
-[UISwitchModernVisualElement _switchKnobWidthSpringAnimationFromValue:toValue:pressed:];
-[UISwitchModernVisualElement tintColorDidChange];
-[UISwitchModernVisualElement _transitionWellViewToPressed:animated:];
-[UISwitchModernVisualElement thumbTintColor];
-[UISwitchModernVisualElement gestureRecognizerShouldBegin:];
-[UISwitchModernVisualElement setTintColor:];
-[UISwitchModernVisualElement _accessibleOffImage];
-[UISwitchModernVisualElement _offImagePosition];
-[UISwitchModernVisualElement setGestureTrackingSession:];
-[UISwitchModernVisualElement _gestureRecognizer:shouldReceiveEvent:];
-[UISwitchModernVisualElement selectGestureRecognizer];
-[UISwitchModernVisualElement pressed];
-[UISwitchModernVisualElement setShowsOnOffLabel:];
-[UISwitchModernVisualElement _labelOpacityAnimation];
-[UISwitchModernVisualElement setOffImage:];
-[UISwitchModernVisualElement pointerInteraction:regionForRequest:defaultRegion:];
-[UISwitchModernVisualElement setLongPress:];
-[UISwitchModernVisualElement gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UISwitchModernVisualElement setOn:];
-[UISwitchModernVisualElement _switchWellContainerPositionOn:pressed:];
-[UISwitchModernVisualElement _switchKnobPositionSpringAnimationFromValue:toValue:];
-[UISwitchModernVisualElement performStateChangeFeedback];
-[UISwitchModernVisualElement _leftSwitchWellContainerBoundsOn:pressed:];
-[UISwitchModernVisualElement _knobBoundsPressed:];
-[UISwitchModernVisualElement _invalidateUserInterfaceRenderingMode];
-[UISwitchModernVisualElement _effectiveOffTextColor];
-[UISwitchModernVisualElement _switchWellPositionOn:pressed:];
-[UISwitchModernVisualElement _invalidateKnob];
-[UISwitchModernVisualElement _transitionKnobToPressed:on:animated:];
-[UISwitchModernVisualElement _defaultOnTintColor];
-[UISwitchModernVisualElement _effectiveOffImage];
-[UISwitchModernVisualElement _switchWellContainerBoundsOn:pressed:];
-[UISwitchModernVisualElement sendStateChangeActions];
-[UISwitchModernVisualElement _transitionWellViewToOn:animated:];
-[UISwitchModernVisualElement showsOnOffLabel];
-[UISwitchModernVisualElement _transitionImagesToPressed:on:animated:];
-[UISwitchModernVisualElement _invalidateOnOffImages];
-[UISwitchModernVisualElement _switchTrackAnimationWithFromValue:toValue:on:];
-[UISwitchModernVisualElement _wellPositionOn:forBounds:];
-[UISwitchModernVisualElement setThumbTintColor:];
-[UISwitchModernVisualElement _effectiveOffImageTintColor];
-[UISwitchModernVisualElement onImage];
-[UISwitchModernVisualElement _handleLongPressWithGestureLocationInBounds:gestureState:];
-[UISwitchModernVisualElement _invalidateControl];
-[UISwitchModernVisualElement _effectiveOnImageTintColor];
-[UISwitchModernVisualElement setSwitchControl:];
-[UISwitchModernVisualElement initWithFrame:];
-[UISwitchModernVisualElement setPan:];
-[UISwitchModernVisualElement _selectGestureChanged:];
-[UISwitchModernVisualElement _switchToStaticMode:];
-[UISwitchModernVisualElement _switchTrackPositionAnimationWithFromValue:toValue:on:];
-[UISwitchModernVisualElement _updateDisplayWithAnimationIfNeeded];
-[UISwitchModernVisualElement setPressed:];
-[UISwitchModernVisualElement _knobPositionOn:pressed:forBounds:];
-[UISwitchModernVisualElement _transitionWellViewToPressed:on:animated:];
-[UISwitchModernVisualElement _wellBorderWidthPressed:on:];
-[UISwitchModernVisualElement interactiveChangeToDisplayedOn:];
```
