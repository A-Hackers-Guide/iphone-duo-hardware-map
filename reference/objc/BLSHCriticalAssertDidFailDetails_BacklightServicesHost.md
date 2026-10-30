# `BLSHCriticalAssertDidFailDetails`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _debugLogsEnabled;
B _radarIsUserInitiated;
@"NSDate" _date;
@"NSString" _buildVersion;
@"NSString" _device;
@"NSString" _explanation;
@"NSString" _processName;
Q _failureSource;
```

## Properties

```
@property (T@"NSDate",&,N,V_date) date;
@property (T@"NSString",C,N,V_buildVersion) buildVersion;
@property (T@"NSString",C,N,V_device) device;
@property (T@"NSString",C,N,V_explanation) explanation;
@property (T@"NSString",C,N,V_processName) processName;
@property (TB,N,V_debugLogsEnabled) debugLogsEnabled;
@property (TB,N,V_radarIsUserInitiated) radarIsUserInitiated;
@property (TQ,N,V_failureSource) failureSource;
```

## Instance methods

```
-[BLSHCriticalAssertDidFailDetails setProcessName:];
-[BLSHCriticalAssertDidFailDetails buildVersion];
-[BLSHCriticalAssertDidFailDetails setDevice:];
-[BLSHCriticalAssertDidFailDetails setExplanation:];
-[BLSHCriticalAssertDidFailDetails setDate:];
-[BLSHCriticalAssertDidFailDetails device];
-[BLSHCriticalAssertDidFailDetails explanation];
-[BLSHCriticalAssertDidFailDetails date];
-[BLSHCriticalAssertDidFailDetails processName];
-[BLSHCriticalAssertDidFailDetails debugLogsEnabled];
-[BLSHCriticalAssertDidFailDetails setBuildVersion:];
-[BLSHCriticalAssertDidFailDetails failureSource];
-[BLSHCriticalAssertDidFailDetails initWithCriticalAssertDidFailDictionary:];
-[BLSHCriticalAssertDidFailDetails radarIsUserInitiated];
-[BLSHCriticalAssertDidFailDetails setDebugLogsEnabled:];
-[BLSHCriticalAssertDidFailDetails setFailureSource:];
-[BLSHCriticalAssertDidFailDetails setRadarIsUserInitiated:];
```
