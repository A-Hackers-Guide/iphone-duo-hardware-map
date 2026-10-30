# `CWFAWDLPeerAssistedDiscoveryParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 12 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _followMode;
i _peerSupportedChannelFlags;
Q _localMasterChannel;
Q _localPreferredChannel;
Q _localSecondaryPreferredChannel;
Q _localAssistedDiscoveryMetric;
@"NSString" _peerMACAddress;
Q _peerMasterChannel;
Q _peerPreferredChannel;
Q _peerSecondaryPreferredChannel;
Q _peerAssistedDiscoveryMetric;
Q _followModePreferredBand;
```

## Properties

```
@property (TQ,N,V_localMasterChannel) localMasterChannel;
@property (TQ,N,V_localPreferredChannel) localPreferredChannel;
@property (TQ,N,V_localSecondaryPreferredChannel) localSecondaryPreferredChannel;
@property (TQ,N,V_localAssistedDiscoveryMetric) localAssistedDiscoveryMetric;
@property (T@"NSString",C,N,V_peerMACAddress) peerMACAddress;
@property (TQ,N,V_peerMasterChannel) peerMasterChannel;
@property (TQ,N,V_peerPreferredChannel) peerPreferredChannel;
@property (TQ,N,V_peerSecondaryPreferredChannel) peerSecondaryPreferredChannel;
@property (TQ,N,V_peerAssistedDiscoveryMetric) peerAssistedDiscoveryMetric;
@property (Ti,N,V_peerSupportedChannelFlags) peerSupportedChannelFlags;
@property (TB,N,V_followMode) followMode;
@property (TQ,N,V_followModePreferredBand) followModePreferredBand;
```

## Class methods

```
+[CWFAWDLPeerAssistedDiscoveryParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFAWDLPeerAssistedDiscoveryParameters peerMasterChannel];
-[CWFAWDLPeerAssistedDiscoveryParameters encodeWithCoder:];
-[CWFAWDLPeerAssistedDiscoveryParameters hash];
-[CWFAWDLPeerAssistedDiscoveryParameters description];
-[CWFAWDLPeerAssistedDiscoveryParameters initWithCoder:];
-[CWFAWDLPeerAssistedDiscoveryParameters peerSecondaryPreferredChannel];
-[CWFAWDLPeerAssistedDiscoveryParameters copyWithZone:];
-[CWFAWDLPeerAssistedDiscoveryParameters isEqual:];
-[CWFAWDLPeerAssistedDiscoveryParameters setPeerAssistedDiscoveryMetric:];
-[CWFAWDLPeerAssistedDiscoveryParameters followMode];
-[CWFAWDLPeerAssistedDiscoveryParameters followModePreferredBand];
-[CWFAWDLPeerAssistedDiscoveryParameters isEqualToAWDLParameters:];
-[CWFAWDLPeerAssistedDiscoveryParameters localAssistedDiscoveryMetric];
-[CWFAWDLPeerAssistedDiscoveryParameters localMasterChannel];
-[CWFAWDLPeerAssistedDiscoveryParameters localPreferredChannel];
-[CWFAWDLPeerAssistedDiscoveryParameters localSecondaryPreferredChannel];
-[CWFAWDLPeerAssistedDiscoveryParameters peerAssistedDiscoveryMetric];
-[CWFAWDLPeerAssistedDiscoveryParameters peerMACAddress];
-[CWFAWDLPeerAssistedDiscoveryParameters peerPreferredChannel];
-[CWFAWDLPeerAssistedDiscoveryParameters peerSupportedChannelFlags];
-[CWFAWDLPeerAssistedDiscoveryParameters setFollowMode:];
-[CWFAWDLPeerAssistedDiscoveryParameters setFollowModePreferredBand:];
-[CWFAWDLPeerAssistedDiscoveryParameters setLocalAssistedDiscoveryMetric:];
-[CWFAWDLPeerAssistedDiscoveryParameters setLocalMasterChannel:];
-[CWFAWDLPeerAssistedDiscoveryParameters setLocalPreferredChannel:];
-[CWFAWDLPeerAssistedDiscoveryParameters setLocalSecondaryPreferredChannel:];
-[CWFAWDLPeerAssistedDiscoveryParameters setPeerMACAddress:];
-[CWFAWDLPeerAssistedDiscoveryParameters setPeerMasterChannel:];
-[CWFAWDLPeerAssistedDiscoveryParameters setPeerPreferredChannel:];
-[CWFAWDLPeerAssistedDiscoveryParameters setPeerSecondaryPreferredChannel:];
-[CWFAWDLPeerAssistedDiscoveryParameters setPeerSupportedChannelFlags:];
```
