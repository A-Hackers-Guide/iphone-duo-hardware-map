# `CAMSnapshotView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIBasicAnimationFactory`
- 11 instance variables, 15 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _blurred;
B _dimmed;
B __supportsBlur;
@"UIView" _snapshotView;
q _desiredAspectRatio;
@"UIView" __lowQualityBlurView;
@"UIView" __dimmingView;
@"UIVisualEffectView" __blurView;
q __blurStyleForEffectAnimationFactory;
@"UIView" __snapshottedView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __snapshottedBounds;
```

## Properties

```
@property (TB,R,N,V__supportsBlur) _supportsBlur;
@property (T@"UIView",R,N,V__lowQualityBlurView) _lowQualityBlurView;
@property (T@"UIView",R,N,V__dimmingView) _dimmingView;
@property (T@"UIVisualEffectView",&,N,S_setBlurView:,V__blurView) _blurView;
@property (Tq,N,S_setBlurStyleForEffectAnimationFactory:,V__blurStyleForEffectAnimationFactory) _blurStyleForEffectAnimationFactory;
@property (T@"UIView",R,W,N,V__snapshottedView) _snapshottedView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V__snapshottedBounds) _snapshottedBounds;
@property (T@"UIView",R,N,V_snapshotView) snapshotView;
@property (Tq,R,N,V_desiredAspectRatio) desiredAspectRatio;
@property (TB,N,V_blurred) blurred;
@property (TB,N,V_dimmed) dimmed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSnapshotView snapshotView];
-[CAMSnapshotView setBlurred:];
-[CAMSnapshotView _applySnapshotBlurForStyle:animated:withCompletionBlock:];
-[CAMSnapshotView _removeSnapshotDimAnimated:withCompletionBlock:];
-[CAMSnapshotView setBlurred:animated:style:withCompletionBlock:];
-[CAMSnapshotView _removeLowQualityBlurForStyle:animated:withCompletionBlock:];
-[CAMSnapshotView initWithView:desiredAspectRatio:];
-[CAMSnapshotView activityItemsConfiguration];
-[CAMSnapshotView _prepareForApplyingBlurForStyle:applying:inputRadiusAmount:inputRadiusDuration:inputRadiusDelay:inputRadiusTimingFunction:opacityAmount:opacityDuration:opacityDelay:opacityTimingFunction:];
-[CAMSnapshotView setDimmed:animated:withCompletionBlock:];
-[CAMSnapshotView _setBlurStyleForEffectAnimationFactory:];
-[CAMSnapshotView _setupDimOnSnapshot];
-[CAMSnapshotView _supportsBlur];
-[CAMSnapshotView layoutSubviews];
-[CAMSnapshotView _removeAnimationOnView:forKey:];
-[CAMSnapshotView _resumeFadeInDuration];
-[CAMSnapshotView _snapshottedView];
-[CAMSnapshotView prepareForResumingUsingCrossfade];
-[CAMSnapshotView _blurStyleForEffectAnimationFactory];
-[CAMSnapshotView removeAllAnimationsOnLayer:recursively:shouldLog:];
-[CAMSnapshotView setDimmed:];
-[CAMSnapshotView _lowQualityBlurView];
-[CAMSnapshotView fadeOutAnimatedWithStyle:completion:];
-[CAMSnapshotView _applySnapshotDimAnimated:withCompletionBlock:];
-[CAMSnapshotView _removeSnapshotBlurForStyle:animated:withCompletionBlock:];
-[CAMSnapshotView _setupLowQualityBlurOnSnapshot];
-[CAMSnapshotView _snapshottedBounds];
-[CAMSnapshotView removeInflightBlurAnimations];
-[CAMSnapshotView initWithVideoPreviewImage:viewportFrameInSuperviewCoordinates:superviewBounds:desiredAspectRatio:];
-[CAMSnapshotView _setBlurView:];
-[CAMSnapshotView blurred];
-[CAMSnapshotView _prepareForApplyingLowQualityBlurForStyle:applying:opacityAmount:opacityDuration:opacityDelay:opacityTimingFunction:targetView:];
-[CAMSnapshotView dimmed];
-[CAMSnapshotView _blurView];
-[CAMSnapshotView setSnapshotVisible:duration:];
-[CAMSnapshotView _dimmingView];
-[CAMSnapshotView _applyLowQualityBlurForStyle:animated:withCompletionBlock:];
-[CAMSnapshotView _basicAnimationForView:withKeyPath:];
-[CAMSnapshotView desiredAspectRatio];
```
