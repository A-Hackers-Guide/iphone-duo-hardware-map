# `CAMSemanticStyleControl`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIGestureRecognizerDelegate`, `CEKExpandingSliderDelegate`
- 8 instance variables, 12 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _shouldConfirmBeforeResetting;
@"CAMSemanticStyle" _semanticStyle;
@"NSArray" __allSliders;
@"UILabel" __descriptionLabel;
@"UIButton" __resetButton;
@"UIView" __gradientContainer;
@"CEKEdgeGradientView" __edgeGradients;
{?="startInset"d"endInset"d} _gradientInsets;
```

## Properties

```
@property (T@"NSArray",R,N,V__allSliders) _allSliders;
@property (T@"UILabel",R,N,V__descriptionLabel) _descriptionLabel;
@property (T@"UIButton",R,N,V__resetButton) _resetButton;
@property (T@"UIView",R,N,V__gradientContainer) _gradientContainer;
@property (T@"CEKEdgeGradientView",R,N,V__edgeGradients) _edgeGradients;
@property (T@"CAMSemanticStyle",&,N,V_semanticStyle) semanticStyle;
@property (T{?=dd},N,V_gradientInsets) gradientInsets;
@property (TB,N,V_shouldConfirmBeforeResetting) shouldConfirmBeforeResetting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSemanticStyleControl setSemanticStyle:];
-[CAMSemanticStyleControl layoutSubviews];
-[CAMSemanticStyleControl hitTest:withEvent:];
-[CAMSemanticStyleControl _handleReset];
-[CAMSemanticStyleControl beginTrackingWithTouch:withEvent:];
-[CAMSemanticStyleControl semanticStyle];
-[CAMSemanticStyleControl setSemanticStyle:animated:];
-[CAMSemanticStyleControl canBecomeFirstResponder];
-[CAMSemanticStyleControl initWithFrame:];
-[CAMSemanticStyleControl _allSliders];
-[CAMSemanticStyleControl _createSliderForIndex:];
-[CAMSemanticStyleControl _descriptionLabel];
-[CAMSemanticStyleControl _edgeGradients];
-[CAMSemanticStyleControl _gradientContainer];
-[CAMSemanticStyleControl _handleResetButtonReleased:];
-[CAMSemanticStyleControl _handleSliderDidChangeValue:];
-[CAMSemanticStyleControl _resetButton];
-[CAMSemanticStyleControl _showResetConfirmation];
-[CAMSemanticStyleControl _updateSlidersAnimated:];
-[CAMSemanticStyleControl _updateSubviewsVisibilityWithDuration:delay:];
-[CAMSemanticStyleControl gradientInsets];
-[CAMSemanticStyleControl setGradientInsets:];
-[CAMSemanticStyleControl setShouldConfirmBeforeResetting:];
-[CAMSemanticStyleControl shouldConfirmBeforeResetting];
-[CAMSemanticStyleControl sliderWillCollapse:];
-[CAMSemanticStyleControl sliderWillExpand:];
```
