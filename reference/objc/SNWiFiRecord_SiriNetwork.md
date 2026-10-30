# `SNWiFiRecord`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isCaptive;
q _rssi;
q _snr;
q _cca;
@"NSString" _channelInfo;
@"NSString" _phyMode;
@"NSDate" _timestamp;
```

## Properties

```
@property (Tq,N,V_rssi) rssi;
@property (Tq,N,V_snr) snr;
@property (Tq,N,V_cca) cca;
@property (T@"NSString",C,N,V_channelInfo) channelInfo;
@property (T@"NSString",C,N,V_phyMode) phyMode;
@property (TB,N,V_isCaptive) isCaptive;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
```

## Instance methods

```
-[SNWiFiRecord rssi];
-[SNWiFiRecord cca];
-[SNWiFiRecord setSnr:];
-[SNWiFiRecord snr];
-[SNWiFiRecord channelInfo];
-[SNWiFiRecord setTimestamp:];
-[SNWiFiRecord phyMode];
-[SNWiFiRecord setCca:];
-[SNWiFiRecord timestamp];
-[SNWiFiRecord setRssi:];
-[SNWiFiRecord setIsCaptive:];
-[SNWiFiRecord setChannelInfo:];
-[SNWiFiRecord isCaptive];
-[SNWiFiRecord setPhyMode:];
```
