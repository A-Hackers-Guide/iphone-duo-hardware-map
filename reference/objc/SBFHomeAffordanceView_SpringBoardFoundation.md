# `SBFHomeAffordanceView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
Q _hintStyle;
@"SBFHomeGrabberSettings" _homeGrabberSettings;
@"SBFSiriSystemAssistantExperienceSettings" _systemAssistantExperienceSettings;
@"UIView" _topLevelContainerView;
@"UIVisualEffectView" _visualEffectView;
@"UIView" _contentViewContainerView;
q _bounceAnimationGenerationCount;
q _glowAnimationGenerationCount;
q _pulseAnimationGenerationCount;
q _outstandingGlowOrPulseAnimationCount;
```

## Properties

```
@property (T@"SBFHomeGrabberSettings",R,N,V_homeGrabberSettings) homeGrabberSettings;
@property (T@"SBFSiriSystemAssistantExperienceSettings",R,N,V_systemAssistantExperienceSettings) systemAssistantExperienceSettings;
@property (T@"UIView",W,N,V_topLevelContainerView) topLevelContainerView;
@property (T@"UIVisualEffectView",W,N,V_visualEffectView) visualEffectView;
@property (T@"UIView",W,N,V_contentViewContainerView) contentViewContainerView;
@property (Tq,N,V_bounceAnimationGenerationCount) bounceAnimationGenerationCount;
@property (Tq,N,V_glowAnimationGenerationCount) glowAnimationGenerationCount;
@property (Tq,N,V_pulseAnimationGenerationCount) pulseAnimationGenerationCount;
@property (Tq,N,V_outstandingGlowOrPulseAnimationCount) outstandingGlowOrPulseAnimationCount;
@property (TQ,N,V_hintStyle) hintStyle;
```

## Instance methods

```
-[SBFHomeAffordanceView contentViewContainerView];
-[SBFHomeAffordanceView homeGrabberSettings];
-[SBFHomeAffordanceView visualEffectView];
-[SBFHomeAffordanceView setGlowAnimationGenerationCount:];
-[SBFHomeAffordanceView _incrementBounceAnimationGenerationCount];
-[SBFHomeAffordanceView performHintAnimationWithCompletionHandler:];
-[SBFHomeAffordanceView glowAnimationGenerationCount];
-[SBFHomeAffordanceView _incrementGlowAnimationGenerationCount];
-[SBFHomeAffordanceView pulseAnimationGenerationCount];
-[SBFHomeAffordanceView removeContentView:];
-[SBFHomeAffordanceView cancelHintAnimationWithCompletionHandler:];
-[SBFHomeAffordanceView setOutstandingGlowOrPulseAnimationCount:];
-[SBFHomeAffordanceView topLevelContainerView];
-[SBFHomeAffordanceView setTopLevelContainerView:];
-[SBFHomeAffordanceView layoutSubviews];
-[SBFHomeAffordanceView setVisualEffectView:];
-[SBFHomeAffordanceView addContentView:];
-[SBFHomeAffordanceView setPulseAnimationGenerationCount:];
-[SBFHomeAffordanceView hintStyle];
-[SBFHomeAffordanceView insertContentView:atIndex:];
-[SBFHomeAffordanceView setBounceAnimationGenerationCount:];
-[SBFHomeAffordanceView _incrementPulseAnimationGenerationCount];
-[SBFHomeAffordanceView setContentViewContainerView:];
-[SBFHomeAffordanceView performHintAnimation];
-[SBFHomeAffordanceView outstandingGlowOrPulseAnimationCount];
-[SBFHomeAffordanceView _performGlowAnimationWithCompletionHandler:];
-[SBFHomeAffordanceView systemAssistantExperienceSettings];
-[SBFHomeAffordanceView cancelHintAnimation];
-[SBFHomeAffordanceView setHintStyle:];
-[SBFHomeAffordanceView bounceAnimationGenerationCount];
-[SBFHomeAffordanceView _performPulseAnimationWithCompletionHandler:];
-[SBFHomeAffordanceView initWithFrame:];
-[SBFHomeAffordanceView _performBounceAnimationWithCompletionHandler:];
```
