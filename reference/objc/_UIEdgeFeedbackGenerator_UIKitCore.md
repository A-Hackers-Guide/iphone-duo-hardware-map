# `_UIEdgeFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFeedbackGenerator`
- Protocols: `UIFeedbackGeneratorUserInteractionDriven`
- 15 instance variables, 17 properties, 52 instance methods, 1 class methods

## Instance variables

```
@"_UIFeedbackEngine" _feedbackEngine;
B _playedOvershotThresholdFeedback;
B _closeToEdge;
d _distance;
q _axis;
d _extentBeyondDistance;
d _closeToEdgeUpdateTime;
d _value;
d _previousValue;
q _lastState;
d _lastValueUpdateTime;
d _previousValueUpdateTime;
d _velocity;
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _playingContinuousFeedback;
q _state;
```

## Properties

```
@property (T@"_UIEdgeFeedbackGeneratorConfiguration",R,N,G_edgeConfiguration) edgeConfiguration;
@property (TB,N,G_isCloseToEdge,S_setCloseToEdge:,V_closeToEdge) closeToEdge;
@property (Td,N,G_closeToEdgeUpdateTime,S_setCloseToEdgeUpdateTime:,V_closeToEdgeUpdateTime) closeToEdgeUpdateTime;
@property (Td,N,G_value,S_setValue:,V_value) value;
@property (Td,N,G_previousValue,S_setPreviousValue:,V_previousValue) previousValue;
@property (Tq,N,G_lastState,S_setLastState:,V_lastState) lastState;
@property (Td,N,G_lastValueUpdateTime,S_setLastValueUpdateTime:,V_lastValueUpdateTime) lastValueUpdateTime;
@property (Td,N,G_previousValueUpdateTime,S_setPreviousValueUpdateTime:,V_previousValueUpdateTime) previousValueUpdateTime;
@property (Td,N,G_velocity,S_setVelocity:,V_velocity) velocity;
@property (TB,R,N,G_isOvershot) overshot;
@property (Tf,R,N,G_percentBeyondDistance) percentBeyondDistance;
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,G_playingContinuousFeedback,S_setPlayingContinuousFeedback:,V_playingContinuousFeedback) playingContinuousFeedback;
@property (Td,R,N,G_effectiveDistance) effectiveDistance;
@property (Tq,N,G_state,S_setState:,V_state) state;
@property (Tq,N,V_axis) axis;
@property (Td,N,V_distance) distance;
@property (Td,N,V_extentBeyondDistance) extentBeyondDistance;
```

## Class methods

```
+[_UIEdgeFeedbackGenerator _configurationClass];
```

## Instance methods

```
-[_UIEdgeFeedbackGenerator _setValue:];
-[_UIEdgeFeedbackGenerator userInteractionStartedAtLocation:];
-[_UIEdgeFeedbackGenerator _stopAnimatingWithTimeout:];
-[_UIEdgeFeedbackGenerator _positionUpdated:withVelocity:atLocation:];
-[_UIEdgeFeedbackGenerator _state];
-[_UIEdgeFeedbackGenerator _setVelocity:];
-[_UIEdgeFeedbackGenerator positionUpdated:atLocation:];
-[_UIEdgeFeedbackGenerator _percentBeyondDistance];
-[_UIEdgeFeedbackGenerator _setCloseToEdge:];
-[_UIEdgeFeedbackGenerator _isCloseToEdge];
-[_UIEdgeFeedbackGenerator _closeToEdgeUpdateTime];
-[_UIEdgeFeedbackGenerator _stats_key];
-[_UIEdgeFeedbackGenerator _velocity];
-[_UIEdgeFeedbackGenerator _setPreviousValueUpdateTime:];
-[_UIEdgeFeedbackGenerator userInteractionCancelledAtLocation:];
-[_UIEdgeFeedbackGenerator _setLastValueUpdateTime:];
-[_UIEdgeFeedbackGenerator _valueIsOvershot:];
-[_UIEdgeFeedbackGenerator axis];
-[_UIEdgeFeedbackGenerator distance];
-[_UIEdgeFeedbackGenerator userInteractionStarted];
-[_UIEdgeFeedbackGenerator _setLastState:];
-[_UIEdgeFeedbackGenerator _previousValueUpdateTime];
-[_UIEdgeFeedbackGenerator _previousValue];
-[_UIEdgeFeedbackGenerator _effectiveDistance];
-[_UIEdgeFeedbackGenerator extentBeyondDistance];
-[_UIEdgeFeedbackGenerator positionUpdated:];
-[_UIEdgeFeedbackGenerator _animationStartedUsingTimeout:];
-[_UIEdgeFeedbackGenerator initWithConfiguration:view:];
-[_UIEdgeFeedbackGenerator setDistance:];
-[_UIEdgeFeedbackGenerator _value];
-[_UIEdgeFeedbackGenerator userInteractionEnded];
-[_UIEdgeFeedbackGenerator _setPreviousValue:];
-[_UIEdgeFeedbackGenerator _setPlayingContinuousFeedback:];
-[_UIEdgeFeedbackGenerator userInteractionEndedAtLocation:];
-[_UIEdgeFeedbackGenerator _isOvershot];
-[_UIEdgeFeedbackGenerator _edgeConfiguration];
-[_UIEdgeFeedbackGenerator _cancelStopAnimatingTimeout];
-[_UIEdgeFeedbackGenerator _setCloseToEdgeUpdateTime:];
-[_UIEdgeFeedbackGenerator initWithStyle:view:];
-[_UIEdgeFeedbackGenerator _deactivate];
-[_UIEdgeFeedbackGenerator setAxis:];
-[_UIEdgeFeedbackGenerator userInteractionCancelled];
-[_UIEdgeFeedbackGenerator _lastValueUpdateTime];
-[_UIEdgeFeedbackGenerator initWithStyle:coordinateSpace:];
-[_UIEdgeFeedbackGenerator _animationEnded];
-[_UIEdgeFeedbackGenerator _updateCloseToEdge];
-[_UIEdgeFeedbackGenerator _playingContinuousFeedback];
-[_UIEdgeFeedbackGenerator setExtentBeyondDistance:];
-[_UIEdgeFeedbackGenerator _setState:];
-[_UIEdgeFeedbackGenerator _lastState];
-[_UIEdgeFeedbackGenerator _animationStarted];
-[_UIEdgeFeedbackGenerator initWithStyle:];
```
