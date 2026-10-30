# `CHHapticPattern`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHHapticPlayable`
- 8 instance variables, 16 properties, 22 instance methods, 3 class methods

## Instance variables

```
@"NSURL" _ahapBaseURL;
@"NSNumber" _version;
@"NSString" _patternID;
@"NSDictionary" _configurationDictionary;
@"NSMutableArray" _embeddedResourceInfo;
@"NSMutableArray" _events;
@"NSMutableArray" _parameters;
@"NSMutableArray" _parameterCurves;
```

## Properties

```
@property (Tf,R) version;
@property (T@"NSDictionary",R,N,V_configurationDictionary) configurationDictionary;
@property (Td,R,N) duration;
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
+[CHHapticPattern patternForKey:error:];
+[CHHapticPattern eventListFromEvents:parameters:parameterCurves:engine:privileged:];
+[CHHapticPattern addHapticsForWheelsOfTime:];
```

## Instance methods

```
-[CHHapticPattern audioPowerUsage];
-[CHHapticPattern priority];
-[CHHapticPattern initWithDictionary:error:];
-[CHHapticPattern patternID];
-[CHHapticPattern parameters];
-[CHHapticPattern initWithEvents:parameterCurves:error:];
-[CHHapticPattern init];
-[CHHapticPattern exportDictionaryWithConfigurationAndReturnError:];
-[CHHapticPattern initWithEvents:parameters:error:];
-[CHHapticPattern version];
-[CHHapticPattern events];
-[CHHapticPattern duration];
-[CHHapticPattern initWithContentsOfURL:error:];
-[CHHapticPattern hapticPowerUsage];
-[CHHapticPattern parameterCurves];
-[CHHapticPattern exportDictionaryAndReturnError:];
-[CHHapticPattern locality];
-[CHHapticPattern configurationDictionary];
-[CHHapticPattern eventListFromDictionary:error:];
-[CHHapticPattern resolveExternalResources:error:];
-[CHHapticPattern doInitWithDictionary:error:];
-[CHHapticPattern usageCategory];
```
