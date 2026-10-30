# `_UICustomDiscreteFeedback`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDiscreteFeedback`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
I _systemSoundID;
Q _eventType;
```

## Properties

```
@property (TQ,R,N,V_eventType) eventType;
@property (TI,R,N,V_systemSoundID) systemSoundID;
```

## Class methods

```
+[_UICustomDiscreteFeedback customDiscreteFeedbackWithEventType:systemSoundID:];
+[_UICustomDiscreteFeedback type];
```

## Instance methods

```
-[_UICustomDiscreteFeedback _effectiveSystemSoundID];
-[_UICustomDiscreteFeedback initWithDictionaryRepresentation:];
-[_UICustomDiscreteFeedback eventType];
-[_UICustomDiscreteFeedback systemSoundID];
-[_UICustomDiscreteFeedback _effectiveEventType];
-[_UICustomDiscreteFeedback copyWithZone:];
-[_UICustomDiscreteFeedback isEqual:];
-[_UICustomDiscreteFeedback dictionaryRepresentation];
```
