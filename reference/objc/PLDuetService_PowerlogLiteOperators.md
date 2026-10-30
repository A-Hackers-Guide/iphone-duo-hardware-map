# `PLDuetService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 3 instance variables, 3 properties, 11 instance methods, 10 class methods

## Instance variables

```
@"PLDuetServiceLpmSource" _lpmSource;
@"PLDuetServiceDAS" _dasEvent;
@"PLDuetServiceImpl" _impl;
```

## Properties

```
@property (T@"PLDuetServiceLpmSource",R,V_lpmSource) lpmSource;
@property (T@"PLDuetServiceDAS",R,V_dasEvent) dasEvent;
@property (T@"PLDuetServiceImpl",R,V_impl) impl;
```

## Class methods

```
+[PLDuetService entryEventIntervalDefinitions];
+[PLDuetService entryEventForwardDefinitions];
+[PLDuetService entryEventBackwardDefinitions];
+[PLDuetService entryEventNoneDefinitions];
+[PLDuetService load];
+[PLDuetService entryAggregateDefinitions];
+[PLDuetService aggregateNameDuetEnergyAccumulator];
+[PLDuetService entryEventForwardDefinitionBatterySaverMode];
+[PLDuetService eventIntervalDefinitionComplicationEvents];
+[PLDuetService eventIntervalDefinitionDuetEvents];
```

## Instance methods

```
-[PLDuetService impl];
-[PLDuetService init];
-[PLDuetService dealloc];
-[PLDuetService initOperatorDependancies];
-[PLDuetService trimConditionsForEntryKey:forTrimDate:];
-[PLDuetService dasEvent];
-[PLDuetService handleBatterySaverModeToken:withNotification:];
-[PLDuetService logEventForwardBatterySaverModeWithState:fromNotification:];
-[PLDuetService lpmSource];
-[PLDuetService registrationModeStringToEnum:];
-[PLDuetService setupBatterySaverModeForNotification:];
```
