# `WiFiP2PAWDLState`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 10 properties, 16 instance methods, 2 class methods

## Instance variables

```
B _supportsSoloMode;
B _supportsDataTransfer;
B _isEnabled;
I _substate;
@"NSString" _interfaceName;
@"NSArray" _channelSequence;
@"WiFiMACAddress" _macAddress;
@"WiFiChannel" _peerMasterChannel;
@"WiFiChannel" _peerPrimaryPreferredChannel;
@"WiFiChannel" _peerSecondaryPreferredChannel;
```

## Properties

```
@property (T@"NSString",R,N,V_interfaceName) interfaceName;
@property (TB,R,N,V_supportsSoloMode) supportsSoloMode;
@property (TB,R,N,V_supportsDataTransfer) supportsDataTransfer;
@property (T@"NSArray",R,N,V_channelSequence) channelSequence;
@property (TB,R,N,V_isEnabled) isEnabled;
@property (TI,R,N,V_substate) substate;
@property (T@"WiFiMACAddress",R,N,V_macAddress) macAddress;
@property (T@"WiFiChannel",R,N,V_peerMasterChannel) peerMasterChannel;
@property (T@"WiFiChannel",R,N,V_peerPrimaryPreferredChannel) peerPrimaryPreferredChannel;
@property (T@"WiFiChannel",R,N,V_peerSecondaryPreferredChannel) peerSecondaryPreferredChannel;
```

## Class methods

```
+[WiFiP2PAWDLState supportsSecureCoding];
+[WiFiP2PAWDLState currentState];
```

## Instance methods

```
-[WiFiP2PAWDLState macAddress];
-[WiFiP2PAWDLState substate];
-[WiFiP2PAWDLState supportsSoloMode];
-[WiFiP2PAWDLState channelSequence];
-[WiFiP2PAWDLState interfaceName];
-[WiFiP2PAWDLState isEnabled];
-[WiFiP2PAWDLState supportsDataTransfer];
-[WiFiP2PAWDLState peerMasterChannel];
-[WiFiP2PAWDLState encodeWithCoder:];
-[WiFiP2PAWDLState description];
-[WiFiP2PAWDLState initWithCoder:];
-[WiFiP2PAWDLState peerSecondaryPreferredChannel];
-[WiFiP2PAWDLState copyWithZone:];
-[WiFiP2PAWDLState isEqual:];
-[WiFiP2PAWDLState initWithInterfaceName:supportsSoloMode:supportsDataTransfer:channelSequence:isEnabled:substate:macAddress:peerMasterChannel:peerPrimaryPreferredChannel:peerSecondaryPreferredChannel:];
-[WiFiP2PAWDLState peerPrimaryPreferredChannel];
```
