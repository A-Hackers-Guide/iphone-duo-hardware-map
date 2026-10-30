# `PLEntryNotificationOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLNSNotificationOperatorComposition`
- 0 instance variables, 0 properties, 11 instance methods, 19 class methods

## Class methods

```
+[PLEntryNotificationOperatorComposition canSleepEntryNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition canSleepEntryNotificationWithWorkQueue:withBlock:];
+[PLEntryNotificationOperatorComposition displayAODNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition displayOffNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition displayOffOrAODNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition displayOnNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition displayOnOrAODNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition displayStateChangeNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition getSBCMaxTimeInterval];
+[PLEntryNotificationOperatorComposition getSBCMinTimeInterval];
+[PLEntryNotificationOperatorComposition luxEntryNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition requestEntryForEntryKey:forOperator:withTimeout:error:];
+[PLEntryNotificationOperatorComposition significantBatteryChangeNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition significantBatteryChangeNotificationWithOperator:withMaxIntervalInSecs:withBlock:];
+[PLEntryNotificationOperatorComposition sleepEntryNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition smcPowerAccumulatedNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition smcThermalInstantNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition wakeEntryNotificationWithOperator:withBlock:];
+[PLEntryNotificationOperatorComposition wakeEntryNotificationWithWorkQueue:withBlock:];
```

## Instance methods

```
-[PLEntryNotificationOperatorComposition initWithOperator:forEntryKey:withFilter:withBlock:];
-[PLEntryNotificationOperatorComposition initNotificationTimerWithWorkQueue:withMaxInterval:withBlock:];
-[PLEntryNotificationOperatorComposition initWithOperator:forEntryKey:forUpdateOrInsert:withFilter:withBlock:];
-[PLEntryNotificationOperatorComposition initWithOperator:forEntryKey:forUpdateOrInsert:withBlock:];
-[PLEntryNotificationOperatorComposition initWithWorkQueue:forEntryKey:withFilter:withBlock:];
-[PLEntryNotificationOperatorComposition initWithWorkQueue:forEntryKey:withBlock:];
-[PLEntryNotificationOperatorComposition initNotificationTimerWithWorkQueue:withBlock:];
-[PLEntryNotificationOperatorComposition initWithOperator:forEntryKey:withBlock:];
-[PLEntryNotificationOperatorComposition initWithWorkQueue:forEntryKey:forUpdateOrInsert:withFilter:withBlock:];
-[PLEntryNotificationOperatorComposition initWithWorkQueue:forEntryKey:forUpdateOrInsert:withBlock:];
-[PLEntryNotificationOperatorComposition requestEntry];
```
