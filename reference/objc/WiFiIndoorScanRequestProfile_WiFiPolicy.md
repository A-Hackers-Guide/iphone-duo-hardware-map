# `WiFiIndoorScanRequestProfile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiScanRequestProfile`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _isCurrentlyInHalfDutyCycle;
I _numFullDutyCycleScans;
@"NSDate" _lastScanTime;
```

## Properties

```
@property (T@"NSDate",&,N,V_lastScanTime) lastScanTime;
@property (TI,N,V_numFullDutyCycleScans) numFullDutyCycleScans;
@property (TB,N,V_isCurrentlyInHalfDutyCycle) isCurrentlyInHalfDutyCycle;
```

## Instance methods

```
-[WiFiIndoorScanRequestProfile handleScanRequest:andResult:];
-[WiFiIndoorScanRequestProfile lastScanTime];
-[WiFiIndoorScanRequestProfile initWithSoftError:];
-[WiFiIndoorScanRequestProfile setLastScanTime:];
-[WiFiIndoorScanRequestProfile isCurrentlyInHalfDutyCycle];
-[WiFiIndoorScanRequestProfile numFullDutyCycleScans];
-[WiFiIndoorScanRequestProfile setIsCurrentlyInHalfDutyCycle:];
-[WiFiIndoorScanRequestProfile setNumFullDutyCycleScans:];
```
