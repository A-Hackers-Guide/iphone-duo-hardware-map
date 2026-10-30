# `_UIContinuousFeedback`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackContinuousPlayable`
- 2 instance variables, 7 properties, 14 instance methods, 3 class methods

## Instance variables

```
d _duration;
q _type;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (Td,N,V_duration) duration;
@property (TB,R,N,GisPlaying) playing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIContinuousFeedback supportsSecureCoding];
+[_UIContinuousFeedback type];
+[_UIContinuousFeedback continuousFeedbackForType:];
```

## Instance methods

```
-[_UIContinuousFeedback initWithDictionaryRepresentation:];
-[_UIContinuousFeedback init];
-[_UIContinuousFeedback duration];
-[_UIContinuousFeedback _effectiveEventType];
-[_UIContinuousFeedback setType:];
-[_UIContinuousFeedback type];
-[_UIContinuousFeedback _playableProtocol];
-[_UIContinuousFeedback setDuration:];
-[_UIContinuousFeedback copyWithZone:];
-[_UIContinuousFeedback isEqual:];
-[_UIContinuousFeedback _debugDictionary];
-[_UIContinuousFeedback dictionaryRepresentation];
-[_UIContinuousFeedback _effectiveDuration];
-[_UIContinuousFeedback _playedAtTime:engine:];
```
