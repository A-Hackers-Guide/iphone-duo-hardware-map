# `_UIFeedbackPattern`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackDiscretePlayable`, `_UIFeedbackContinuousPlayable`
- 6 instance variables, 10 properties, 30 instance methods, 4 class methods

## Instance variables

```
B _canReuseCoreHapticsPlayer;
B _highPriority;
B _isRepeating;
d _duration;
@"NSMutableArray" _feedbacks;
@"NSTimer" _repeatTimer;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_feedbacks) feedbacks;
@property (TB,R,N,V_isRepeating) isRepeating;
@property (T@"NSTimer",&,N,V_repeatTimer) repeatTimer;
@property (TB,R,N,GisHighPriority,V_highPriority) highPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_duration) duration;
@property (TB,R,N,GisPlaying) playing;
```

## Class methods

```
+[_UIFeedbackPattern supportsSecureCoding];
+[_UIFeedbackPattern type];
+[_UIFeedbackPattern feedbackPattern];
+[_UIFeedbackPattern _parametersClass];
```

## Instance methods

```
-[_UIFeedbackPattern feedbacks];
-[_UIFeedbackPattern _view];
-[_UIFeedbackPattern setFeedbacks:];
-[_UIFeedbackPattern isHighPriority];
-[_UIFeedbackPattern _effectivePlayableFeedbackTypes];
-[_UIFeedbackPattern initWithDictionaryRepresentation:];
-[_UIFeedbackPattern play];
-[_UIFeedbackPattern _allEventTypes];
-[_UIFeedbackPattern stop];
-[_UIFeedbackPattern isPlaying];
-[_UIFeedbackPattern setCanReuseCoreHapticsPlayer:];
-[_UIFeedbackPattern setRepeatTimer:];
-[_UIFeedbackPattern duration];
-[_UIFeedbackPattern _setView:];
-[_UIFeedbackPattern isRepeating];
-[_UIFeedbackPattern _setLocation:];
-[_UIFeedbackPattern addFeedback:atTime:];
-[_UIFeedbackPattern _playableProtocol];
-[_UIFeedbackPattern _individualFeedbacks];
-[_UIFeedbackPattern canReuseCoreHapticsPlayer];
-[_UIFeedbackPattern setDuration:];
-[_UIFeedbackPattern _location];
-[_UIFeedbackPattern repeatTimer];
-[_UIFeedbackPattern setPosition:];
-[_UIFeedbackPattern copyWithZone:];
-[_UIFeedbackPattern _playPattern];
-[_UIFeedbackPattern _allSystemSoundIDs];
-[_UIFeedbackPattern isEqual:];
-[_UIFeedbackPattern _debugDictionary];
-[_UIFeedbackPattern dictionaryRepresentation];
```
