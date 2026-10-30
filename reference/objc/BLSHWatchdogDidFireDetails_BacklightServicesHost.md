# `BLSHWatchdogDidFireDetails`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _debugLogsEnabled;
@"NSDate" _date;
@"NSString" _buildVersion;
@"NSString" _device;
@"NSString" _explanation;
@"NSString" _abortReasonString;
```

## Properties

```
@property (T@"NSDate",&,N,V_date) date;
@property (T@"NSString",C,N,V_buildVersion) buildVersion;
@property (T@"NSString",C,N,V_device) device;
@property (T@"NSString",C,N,V_explanation) explanation;
@property (T@"NSString",C,N,V_abortReasonString) abortReasonString;
@property (TB,N,V_debugLogsEnabled) debugLogsEnabled;
```

## Instance methods

```
-[BLSHWatchdogDidFireDetails buildVersion];
-[BLSHWatchdogDidFireDetails setDevice:];
-[BLSHWatchdogDidFireDetails setExplanation:];
-[BLSHWatchdogDidFireDetails setDate:];
-[BLSHWatchdogDidFireDetails device];
-[BLSHWatchdogDidFireDetails explanation];
-[BLSHWatchdogDidFireDetails date];
-[BLSHWatchdogDidFireDetails debugLogsEnabled];
-[BLSHWatchdogDidFireDetails setBuildVersion:];
-[BLSHWatchdogDidFireDetails abortReasonString];
-[BLSHWatchdogDidFireDetails initWithWatchdogDidFireDictionary:];
-[BLSHWatchdogDidFireDetails setAbortReasonString:];
-[BLSHWatchdogDidFireDetails setDebugLogsEnabled:];
```
