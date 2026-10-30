# `_UIStatesFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- 3 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _approachActivated;
@"NSString" _currentState;
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _playingContinuousFeedback;
```

## Properties

```
@property (TB,N,G_approachActivated,S_setApproachActivated:,V_approachActivated) approachActivated;
@property (T@"_UIStatesFeedbackGeneratorConfiguration",R,N,G_statesConfiguration) statesConfiguration;
@property (T@"NSString",&,N,V_currentState) currentState;
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,V_playingContinuousFeedback) playingContinuousFeedback;
```

## Class methods

```
+[_UIStatesFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[_UIStatesFeedbackGenerator _stats_key];
-[_UIStatesFeedbackGenerator initWithConfiguration:view:];
-[_UIStatesFeedbackGenerator initWithStyle:view:];
-[_UIStatesFeedbackGenerator transitionToState:updated:];
-[_UIStatesFeedbackGenerator transitionToState:updated:atLocation:];
-[_UIStatesFeedbackGenerator transitionToState:ended:];
-[_UIStatesFeedbackGenerator _stopPlayingContinuousFeedback];
-[_UIStatesFeedbackGenerator playingContinuousFeedback];
-[_UIStatesFeedbackGenerator initWithStyle:];
-[_UIStatesFeedbackGenerator setPlayingContinuousFeedback:];
-[_UIStatesFeedbackGenerator _statesConfiguration];
-[_UIStatesFeedbackGenerator transitionToState:ended:atLocation:];
-[_UIStatesFeedbackGenerator setCurrentState:];
-[_UIStatesFeedbackGenerator _approachActivated];
-[_UIStatesFeedbackGenerator _configurationFromState:toState:];
-[_UIStatesFeedbackGenerator currentState];
-[_UIStatesFeedbackGenerator _setApproachActivated:];
```
