# `CFXFaceReticleView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 10 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _isShowingFaceIndicator;
B _canPerformFadeInAnimations;
B _canPerformFadeOutAnimations;
@"UIImageView" _reticleImageView;
@"UISelectionFeedbackGenerator" _feedbackGenerator;
@"UIViewPropertyAnimator" _bounceAnimator;
@"UIViewPropertyAnimator" _fadeOutAnimator;
@"UIViewPropertyAnimator" _animojiBounceAnimator;
@"UIViewPropertyAnimator" _animojiFadeOutAnimator;
@"NSMutableArray" _reticleLayersToAnimate;
```

## Properties

```
@property (TB,N,V_isShowingFaceIndicator) isShowingFaceIndicator;
@property (T@"UIImageView",&,N,V_reticleImageView) reticleImageView;
@property (T@"UISelectionFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (TB,N,V_canPerformFadeInAnimations) canPerformFadeInAnimations;
@property (TB,N,V_canPerformFadeOutAnimations) canPerformFadeOutAnimations;
@property (T@"UIViewPropertyAnimator",&,N,V_bounceAnimator) bounceAnimator;
@property (T@"UIViewPropertyAnimator",&,N,V_fadeOutAnimator) fadeOutAnimator;
@property (T@"UIViewPropertyAnimator",&,N,V_animojiBounceAnimator) animojiBounceAnimator;
@property (T@"UIViewPropertyAnimator",&,N,V_animojiFadeOutAnimator) animojiFadeOutAnimator;
@property (T@"NSMutableArray",&,N,V_reticleLayersToAnimate) reticleLayersToAnimate;
```

## Instance methods

```
-[CFXFaceReticleView setFeedbackGenerator:];
-[CFXFaceReticleView feedbackGenerator];
-[CFXFaceReticleView fadeOutAnimator];
-[CFXFaceReticleView setFadeOutAnimator:];
-[CFXFaceReticleView fadeInAnimation];
-[CFXFaceReticleView fadeOutAnimationWithCompletion:];
-[CFXFaceReticleView setCanPerformFadeOutAnimations:];
-[CFXFaceReticleView animojiBounceAnimator];
-[CFXFaceReticleView animojiCloseAnimationWithCompletion:];
-[CFXFaceReticleView animojiFadeInAnimation];
-[CFXFaceReticleView animojiFadeOutAnimator];
-[CFXFaceReticleView bounceAnimator];
-[CFXFaceReticleView canPerformFadeInAnimations];
-[CFXFaceReticleView canPerformFadeOutAnimations];
-[CFXFaceReticleView fadeOutAndEndHapticWithCompletionBlock:];
-[CFXFaceReticleView hideAnimojiFaceReticleAnimatedWithCompletion:];
-[CFXFaceReticleView initWithFrame:reticleType:];
-[CFXFaceReticleView isShowingFaceIndicator];
-[CFXFaceReticleView reticleImageView];
-[CFXFaceReticleView reticleLayersToAnimate];
-[CFXFaceReticleView setAnimojiBounceAnimator:];
-[CFXFaceReticleView setAnimojiFadeOutAnimator:];
-[CFXFaceReticleView setBounceAnimator:];
-[CFXFaceReticleView setCanPerformFadeInAnimations:];
-[CFXFaceReticleView setIsShowingFaceIndicator:];
-[CFXFaceReticleView setReticleImageView:];
-[CFXFaceReticleView setReticleLayersToAnimate:];
-[CFXFaceReticleView setupAnimojiReticleLayers];
-[CFXFaceReticleView shouldUseHapticFeedback:];
-[CFXFaceReticleView showAndAnimateAnimojiFaceReticle];
-[CFXFaceReticleView updateFrameForDisplayRelativeToBounds:];
-[CFXFaceReticleView userFeedbackForTrackingType:needsHaptics:];
```
