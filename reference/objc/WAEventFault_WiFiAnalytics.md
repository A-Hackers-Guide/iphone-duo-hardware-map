# `WAEventFault`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i} _data;
@"NSString" _interface;
@"NSString" _type;
```

## Properties

```
@property (T@"NSString",&,V_interface) interface;
@property (T@"NSString",&,V_type) type;
```

## Instance methods

```
-[WAEventFault processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventFault updateRecord:];
-[WAEventFault data];
-[WAEventFault setInterface:];
-[WAEventFault interface];
-[WAEventFault setType:];
-[WAEventFault type];
-[WAEventFault description];
-[WAEventFault initWithBssid:interface:type:at:data:withLqmHistory:withError:];
```
