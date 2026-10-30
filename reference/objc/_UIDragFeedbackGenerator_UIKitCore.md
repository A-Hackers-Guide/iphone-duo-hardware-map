# `_UIDragFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- Protocols: `UIFeedbackGeneratorUserInteractionDriven`
- 2 instance variables, 3 properties, 19 instance methods, 1 class methods

## Instance variables

```
q _state;
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _playingContinuousFeedback;
```

## Properties

```
@property (T@"_UIDragFeedbackGeneratorConfiguration",R,N,G_dragConfiguration) dragConfiguration;
@property (Tq,N,G_state,S_setState:,V_state) state;
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,G_playingContinuousFeedback,S_setPlayingContinuousFeedback:,V_playingContinuousFeedback) playingContinuousFeedback;
```

## Class methods

```
+[_UIDragFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[_UIDragFeedbackGenerator userInteractionStartedAtLocation:];
-[_UIDragFeedbackGenerator _state];
-[_UIDragFeedbackGenerator _stats_key];
-[_UIDragFeedbackGenerator userInteractionCancelledAtLocation:];
-[_UIDragFeedbackGenerator userInteractionStarted];
-[_UIDragFeedbackGenerator userInteractionEnded];
-[_UIDragFeedbackGenerator _setPlayingContinuousFeedback:];
-[_UIDragFeedbackGenerator userInteractionEndedAtLocation:];
-[_UIDragFeedbackGenerator userInteractionCancelled];
-[_UIDragFeedbackGenerator _playingContinuousFeedback];
-[_UIDragFeedbackGenerator _setState:];
-[_UIDragFeedbackGenerator _stopPlayingContinuousFeedback];
-[_UIDragFeedbackGenerator dropTargetUpdated];
-[_UIDragFeedbackGenerator positionUpdated];
-[_UIDragFeedbackGenerator _startPlayingContinuousFeedback];
-[_UIDragFeedbackGenerator _dragConfiguration];
-[_UIDragFeedbackGenerator _startPlayingContinuousFeedbackNow];
-[_UIDragFeedbackGenerator dropTargetUpdatedAtLocation:];
-[_UIDragFeedbackGenerator positionUpdatedAtLocation:];
```
