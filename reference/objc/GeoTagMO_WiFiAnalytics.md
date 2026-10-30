# `GeoTagMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 5 properties, 0 instance methods, 7 class methods

## Properties

```
@property (T@"NSDate",C,D,N) date;
@property (Td,D,N) latitude;
@property (Td,D,N) longitude;
@property (Ti,D,N) taggedCount;
@property (T@"BSSMO",&,D,N) bss;
```

## Class methods

```
+[GeoTagMO fetchRequest];
+[GeoTagMO entityName];
+[GeoTagMO generateInstance:];
+[GeoTagMO geoTagsAtLocation:withinDistance:inBand:container:];
+[GeoTagMO geoTagsForNetwork:container:];
+[GeoTagMO geoTagsInBand:ssid:moc:];
+[GeoTagMO isNetworkWithinRangeOfLocation:range:location:container:count:];
```
