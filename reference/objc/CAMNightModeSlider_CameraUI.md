# `CAMNightModeSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CEKDiscreteSlider`
- 7 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _nightModeActive;
B __performingCaptureAnimation;
Q __selectedIndexBeforeCaptureAnimation;
d __remainingCaptureAnimationTime;
@"NSTimer" __valueLabelUpdateTimer;
d __inactiveTickMarkHeight;
{?="minimumDuration"d"maximumDuration"d} _durationMapping;
```

## Properties

```
@property (TB,N,G_isPerformingCaptureAnimation,S_setPerformingCaptureAnimation:,V__performingCaptureAnimation) _performingCaptureAnimation;
@property (TQ,N,S_setSelectedIndexBeforeCaptureAnimation:,V__selectedIndexBeforeCaptureAnimation) _selectedIndexBeforeCaptureAnimation;
@property (Td,N,S_setRemainingCaptureAnimationTime:,V__remainingCaptureAnimationTime) _remainingCaptureAnimationTime;
@property (T@"NSTimer",&,N,S_setValueLabelUpdateTimer:,V__valueLabelUpdateTimer) _valueLabelUpdateTimer;
@property (Td,R,N,V__inactiveTickMarkHeight) _inactiveTickMarkHeight;
@property (TQ,N) nightMode;
@property (TB,N,GisNightModeActive,V_nightModeActive) nightModeActive;
@property (T{?=dd},N,V_durationMapping) durationMapping;
```

## Instance methods

```
-[CAMNightModeSlider nightMode];
-[CAMNightModeSlider dealloc];
-[CAMNightModeSlider setNightMode:];
-[CAMNightModeSlider initWithFrame:];
-[CAMNightModeSlider _setPerformingCaptureAnimation:];
-[CAMNightModeSlider durationMapping];
-[CAMNightModeSlider _handleValueLabelUpdateTimerWithStartTime:duration:];
-[CAMNightModeSlider _inactiveTickMarkHeight];
-[CAMNightModeSlider _isPerformingCaptureAnimation];
-[CAMNightModeSlider _remainingCaptureAnimationTime];
-[CAMNightModeSlider _selectedIndexBeforeCaptureAnimation];
-[CAMNightModeSlider _setRemainingCaptureAnimationTime:];
-[CAMNightModeSlider _setSelectedIndexBeforeCaptureAnimation:];
-[CAMNightModeSlider _setValueLabelUpdateTimer:];
-[CAMNightModeSlider _startValueLabelUpdateTimerWithDuration:];
-[CAMNightModeSlider _stopValueLabelUpdateTimer];
-[CAMNightModeSlider _valueLabelUpdateTimer];
-[CAMNightModeSlider _valueTextForDuration:];
-[CAMNightModeSlider _valueTextForDuration:format:];
-[CAMNightModeSlider endCaptureAnimationAnimated:];
-[CAMNightModeSlider isNightModeActive];
-[CAMNightModeSlider performCaptureAnimationWithDuration:completion:];
-[CAMNightModeSlider setDurationMapping:];
-[CAMNightModeSlider setNightModeActive:];
-[CAMNightModeSlider valueText];
```
