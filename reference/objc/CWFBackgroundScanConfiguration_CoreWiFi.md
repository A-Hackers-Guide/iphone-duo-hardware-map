# `CWFBackgroundScanConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 7 instance variables, 11 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _cacheEnabled;
B _cacheRollover;
{?="channels"b1"networks"b1"cacheEnabled"b1"cacheRollover"b1"scanFrequency"b1"lostNetworkScanCount"b1} _modifyMap;
@"NSArray" _networks;
@"NSArray" _channels;
Q _scanFrequency;
Q _lostNetworkScanCount;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{?=b1b1b1b1b1b1},N,V_modifyMap) modifyMap;
@property (T@"NSArray",C,N,V_networks) networks;
@property (T@"NSArray",C,N,V_channels) channels;
@property (TB,N,V_cacheEnabled) cacheEnabled;
@property (TB,N,V_cacheRollover) cacheRollover;
@property (TQ,N,V_scanFrequency) scanFrequency;
@property (TQ,N,V_lostNetworkScanCount) lostNetworkScanCount;
```

## Class methods

```
+[CWFBackgroundScanConfiguration supportsSecureCoding];
```

## Instance methods

```
-[CWFBackgroundScanConfiguration channels];
-[CWFBackgroundScanConfiguration modified];
-[CWFBackgroundScanConfiguration setNetworks:];
-[CWFBackgroundScanConfiguration JSONCompatibleKeyValueMap];
-[CWFBackgroundScanConfiguration networks];
-[CWFBackgroundScanConfiguration setChannels:];
-[CWFBackgroundScanConfiguration encodeWithCoder:];
-[CWFBackgroundScanConfiguration hash];
-[CWFBackgroundScanConfiguration description];
-[CWFBackgroundScanConfiguration initWithCoder:];
-[CWFBackgroundScanConfiguration copyWithZone:];
-[CWFBackgroundScanConfiguration isEqual:];
-[CWFBackgroundScanConfiguration merge:];
-[CWFBackgroundScanConfiguration cacheEnabled];
-[CWFBackgroundScanConfiguration cacheRollover];
-[CWFBackgroundScanConfiguration isEqualToBackgroundScanConfiguration:];
-[CWFBackgroundScanConfiguration lostNetworkScanCount];
-[CWFBackgroundScanConfiguration modifyMap];
-[CWFBackgroundScanConfiguration scanFrequency];
-[CWFBackgroundScanConfiguration setCacheEnabled:];
-[CWFBackgroundScanConfiguration setCacheRollover:];
-[CWFBackgroundScanConfiguration setLostNetworkScanCount:];
-[CWFBackgroundScanConfiguration setModifyMap:];
-[CWFBackgroundScanConfiguration setScanFrequency:];
```
