# `_UITransientHapticFeedback`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackDiscretePlayable`, `_UIFeedbackTransientHaptic_Internal`, `_UIFeedbackCoreHapticsPlayerReuse_Internal`
- 3 instance variables, 8 properties, 10 instance methods, 3 class methods

## Instance variables

```
B _highPriority;
f _intensity;
f _sharpness;
```

## Properties

```
@property (TB,R,N,GisHighPriority,V_highPriority) highPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tf,R,N,V_intensity) intensity;
@property (Tf,R,N,V_sharpness) sharpness;
@property (TB,R,N) canReuseCoreHapticsPlayer;
```

## Class methods

```
+[_UITransientHapticFeedback supportsSecureCoding];
+[_UITransientHapticFeedback type];
+[_UITransientHapticFeedback transientHapticFeedbackWithIntensity:sharpness:];
```

## Instance methods

```
-[_UITransientHapticFeedback isHighPriority];
-[_UITransientHapticFeedback intensity];
-[_UITransientHapticFeedback _effectivePlayableFeedbackTypes];
-[_UITransientHapticFeedback initWithDictionaryRepresentation:];
-[_UITransientHapticFeedback sharpness];
-[_UITransientHapticFeedback _playableProtocol];
-[_UITransientHapticFeedback canReuseCoreHapticsPlayer];
-[_UITransientHapticFeedback copyWithZone:];
-[_UITransientHapticFeedback isEqual:];
-[_UITransientHapticFeedback dictionaryRepresentation];
```
