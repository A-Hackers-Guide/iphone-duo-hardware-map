# `SNWiFiRecordInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
q rssi;
q snr;
q cca;
? channelInfo;
? phyMode;
B isCaptive;
? timestamp;
```

## Properties

```
@property (Tq,N,R,Vrssi) rssi;
@property (Tq,N,R,Vsnr) snr;
@property (Tq,N,R,Vcca) cca;
@property (T@"NSString",N,R) channelInfo;
@property (T@"NSString",N,R) phyMode;
@property (TB,N,R,VisCaptive) isCaptive;
@property (T@"NSDate",N,R) timestamp;
```

## Instance methods

```
-[SNWiFiRecordInternal rssi];
-[SNWiFiRecordInternal cca];
-[SNWiFiRecordInternal snr];
-[SNWiFiRecordInternal channelInfo];
-[SNWiFiRecordInternal init];
-[SNWiFiRecordInternal phyMode];
-[SNWiFiRecordInternal timestamp];
-[SNWiFiRecordInternal isCaptive];
-[SNWiFiRecordInternal initWithRssi:snr:cca:channelInfo:phyMode:isCaptive:timestamp:];
```
