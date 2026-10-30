# `WAEventLeave`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 1 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"isInVol"B"associationDuration"d} _data;
```

## Class methods

```
+[WAEventLeave leaveReasonAsString:];
```

## Instance methods

```
-[WAEventLeave processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventLeave updateRecord:];
-[WAEventLeave data];
-[WAEventLeave description];
-[WAEventLeave initWithBssid:ssid:at:data:withLqmHistory:withError:];
```
