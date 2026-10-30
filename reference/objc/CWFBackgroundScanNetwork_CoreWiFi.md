# `CWFBackgroundScanNetwork`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 8 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _entry;
B _exit;
@"NSString" _BSSID;
@"CWFChannel" _channel;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",C,N,V_BSSID) BSSID;
@property (TB,N,V_entry) entry;
@property (TB,N,V_exit) exit;
@property (T@"CWFChannel",C,N,V_channel) channel;
```

## Class methods

```
+[CWFBackgroundScanNetwork supportsSecureCoding];
```

## Instance methods

```
-[CWFBackgroundScanNetwork setChannel:];
-[CWFBackgroundScanNetwork channel];
-[CWFBackgroundScanNetwork BSSID];
-[CWFBackgroundScanNetwork JSONCompatibleKeyValueMap];
-[CWFBackgroundScanNetwork setBSSID:];
-[CWFBackgroundScanNetwork exit];
-[CWFBackgroundScanNetwork encodeWithCoder:];
-[CWFBackgroundScanNetwork hash];
-[CWFBackgroundScanNetwork description];
-[CWFBackgroundScanNetwork initWithCoder:];
-[CWFBackgroundScanNetwork entry];
-[CWFBackgroundScanNetwork copyWithZone:];
-[CWFBackgroundScanNetwork isEqual:];
-[CWFBackgroundScanNetwork setEntry:];
-[CWFBackgroundScanNetwork setExit:];
-[CWFBackgroundScanNetwork isEqualToBackgroundScanNetwork:];
```
