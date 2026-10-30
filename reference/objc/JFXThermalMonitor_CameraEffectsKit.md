# `JFXThermalMonitor`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 7 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _hasGoneAboveNominal;
i _currentThermalLevel;
i _highestThermalLevel;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TB,N,V_hasGoneAboveNominal) hasGoneAboveNominal;
@property (Ti,N,V_currentThermalLevel) currentThermalLevel;
@property (Ti,N,V_highestThermalLevel) highestThermalLevel;
@property (TB,R,N) thermalLevelExceededNominal;
@property (Ti,R,N) thermalLevel;
@property (Ti,R,N) highestThermalLevelReached;
```

## Class methods

```
+[JFXThermalMonitor sharedInstance];
+[JFXThermalMonitor stringFromThermalPressureLevel:];
+[JFXThermalMonitor enumerateThermalPressureLevel:];
```

## Instance methods

```
-[JFXThermalMonitor _postNotification:];
-[JFXThermalMonitor init];
-[JFXThermalMonitor setCurrentThermalLevel:];
-[JFXThermalMonitor queue];
-[JFXThermalMonitor currentThermalLevel];
-[JFXThermalMonitor thermalLevel];
-[JFXThermalMonitor setQueue:];
-[JFXThermalMonitor _analyticValueForThermalLevelBefore:after:];
-[JFXThermalMonitor _disabledThermalTracking];
-[JFXThermalMonitor _updateThermalLevelsWithToken:];
-[JFXThermalMonitor hasGoneAboveNominal];
-[JFXThermalMonitor highestThermalLevel];
-[JFXThermalMonitor highestThermalLevelReached];
-[JFXThermalMonitor setHasGoneAboveNominal:];
-[JFXThermalMonitor setHighestThermalLevel:];
-[JFXThermalMonitor thermalLevelExceededNominal];
-[JFXThermalMonitor thermalLevelLabel];
```
