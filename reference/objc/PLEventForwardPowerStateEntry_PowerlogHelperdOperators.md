# `PLEventForwardPowerStateEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLMultiKeyEntry`
- 0 instance variables, 4 properties, 9 instance methods, 2 class methods

## Properties

```
@property (Ts,R) state;
@property (Ts,R) event;
@property (T@"NSArray",R) reason;
@property (TB,R) isBasebandWake;
```

## Class methods

```
+[PLEventForwardPowerStateEntry load];
+[PLEventForwardPowerStateEntry entryKey];
```

## Instance methods

```
-[PLEventForwardPowerStateEntry event];
-[PLEventForwardPowerStateEntry reason];
-[PLEventForwardPowerStateEntry state];
-[PLEventForwardPowerStateEntry initEntryWithIOMessage:];
-[PLEventForwardPowerStateEntry initEntryWithState:withEvent:withReason:withCurrentWakeTime:withCurrentWakeTimeKey:withDate:];
-[PLEventForwardPowerStateEntry initEntryWithState:withEvent:withReason:withCurrentWakeTime:withCurrentWakeTimeKey:withWakeType:withDriverWakeReason:withDate:];
-[PLEventForwardPowerStateEntry initEntryWithState:withEvent:withReason:withDate:];
-[PLEventForwardPowerStateEntry initEntryWithState:withEvent:withReason:withKernelSleepDate:withDate:];
-[PLEventForwardPowerStateEntry isBasebandWake];
```
