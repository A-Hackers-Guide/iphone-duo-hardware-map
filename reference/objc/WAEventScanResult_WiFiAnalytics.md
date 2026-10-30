# `WAEventScanResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"resultBand"s"resultChannel"s"resultRssi"s} _data;
@"NSString" _resultBssid;
@"NSString" _resultSsid;
```

## Properties

```
@property (T@"NSString",C,N,V_resultBssid) resultBssid;
@property (T@"NSString",C,N,V_resultSsid) resultSsid;
```

## Instance methods

```
-[WAEventScanResult processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventScanResult updateRecord:];
-[WAEventScanResult data];
-[WAEventScanResult description];
-[WAEventScanResult setResultBssid:];
-[WAEventScanResult initWithBssid:resultBssid:resultSsid:at:data:withLqmHistory:withError:];
-[WAEventScanResult resultBssid];
-[WAEventScanResult resultSsid];
-[WAEventScanResult setResultSsid:];
```
