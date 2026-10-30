# `CBPeer`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _isLinkEncrypted;
C _connectedTransport;
@"NSUUID" _identifier;
Q _mtuLength;
q _pairingState;
q _hostState;
q _role;
@"CBManager" _manager;
```

## Properties

```
@property (TQ,N,V_mtuLength) mtuLength;
@property (Tq,N,V_pairingState) pairingState;
@property (Tq,N,V_hostState) hostState;
@property (TB,N,V_isLinkEncrypted) isLinkEncrypted;
@property (Tq,N,V_role) role;
@property (T@"CBManager",W,N,V_manager) manager;
@property (TC,N,V_connectedTransport) connectedTransport;
@property (T@"NSUUID",R,N,V_identifier) identifier;
```

## Instance methods

```
-[CBPeer handleMsg:args:];
-[CBPeer hasTag:];
-[CBPeer identifier];
-[CBPeer setHostState:];
-[CBPeer setManager:];
-[CBPeer manager];
-[CBPeer handleHostStateUpdated:];
-[CBPeer role];
-[CBPeer hash];
-[CBPeer setRole:];
-[CBPeer copyWithZone:];
-[CBPeer hostState];
-[CBPeer pairingState];
-[CBPeer setPairingState:];
-[CBPeer customProperty:];
-[CBPeer getTags];
-[CBPeer customPropertyNames];
-[CBPeer setCustomProperty:value:];
-[CBPeer tag:];
-[CBPeer untag:];
-[CBPeer addTags:];
-[CBPeer isLinkEncrypted];
-[CBPeer connectedTransport];
-[CBPeer handleLinkEncryptionChanged:];
-[CBPeer handleMTUChanged:];
-[CBPeer initWithInfo:manager:];
-[CBPeer mtuLength];
-[CBPeer peerStateToString:];
-[CBPeer removeTags:];
-[CBPeer sendInternalMsg:args:];
-[CBPeer sendInternalSyncMsg:args:];
-[CBPeer setConnectedTransport:];
-[CBPeer setIsLinkEncrypted:];
-[CBPeer setMtuLength:];
```
