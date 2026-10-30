# `_UIDiscreteFeedback`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackDiscretePlayable`
- 2 instance variables, 6 properties, 12 instance methods, 3 class methods

## Instance variables

```
B _highPriority;
q _type;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (TB,R,N,GisHighPriority,V_highPriority) highPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDiscreteFeedback supportsSecureCoding];
+[_UIDiscreteFeedback discreteFeedbackForType:];
+[_UIDiscreteFeedback type];
```

## Instance methods

```
-[_UIDiscreteFeedback isHighPriority];
-[_UIDiscreteFeedback _effectiveSystemSoundID];
-[_UIDiscreteFeedback initWithDictionaryRepresentation:];
-[_UIDiscreteFeedback isPlaying];
-[_UIDiscreteFeedback _effectiveEventType];
-[_UIDiscreteFeedback setType:];
-[_UIDiscreteFeedback type];
-[_UIDiscreteFeedback _playableProtocol];
-[_UIDiscreteFeedback copyWithZone:];
-[_UIDiscreteFeedback isEqual:];
-[_UIDiscreteFeedback _debugDictionary];
-[_UIDiscreteFeedback dictionaryRepresentation];
```
