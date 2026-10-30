# `PLEventBackwardBatteryEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLEntry`
- 0 instance variables, 0 properties, 8 instance methods, 9 class methods

## Class methods

```
+[PLEventBackwardBatteryEntry load];
+[PLEventBackwardBatteryEntry entryKey];
+[PLEventBackwardBatteryEntry entryKeyPack0];
+[PLEventBackwardBatteryEntry entryKeyPack1];
+[PLEventBackwardBatteryEntry populateCellVoltageForEntry:withRawData:];
+[PLEventBackwardBatteryEntry populateCellWOMForEntry:withRawData:];
+[PLEventBackwardBatteryEntry populateDODForEntry:withRawData:];
+[PLEventBackwardBatteryEntry populateQmaxForEntry:withRawData:];
+[PLEventBackwardBatteryEntry populatewRaForEntry:withRawData:];
```

## Instance methods

```
-[PLEventBackwardBatteryEntry dealloc];
-[PLEventBackwardBatteryEntry initEntryWithRawData:];
-[PLEventBackwardBatteryEntry absoluteLevelWithRawData:];
-[PLEventBackwardBatteryEntry levelWithRawData:];
-[PLEventBackwardBatteryEntry populateAdapterPowerTierWithRawData:];
-[PLEventBackwardBatteryEntry populatePresentDODFromRawData:];
-[PLEventBackwardBatteryEntry populateTLCCounterWithRawData:];
-[PLEventBackwardBatteryEntry rawLevelWithRawData:];
```
