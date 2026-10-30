# `WiFiAwareState`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 15 instance variables, 15 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"WiFiAwareInterfaceInfo" _interfaceInfo;
B _isFWElection;
Q _nanRole;
q _hopCount;
@"WiFiMACAddress" _clusterId;
q _selfRankM;
q _selfRankR;
@"WiFiMACAddress" _immediateMaster;
q _immediateMasterRankM;
q _immediateMasterRankR;
@"WiFiMACAddress" _anchorMaster;
q _anchorMasterRankM;
q _anchorMasterRankR;
q _ambtt;
Q _tsf;
```

## Properties

```
@property (T@"WiFiAwareInterfaceInfo",R,N) interfaceInfo;
@property (TB,R,N,V_isFWElection) isFWElection;
@property (TQ,R,N,V_nanRole) nanRole;
@property (Tq,R,N,V_hopCount) hopCount;
@property (T@"WiFiMACAddress",R,N,V_clusterId) clusterId;
@property (Tq,R,N,V_selfRankM) selfRankM;
@property (Tq,R,N,V_selfRankR) selfRankR;
@property (T@"WiFiMACAddress",R,N,V_immediateMaster) immediateMaster;
@property (Tq,R,N,V_immediateMasterRankM) immediateMasterRankM;
@property (Tq,R,N,V_immediateMasterRankR) immediateMasterRankR;
@property (T@"WiFiMACAddress",R,N,V_anchorMaster) anchorMaster;
@property (Tq,R,N,V_anchorMasterRankM) anchorMasterRankM;
@property (Tq,R,N,V_anchorMasterRankR) anchorMasterRankR;
@property (Tq,R,N,V_ambtt) ambtt;
@property (TQ,R,N,V_tsf) tsf;
```

## Class methods

```
+[WiFiAwareState supportsSecureCoding];
+[WiFiAwareState currentState];
```

## Instance methods

```
-[WiFiAwareState initInternal];
-[WiFiAwareState interfaceName];
-[WiFiAwareState isEnabled];
-[WiFiAwareState encodeWithCoder:];
-[WiFiAwareState description];
-[WiFiAwareState initWithCoder:];
-[WiFiAwareState copyWithZone:];
-[WiFiAwareState clusterId];
-[WiFiAwareState nanRole];
-[WiFiAwareState tsf];
-[WiFiAwareState immediateMaster];
-[WiFiAwareState ambtt];
-[WiFiAwareState anchorMaster];
-[WiFiAwareState anchorMasterRankM];
-[WiFiAwareState anchorMasterRankR];
-[WiFiAwareState descriptionWithChangedOptions:];
-[WiFiAwareState descriptionWithChangedOptions:forceAllChangedOptions:];
-[WiFiAwareState hopCount];
-[WiFiAwareState immediateMasterRankM];
-[WiFiAwareState immediateMasterRankR];
-[WiFiAwareState initWithInterfaceInfo:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:];
-[WiFiAwareState interfaceAddr];
-[WiFiAwareState interfaceInfo];
-[WiFiAwareState isFWElection];
-[WiFiAwareState selfRankM];
-[WiFiAwareState selfRankR];
```
