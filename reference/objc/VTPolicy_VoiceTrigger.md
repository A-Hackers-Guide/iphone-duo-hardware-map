# `VTPolicy`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTEventMonitorDelegate`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _monitors;
@"NSMutableArray" _conditions;
@? _callback;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTPolicy defaultVoiceTriggerEnablePolicy];
```

## Instance methods

```
-[VTPolicy setCallback:];
-[VTPolicy init];
-[VTPolicy dealloc];
-[VTPolicy isEnabled];
-[VTPolicy addConditions:];
-[VTPolicy _checkAllConditionsEnabled];
-[VTPolicy subscribeEventMonitor:];
-[VTPolicy notifyCallback:];
-[VTPolicy VTEventMonitorDidReceiveEvent:];
```
