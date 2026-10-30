# `WADeviceAnalytics_InsideOutsideClassifierParameters`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
s _bestBand;
s _rssiThreshold;
s _insideCount;
s _outsideCount;
f _tpr;
f _fpr;
@"NSString" _ssid;
```

## Properties

```
@property (T@"NSString",&,N,V_ssid) ssid;
@property (Ts,N,V_bestBand) bestBand;
@property (Ts,N,V_rssiThreshold) rssiThreshold;
@property (Tf,N,V_tpr) tpr;
@property (Tf,N,V_fpr) fpr;
@property (Ts,N,V_insideCount) insideCount;
@property (Ts,N,V_outsideCount) outsideCount;
```

## Instance methods

```
-[WADeviceAnalytics_InsideOutsideClassifierParameters setRssiThreshold:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters ssid];
-[WADeviceAnalytics_InsideOutsideClassifierParameters setSsid:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters rssiThreshold];
-[WADeviceAnalytics_InsideOutsideClassifierParameters initWithNetwork:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters description];
-[WADeviceAnalytics_InsideOutsideClassifierParameters fpr];
-[WADeviceAnalytics_InsideOutsideClassifierParameters setFpr:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters setInsideCount:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters setTpr:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters tpr];
-[WADeviceAnalytics_InsideOutsideClassifierParameters bestBand];
-[WADeviceAnalytics_InsideOutsideClassifierParameters insideCount];
-[WADeviceAnalytics_InsideOutsideClassifierParameters outsideCount];
-[WADeviceAnalytics_InsideOutsideClassifierParameters setBestBand:];
-[WADeviceAnalytics_InsideOutsideClassifierParameters setOutsideCount:];
```
