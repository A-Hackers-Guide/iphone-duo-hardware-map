# `WFLinkQuality`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
f _scaledRssi;
@"NSString" _ssid;
q _rssi;
```

## Properties

```
@property (T@"NSString",C,N,V_ssid) ssid;
@property (Tq,N,V_rssi) rssi;
@property (Tf,N,V_scaledRssi) scaledRssi;
```

## Instance methods

```
-[WFLinkQuality rssi];
-[WFLinkQuality ssid];
-[WFLinkQuality setSsid:];
-[WFLinkQuality init];
-[WFLinkQuality setRssi:];
-[WFLinkQuality description];
-[WFLinkQuality copyWithZone:];
-[WFLinkQuality isEqual:];
-[WFLinkQuality initWithSSID:rssi:scaledRSSI:];
-[WFLinkQuality scaledRssi];
-[WFLinkQuality setScaledRssi:];
```
