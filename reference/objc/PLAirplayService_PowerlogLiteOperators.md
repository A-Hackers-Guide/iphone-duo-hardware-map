# `PLAirplayService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 6 instance variables, 6 properties, 17 instance methods, 4 class methods

## Instance variables

```
B _airplayMirroringOn;
@"PLEntryNotificationOperatorComposition" _screenstateCallback;
@"PLEntryNotificationOperatorComposition" _audioAppCallback;
@"NSArray" _screenLayoutEntries;
@"NSString" _entryKeyPLScreenStateAgentScreenState;
@"NSSet" _excludedAccountingEvents;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_screenstateCallback) screenstateCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_audioAppCallback) audioAppCallback;
@property (T@"NSArray",&,V_screenLayoutEntries) screenLayoutEntries;
@property (T@"NSString",R,V_entryKeyPLScreenStateAgentScreenState) entryKeyPLScreenStateAgentScreenState;
@property (TB,V_airplayMirroringOn) airplayMirroringOn;
@property (T@"NSSet",&,V_excludedAccountingEvents) excludedAccountingEvents;
```

## Class methods

```
+[PLAirplayService load];
+[PLAirplayService defaults];
+[PLAirplayService isEnabled];
+[PLAirplayService entryAggregateDefinitions];
```

## Instance methods

```
-[PLAirplayService init];
-[PLAirplayService initOperatorDependancies];
-[PLAirplayService buildCallBack:withGroup:withHandler:];
-[PLAirplayService testService];
-[PLAirplayService screenstateCallback];
-[PLAirplayService setScreenstateCallback:];
-[PLAirplayService airplayMirroringOn];
-[PLAirplayService audioAppCallback];
-[PLAirplayService entryKeyPLScreenStateAgentScreenState];
-[PLAirplayService excludedAccountingEvents];
-[PLAirplayService handleAudioAppCallback:];
-[PLAirplayService handleScreenStateCallback:];
-[PLAirplayService screenLayoutEntries];
-[PLAirplayService setAirplayMirroringOn:];
-[PLAirplayService setAudioAppCallback:];
-[PLAirplayService setExcludedAccountingEvents:];
-[PLAirplayService setScreenLayoutEntries:];
```
