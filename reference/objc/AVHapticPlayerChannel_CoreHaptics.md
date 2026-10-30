# `AVHapticPlayerChannel`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
Q _chanID;
Q _behavior;
@"AVHapticClient" _client;
```

## Properties

```
@property (TQ,V_chanID) chanID;
@property (T@"AVHapticClient",W,V_client) client;
@property (TQ) eventBehavior;
@property (TB,R) invalidated;
```

## Instance methods

```
-[AVHapticPlayerChannel setEventBehavior:];
-[AVHapticPlayerChannel setChanID:];
-[AVHapticPlayerChannel scheduleParameterCurve:curve:atTime:error:];
-[AVHapticPlayerChannel invalidated];
-[AVHapticPlayerChannel eventBehavior];
-[AVHapticPlayerChannel clearEvents:error:];
-[AVHapticPlayerChannel chanID];
-[AVHapticPlayerChannel setClient:];
-[AVHapticPlayerChannel invalidate];
-[AVHapticPlayerChannel sendEvents:atTime:error:];
-[AVHapticPlayerChannel resetAtTime:error:];
-[AVHapticPlayerChannel initWithChannelID:client:];
-[AVHapticPlayerChannel client];
-[AVHapticPlayerChannel setParameter:value:atTime:error:];
-[AVHapticPlayerChannel sendEvents:withImmediateParameters:atTime:error:];
```
