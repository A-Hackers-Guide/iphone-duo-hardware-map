# `WADeviceAnalyticsNetwork`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
B _isHome;
@"NSString" _ssid;
@"NSSet" _lans;
@"NSDictionary" _bssidsAndLans;
```

## Properties

```
@property (T@"NSString",R,V_ssid) ssid;
@property (TB,R,V_isHome) isHome;
@property (T@"NSSet",R,V_lans) lans;
@property (T@"NSDictionary",R,V_bssidsAndLans) bssidsAndLans;
```

## Class methods

```
+[WADeviceAnalyticsNetwork networkWith:];
```

## Instance methods

```
-[WADeviceAnalyticsNetwork ssid];
-[WADeviceAnalyticsNetwork initWith:];
-[WADeviceAnalyticsNetwork description];
-[WADeviceAnalyticsNetwork isHome];
-[WADeviceAnalyticsNetwork bssidsAndLans];
-[WADeviceAnalyticsNetwork lans];
```
