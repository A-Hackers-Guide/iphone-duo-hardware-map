# `_UIFeedbackParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 10 properties, 25 instance methods, 1 class methods

## Instance variables

```
f _volume;
f _rate;
f _transposition;
f _attackTime;
f _decayTime;
f _releaseTime;
@"_UIFeedback" _feedback;
@"_UIFeedbackParameters" _parentParameters;
```

## Properties

```
@property (T@"_UIFeedback",W,N,V_feedback) feedback;
@property (T@"_UIFeedbackParameters",W,N,V_parentParameters) parentParameters;
@property (TB,R,N,G_isAudio) audio;
@property (Tf,R,N,G_effectiveVolume) effectiveVolume;
@property (Tf,N,V_volume) volume;
@property (Tf,N,V_rate) rate;
@property (Tf,N,V_transposition) transposition;
@property (Tf,N,V_attackTime) attackTime;
@property (Tf,N,V_decayTime) decayTime;
@property (Tf,N,V_releaseTime) releaseTime;
```

## Class methods

```
+[_UIFeedbackParameters parameters];
```

## Instance methods

```
-[_UIFeedbackParameters feedback];
-[_UIFeedbackParameters rate];
-[_UIFeedbackParameters releaseTime];
-[_UIFeedbackParameters _isAudio];
-[_UIFeedbackParameters _effectiveVolume];
-[_UIFeedbackParameters initWithFeedback:];
-[_UIFeedbackParameters setFeedback:];
-[_UIFeedbackParameters volume];
-[_UIFeedbackParameters decayTime];
-[_UIFeedbackParameters setVolume:];
-[_UIFeedbackParameters setRate:];
-[_UIFeedbackParameters setDecayTime:];
-[_UIFeedbackParameters setParentParameters:];
-[_UIFeedbackParameters attackTime];
-[_UIFeedbackParameters setAttackTime:];
-[_UIFeedbackParameters parentParameters];
-[_UIFeedbackParameters initWithDictionaryRepresentation:feedback:];
-[_UIFeedbackParameters setReleaseTime:];
-[_UIFeedbackParameters setTransposition:];
-[_UIFeedbackParameters transposition];
-[_UIFeedbackParameters _updateParameterWithKey:];
-[_UIFeedbackParameters _effectiveValueForParameterWithKey:];
-[_UIFeedbackParameters copyWithZone:];
-[_UIFeedbackParameters isEqual:];
-[_UIFeedbackParameters dictionaryRepresentation];
```
