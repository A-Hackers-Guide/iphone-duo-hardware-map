# `PatternPlayer`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PatternPlayerBase`
- Protocols: `CHHapticPatternPlayerExtended`
- 1 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"AVHapticPlayerChannel" _channel;
```

## Properties

```
@property (TB) isMuted;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PatternPlayer isMuted];
-[PatternPlayer doSetMute:];
-[PatternPlayer sendParameters:atTime:error:];
-[PatternPlayer clearExternalResources:];
-[PatternPlayer stopAtTime:error:];
-[PatternPlayer startAtTime:error:];
-[PatternPlayer cancelAndReturnError:];
-[PatternPlayer setIsMuted:];
-[PatternPlayer init];
-[PatternPlayer dealloc];
-[PatternPlayer scheduleParameterCurve:atTime:error:];
-[PatternPlayer processImmediateParameters:];
-[PatternPlayer startAtTime:withImmediateParameters:error:];
-[PatternPlayer releaseExternalResources:events:];
-[PatternPlayer initWithPlayable:engine:privileged:error:];
```
