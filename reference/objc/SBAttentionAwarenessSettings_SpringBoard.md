# `SBAttentionAwarenessSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUISettings`
- Protocols: `MCProfileConnectionObserver`
- 8 instance variables, 8 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _allowsAttentionAwareAutoLock;
B _supportsAttentionSensor;
B _shouldUseAttentionSensor;
B _isObservingDataSources;
^{AWNotification_s=} _attentionAwarenessToken;
d _sampleInterval;
d _dimInterval;
d _sleepInterval;
```

## Properties

```
@property (TB,N) shouldUseAttentionSensor;
@property (Td,N,V_sampleInterval) sampleInterval;
@property (Td,N,V_dimInterval) dimInterval;
@property (Td,N,V_sleepInterval) sleepInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAttentionAwarenessSettings settingsControllerModule];
+[SBAttentionAwarenessSettings attentionSensorSupported];
```

## Instance methods

```
-[SBAttentionAwarenessSettings profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[SBAttentionAwarenessSettings sampleInterval];
-[SBAttentionAwarenessSettings dealloc];
-[SBAttentionAwarenessSettings setSampleInterval:];
-[SBAttentionAwarenessSettings setDefaultValues];
-[SBAttentionAwarenessSettings setDimInterval:];
-[SBAttentionAwarenessSettings dimInterval];
-[SBAttentionAwarenessSettings setShouldUseAttentionSensor:];
-[SBAttentionAwarenessSettings setSleepInterval:];
-[SBAttentionAwarenessSettings shouldUseAttentionSensor];
-[SBAttentionAwarenessSettings sleepInterval];
```
