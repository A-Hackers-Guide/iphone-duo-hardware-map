# `CAMExposureBiasSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 11 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _suspendTrackFadeOut;
f _exposureBiasMin;
f _exposureBiasMax;
f _exposureBiasValue;
@"CAMExposureBiasSliderThumb" __thumbView;
@"UIView" __minTrackView;
@"UIView" __maxTrackView;
@"UIView" __minTrackMaskView;
@"UIView" __maxTrackMaskView;
d __lastInteractionTime;
```

## Properties

```
@property (T@"CAMExposureBiasSliderThumb",R,&,N,V__thumbView) _thumbView;
@property (T@"UIView",R,&,N,V__minTrackView) _minTrackView;
@property (T@"UIView",R,&,N,V__maxTrackView) _maxTrackView;
@property (T@"UIView",R,&,N,V__minTrackMaskView) _minTrackMaskView;
@property (T@"UIView",R,&,N,V__maxTrackMaskView) _maxTrackMaskView;
@property (Td,R,N,V__lastInteractionTime) _lastInteractionTime;
@property (Tf,N,V_exposureBiasMin) exposureBiasMin;
@property (Tf,N,V_exposureBiasMax) exposureBiasMax;
@property (Tf,N,V_exposureBiasValue) exposureBiasValue;
@property (TB,N,V_suspendTrackFadeOut) suspendTrackFadeOut;
@property (Td,R,N) thumbMaxExtension;
```

## Instance methods

```
-[CAMExposureBiasSlider exposureBiasValue];
-[CAMExposureBiasSlider setExposureBiasValue:];
-[CAMExposureBiasSlider layoutSubviews];
-[CAMExposureBiasSlider sizeThatFits:];
-[CAMExposureBiasSlider tintColorDidChange];
-[CAMExposureBiasSlider initWithFrame:];
-[CAMExposureBiasSlider _maxTrackView];
-[CAMExposureBiasSlider _minTrackView];
-[CAMExposureBiasSlider _thumbView];
-[CAMExposureBiasSlider exposureBiasMax];
-[CAMExposureBiasSlider exposureBiasMin];
-[CAMExposureBiasSlider _animateTrackAlpha:withDuration:];
-[CAMExposureBiasSlider _cancelDelayedDim];
-[CAMExposureBiasSlider _dimTrackForInactivity];
-[CAMExposureBiasSlider _lastInteractionTime];
-[CAMExposureBiasSlider _maxTrackMaskView];
-[CAMExposureBiasSlider _minTrackMaskView];
-[CAMExposureBiasSlider _normalizedExposureValue];
-[CAMExposureBiasSlider _scheduleDelayedDim];
-[CAMExposureBiasSlider _sunCenterForNormalizedValue:];
-[CAMExposureBiasSlider _trackAlpha];
-[CAMExposureBiasSlider _updateForChangedNormalizedExposureValue];
-[CAMExposureBiasSlider forceTrackDimmed];
-[CAMExposureBiasSlider setExposureBiasMax:];
-[CAMExposureBiasSlider setExposureBiasMin:];
-[CAMExposureBiasSlider setSuspendTrackFadeOut:];
-[CAMExposureBiasSlider suspendTrackFadeOut];
-[CAMExposureBiasSlider thumbMaxExtension];
-[CAMExposureBiasSlider updateLastInteractionTime];
```
