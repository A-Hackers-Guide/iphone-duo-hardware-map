# `CWFSensingParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 6 instance variables, 10 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _highPriority;
S _beaconInterval;
i _matchFrameType;
i _channelNumber;
I _band;
@"NSString" _matchMACAddress;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,N,V_matchFrameType) matchFrameType;
@property (T@"NSString",C,N,V_matchMACAddress) matchMACAddress;
@property (Ti,N,V_channelNumber) channelNumber;
@property (TI,N,V_band) band;
@property (TS,N,V_beaconInterval) beaconInterval;
@property (TB,N,V_highPriority) highPriority;
```

## Class methods

```
+[CWFSensingParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFSensingParameters setHighPriority:];
-[CWFSensingParameters JSONCompatibleKeyValueMap];
-[CWFSensingParameters highPriority];
-[CWFSensingParameters init];
-[CWFSensingParameters band];
-[CWFSensingParameters setChannelNumber:];
-[CWFSensingParameters setBand:];
-[CWFSensingParameters encodeWithCoder:];
-[CWFSensingParameters hash];
-[CWFSensingParameters description];
-[CWFSensingParameters initWithCoder:];
-[CWFSensingParameters copyWithZone:];
-[CWFSensingParameters isEqual:];
-[CWFSensingParameters channelNumber];
-[CWFSensingParameters beaconInterval];
-[CWFSensingParameters setBeaconInterval:];
-[CWFSensingParameters convertToDriverStructure:error:];
-[CWFSensingParameters matchMACAddress];
-[CWFSensingParameters convertToDriverAPParams:error:];
-[CWFSensingParameters isEqualToSensingParameters:];
-[CWFSensingParameters matchFrameType];
-[CWFSensingParameters setMatchFrameType:];
-[CWFSensingParameters setMatchMACAddress:];
```
