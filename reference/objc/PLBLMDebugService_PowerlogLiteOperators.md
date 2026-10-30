# `PLBLMDebugService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 9 instance variables, 9 properties, 27 instance methods, 4 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _xpcListenerBLMDebugTrigger;
@"PLEntryNotificationOperatorComposition" _ioreportCallback;
@"PLEntryNotificationOperatorComposition" _processnetworkCallback;
@"PLEntryNotificationOperatorComposition" _wifiCallback;
@"PLEntryNotificationOperatorComposition" _bbCallback;
@"PLEntryNotificationOperatorComposition" _btCallback;
@"PLEntryNotificationOperatorComposition" _displayAPLCallback;
@"PLTimer" _debugTimers;
@"NSMutableDictionary" _triggers;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_xpcListenerBLMDebugTrigger) xpcListenerBLMDebugTrigger;
@property (T@"PLEntryNotificationOperatorComposition",&,V_ioreportCallback) ioreportCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_processnetworkCallback) processnetworkCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wifiCallback) wifiCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbCallback) bbCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btCallback) btCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayAPLCallback) displayAPLCallback;
@property (T@"PLTimer",&,V_debugTimers) debugTimers;
@property (T@"NSMutableDictionary",&,V_triggers) triggers;
```

## Class methods

```
+[PLBLMDebugService entryEventNoneDefinitions];
+[PLBLMDebugService load];
+[PLBLMDebugService entryEventNoneDefinitionBLMDebug];
+[PLBLMDebugService isModelTriggerRun];
```

## Instance methods

```
-[PLBLMDebugService setTriggers:];
-[PLBLMDebugService init];
-[PLBLMDebugService initOperatorDependancies];
-[PLBLMDebugService triggers];
-[PLBLMDebugService setDebugTimers:];
-[PLBLMDebugService Testservice:];
-[PLBLMDebugService bbCallback];
-[PLBLMDebugService btCallback];
-[PLBLMDebugService debugTimers];
-[PLBLMDebugService displayAPLCallback];
-[PLBLMDebugService energyForRootNodeID:withRange:];
-[PLBLMDebugService ioreportCallback];
-[PLBLMDebugService logRailData:withTriggerName:inTimeRange:];
-[PLBLMDebugService processnetworkCallback];
-[PLBLMDebugService registerTrigger:];
-[PLBLMDebugService respondBLMDDebugQuery:];
-[PLBLMDebugService setBbCallback:];
-[PLBLMDebugService setBtCallback:];
-[PLBLMDebugService setDisplayAPLCallback:];
-[PLBLMDebugService setIoreportCallback:];
-[PLBLMDebugService setProcessnetworkCallback:];
-[PLBLMDebugService setWifiCallback:];
-[PLBLMDebugService setXpcListenerBLMDebugTrigger:];
-[PLBLMDebugService triggerLoggersNow:];
-[PLBLMDebugService triggerSelectorAtDate:withSelector:withUseInfo:];
-[PLBLMDebugService wifiCallback];
-[PLBLMDebugService xpcListenerBLMDebugTrigger];
```
