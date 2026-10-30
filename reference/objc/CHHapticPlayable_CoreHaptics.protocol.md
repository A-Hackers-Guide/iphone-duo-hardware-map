# `CHHapticPlayable` (protocol)

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R) events;
@property (T@"NSArray",R) parameters;
@property (T@"NSArray",R) parameterCurves;
@property (T@"NSString",R) patternID;
@property (Td,R) duration;
@property (T@"NSString",R) locality;
@property (T@"NSString",R) priority;
@property (T@"NSString",R) hapticPowerUsage;
@property (T@"NSString",R) audioPowerUsage;
@property (T@"NSString",R) usageCategory;
```

## Instance methods

```
-[CHHapticPlayable audioPowerUsage];
-[CHHapticPlayable priority];
-[CHHapticPlayable patternID];
-[CHHapticPlayable parameters];
-[CHHapticPlayable events];
-[CHHapticPlayable duration];
-[CHHapticPlayable hapticPowerUsage];
-[CHHapticPlayable parameterCurves];
-[CHHapticPlayable locality];
-[CHHapticPlayable resolveExternalResources:error:];
-[CHHapticPlayable usageCategory];
```
