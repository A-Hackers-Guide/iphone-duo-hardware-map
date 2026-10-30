# `PLAWDBattery`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 9 instance variables, 9 properties, 30 instance methods, 3 class methods

## Instance variables

```
B _prevDeviceCharging;
B _prevDisplayON;
@"PLEntryNotificationOperatorComposition" _batteryEventCallback;
@"PLEntryNotificationOperatorComposition" _displayEventCallback;
d _prevCapacity;
d _prevVoltage;
q _dispOnOffCnt;
d _prevDispTimeStamp;
q _batterySubmitCnt;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryEventCallback) batteryEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayEventCallback) displayEventCallback;
@property (Td,V_prevCapacity) prevCapacity;
@property (Td,V_prevVoltage) prevVoltage;
@property (TB,V_prevDeviceCharging) prevDeviceCharging;
@property (TB,V_prevDisplayON) prevDisplayON;
@property (Tq,V_dispOnOffCnt) dispOnOffCnt;
@property (Td,V_prevDispTimeStamp) prevDispTimeStamp;
@property (Tq,V_batterySubmitCnt) batterySubmitCnt;
```

## Class methods

```
+[PLAWDBattery entryAggregateDefinitions];
+[PLAWDBattery entryAggregateDefinitionAwdBattery];
+[PLAWDBattery getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDBattery resetBatteryTable];
-[PLAWDBattery handleBatteryCallback:];
-[PLAWDBattery handleDisplayCallback:];
-[PLAWDBattery setPrevVoltage:];
-[PLAWDBattery addEntryToBatteryTable:withValue:];
-[PLAWDBattery batteryEventCallback];
-[PLAWDBattery batterySubmitCnt];
-[PLAWDBattery dispOnOffCnt];
-[PLAWDBattery displayEventCallback];
-[PLAWDBattery finalizeBatteryTable];
-[PLAWDBattery initBatteryStats];
-[PLAWDBattery isDeviceCharging:];
-[PLAWDBattery prevCapacity];
-[PLAWDBattery prevDeviceCharging];
-[PLAWDBattery prevDispTimeStamp];
-[PLAWDBattery prevDisplayON];
-[PLAWDBattery prevVoltage];
-[PLAWDBattery processEnergyConsumedAndAddEntry:withVoltage:];
-[PLAWDBattery reInitBatteryStats];
-[PLAWDBattery setBatteryEventCallback:];
-[PLAWDBattery setBatterySubmitCnt:];
-[PLAWDBattery setDispOnOffCnt:];
-[PLAWDBattery setDisplayEventCallback:];
-[PLAWDBattery setPrevCapacity:];
-[PLAWDBattery setPrevDeviceCharging:];
-[PLAWDBattery setPrevDispTimeStamp:];
-[PLAWDBattery setPrevDisplayON:];
-[PLAWDBattery startMetricCollection:];
-[PLAWDBattery stopMetricCollection:];
-[PLAWDBattery submitDataToAWDServer:withAwdConn:];
```
