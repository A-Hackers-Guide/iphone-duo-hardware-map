# `PLPMUAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 5 instance variables, 1 properties, 6 instance methods, 10 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} hidEventSystem;
@"NSMutableDictionary" matchingSensors;
@"NSMutableArray" sensorNamesC;
@"NSMutableArray" sensorNamesV;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
```

## Class methods

```
+[PLPMUAgent entryEventIntervalDefinitions];
+[PLPMUAgent entryEventPointDefinitions];
+[PLPMUAgent entryEventForwardDefinitions];
+[PLPMUAgent entryEventBackwardDefinitions];
+[PLPMUAgent entryEventNoneDefinitions];
+[PLPMUAgent load];
+[PLPMUAgent defaults];
+[PLPMUAgent accountingGroupDefinitions];
+[PLPMUAgent railDefinitions];
+[PLPMUAgent entryAggregateDefinitions];
```

## Instance methods

```
-[PLPMUAgent init];
-[PLPMUAgent initOperatorDependancies];
-[PLPMUAgent setBatteryLevelChanged:];
-[PLPMUAgent log];
-[PLPMUAgent batteryLevelChanged];
-[PLPMUAgent logEventPointSensors];
```
