# `CHHapticEvent`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHHapticPlayable`
- 5 instance variables, 19 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _type;
Q _audioResID;
@"NSArray" _eventParams;
d _time;
d _duration;
```

## Properties

```
@property (TQ,R) audioResID;
@property (Td,R) fullDuration;
@property (T@"NSString",R,V_type) type;
@property (T@"NSArray",R,V_eventParams) eventParameters;
@property (Td,V_time) relativeTime;
@property (Td,V_duration) duration;
@property (T@"NSArray",R) events;
@property (T@"NSArray",R) parameters;
@property (T@"NSArray",R) parameterCurves;
@property (T@"NSString",R) patternID;
@property (T@"NSString",R) locality;
@property (T@"NSString",R) priority;
@property (T@"NSString",R) hapticPowerUsage;
@property (T@"NSString",R) audioPowerUsage;
@property (T@"NSString",R) usageCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CHHapticEvent parameterValuesFromLegacyEventType:sharpness:fullness:error:];
```

## Instance methods

```
-[CHHapticEvent audioPowerUsage];
-[CHHapticEvent priority];
-[CHHapticEvent patternID];
-[CHHapticEvent parameters];
-[CHHapticEvent initWithEventType:parameters:relativeTime:];
-[CHHapticEvent init];
-[CHHapticEvent initWithAudioResourceID:parameters:relativeTime:];
-[CHHapticEvent initWithAudioResourceID:parameters:relativeTime:duration:];
-[CHHapticEvent getType];
-[CHHapticEvent events];
-[CHHapticEvent duration];
-[CHHapticEvent setRelativeTime:];
-[CHHapticEvent eventParameters];
-[CHHapticEvent hapticPowerUsage];
-[CHHapticEvent initWithEventType:parameters:relativeTime:duration:];
-[CHHapticEvent type];
-[CHHapticEvent relativeTime];
-[CHHapticEvent fullDuration];
-[CHHapticEvent parameterCurves];
-[CHHapticEvent initWithAudioResourceIndex:parameters:time:duration:];
-[CHHapticEvent locality];
-[CHHapticEvent setDuration:];
-[CHHapticEvent resolveExternalResources:error:];
-[CHHapticEvent usageCategory];
-[CHHapticEvent audioResID];
```
