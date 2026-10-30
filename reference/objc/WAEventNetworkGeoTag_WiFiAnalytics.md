# `WAEventNetworkGeoTag`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"latitude"d"longitude"d} _data;
@"NSString" _ssid;
@"NSMutableSet" _expiredGeotags;
```

## Properties

```
@property (T@"NSString",&,N,V_ssid) ssid;
@property (T@"NSMutableSet",&,N,V_expiredGeotags) expiredGeotags;
```

## Instance methods

```
-[WAEventNetworkGeoTag processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventNetworkGeoTag ssid];
-[WAEventNetworkGeoTag setSsid:];
-[WAEventNetworkGeoTag data];
-[WAEventNetworkGeoTag _updateRecord:];
-[WAEventNetworkGeoTag description];
-[WAEventNetworkGeoTag expiredGeotags];
-[WAEventNetworkGeoTag findReusableGeoTagFor:];
-[WAEventNetworkGeoTag initWithBssid:ssid:at:data:withError:];
-[WAEventNetworkGeoTag setExpiredGeotags:];
```
