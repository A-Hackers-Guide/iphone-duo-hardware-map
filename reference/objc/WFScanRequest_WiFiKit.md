# `WFScanRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 26 instance methods, 2 class methods

## Instance variables

```
B _applyRssiThresholdFilter;
B _includeBSSList;
B _lowPriorityScan;
B _channelListIncludesTwoFour;
@"NSString" _ssid;
Q _dwellTime;
@"NSArray" _channels;
q _rssiThreshold;
@"NSUUID" _UUID;
```

## Properties

```
@property (T@"NSString",C,N,V_ssid) ssid;
@property (T@"NSArray",&,N,V_channels) channels;
@property (Tq,N,V_rssiThreshold) rssiThreshold;
@property (TB,N,V_channelListIncludesTwoFour) channelListIncludesTwoFour;
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (TB,V_applyRssiThresholdFilter) applyRssiThresholdFilter;
@property (TQ,V_dwellTime) dwellTime;
@property (TB,V_includeBSSList) includeBSSList;
@property (TB,V_lowPriorityScan) lowPriorityScan;
```

## Class methods

```
+[WFScanRequest scanRequestForChannels:];
+[WFScanRequest scanRequestForSSID:channels:];
```

## Instance methods

```
-[WFScanRequest setRssiThreshold:];
-[WFScanRequest ssid];
-[WFScanRequest setSsid:];
-[WFScanRequest channels];
-[WFScanRequest rssiThreshold];
-[WFScanRequest dwellTime];
-[WFScanRequest setDwellTime:];
-[WFScanRequest init];
-[WFScanRequest setUUID:];
-[WFScanRequest UUID];
-[WFScanRequest setChannels:];
-[WFScanRequest description];
-[WFScanRequest lowPriorityScan];
-[WFScanRequest cScanParameters];
-[WFScanRequest _channelListFromArrayOfChannels:];
-[WFScanRequest _channelListIncludesTwoFour:];
-[WFScanRequest _defaultScanDictionary];
-[WFScanRequest applyRssiThresholdFilter];
-[WFScanRequest channelListIncludesTwoFour];
-[WFScanRequest includeBSSList];
-[WFScanRequest initWithSSID:channels:];
-[WFScanRequest scanParameters];
-[WFScanRequest setApplyRssiThresholdFilter:];
-[WFScanRequest setChannelListIncludesTwoFour:];
-[WFScanRequest setIncludeBSSList:];
-[WFScanRequest setLowPriorityScan:];
```
