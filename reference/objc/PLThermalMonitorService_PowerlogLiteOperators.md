# `PLThermalMonitorService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"PLEntryNotificationOperatorComposition" _smcNotification;
@"PLXPCResponderOperatorComposition" _sysdiagnoseResponder;
@"PLXPCResponderOperatorComposition" _powerHUDResponder;
@"PLNSNotificationOperatorComposition" _thermalNotification;
@"NSDate" _lastSMCThermalTrigger;
@"NSDate" _sustainedStartDate;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_smcNotification) smcNotification;
@property (T@"PLXPCResponderOperatorComposition",&,V_sysdiagnoseResponder) sysdiagnoseResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_powerHUDResponder) powerHUDResponder;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalNotification) thermalNotification;
@property (T@"NSDate",&,V_lastSMCThermalTrigger) lastSMCThermalTrigger;
@property (T@"NSDate",&,V_sustainedStartDate) sustainedStartDate;
```

## Class methods

```
+[PLThermalMonitorService load];
```

## Instance methods

```
-[PLThermalMonitorService init];
-[PLThermalMonitorService initOperatorDependancies];
-[PLThermalMonitorService performLogging:];
-[PLThermalMonitorService smcNotification];
-[PLThermalMonitorService handlePowerHUDCallback:];
-[PLThermalMonitorService handleSMCCallback:];
-[PLThermalMonitorService handleSysdiagnoseCallback:];
-[PLThermalMonitorService lastSMCThermalTrigger];
-[PLThermalMonitorService performLoggingWithCadence:withDate:];
-[PLThermalMonitorService powerHUDResponder];
-[PLThermalMonitorService setLastSMCThermalTrigger:];
-[PLThermalMonitorService setPowerHUDResponder:];
-[PLThermalMonitorService setSmcNotification:];
-[PLThermalMonitorService setSustainedStartDate:];
-[PLThermalMonitorService setSysdiagnoseResponder:];
-[PLThermalMonitorService setThermalNotification:];
-[PLThermalMonitorService sustainedStartDate];
-[PLThermalMonitorService sysdiagnoseResponder];
-[PLThermalMonitorService thermalNotification];
```
