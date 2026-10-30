# `_SBBatteryLogContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _hasChargedPartially;
i _capacity;
i _voltage;
@"NSArray" _foregroundApplications;
@"NSArray" _screenBrightnessDescriptions;
@"NSString" _hingeStateDescription;
d _usageTimeInSeconds;
d _standbyTimeInSeconds;
```

## Properties

```
@property (T@"NSArray",&,N,V_foregroundApplications) foregroundApplications;
@property (T@"NSArray",&,N,V_screenBrightnessDescriptions) screenBrightnessDescriptions;
@property (T@"NSString",C,N,V_hingeStateDescription) hingeStateDescription;
@property (Ti,N,V_capacity) capacity;
@property (Ti,N,V_voltage) voltage;
@property (Td,N,V_usageTimeInSeconds) usageTimeInSeconds;
@property (Td,N,V_standbyTimeInSeconds) standbyTimeInSeconds;
@property (TB,N,V_hasChargedPartially) hasChargedPartially;
```

## Instance methods

```
-[_SBBatteryLogContext setCapacity:];
-[_SBBatteryLogContext capacity];
-[_SBBatteryLogContext voltage];
-[_SBBatteryLogContext foregroundApplications];
-[_SBBatteryLogContext hasChargedPartially];
-[_SBBatteryLogContext hingeStateDescription];
-[_SBBatteryLogContext screenBrightnessDescriptions];
-[_SBBatteryLogContext setForegroundApplications:];
-[_SBBatteryLogContext setHasChargedPartially:];
-[_SBBatteryLogContext setHingeStateDescription:];
-[_SBBatteryLogContext setScreenBrightnessDescriptions:];
-[_SBBatteryLogContext setStandbyTimeInSeconds:];
-[_SBBatteryLogContext setUsageTimeInSeconds:];
-[_SBBatteryLogContext setVoltage:];
-[_SBBatteryLogContext standbyTimeInSeconds];
-[_SBBatteryLogContext usageTimeInSeconds];
```
