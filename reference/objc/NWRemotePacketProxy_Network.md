# `NWRemotePacketProxy`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
I _receiveWindowPacketCount;
@"NSObject<NWRemotePacketProxyDelegate>" _delegate;
@"NSMutableArray" _writeRequests;
^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v} _packetProtocol;
^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v} _defaultOutputHandler;
^{nw_hash_table=} _packetHashTable;
```

## Properties

```
@property (T@"NSObject<NWRemotePacketProxyDelegate>",W,V_delegate) delegate;
@property (T@"NSMutableArray",&,V_writeRequests) writeRequests;
@property (T^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v},V_packetProtocol) packetProtocol;
@property (T^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v},V_defaultOutputHandler) defaultOutputHandler;
@property (T^{nw_hash_table=},V_packetHashTable) packetHashTable;
@property (T^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v},R,N) protocol;
@property (TI,N,V_receiveWindowPacketCount) receiveWindowPacketCount;
```

## Instance methods

```
-[NWRemotePacketProxy protocol];
-[NWRemotePacketProxy initWithDelegate:];
-[NWRemotePacketProxy dealloc];
-[NWRemotePacketProxy setDelegate:];
-[NWRemotePacketProxy delegate];
-[NWRemotePacketProxy outputHandlerForPacket:inbound:];
-[NWRemotePacketProxy packetHashTable];
-[NWRemotePacketProxy defaultOutputHandler];
-[NWRemotePacketProxy packetProtocol];
-[NWRemotePacketProxy receiveRemotePacket:];
-[NWRemotePacketProxy receiveWindowPacketCount];
-[NWRemotePacketProxy setDefaultOutputHandler:];
-[NWRemotePacketProxy setDefaultOutputProtocolHandler:];
-[NWRemotePacketProxy setOutputProtocolHandler:local:remote:ipProtocol:];
-[NWRemotePacketProxy setPacketHashTable:];
-[NWRemotePacketProxy setPacketProtocol:];
-[NWRemotePacketProxy setReceiveWindowPacketCount:];
-[NWRemotePacketProxy setWriteRequests:];
-[NWRemotePacketProxy writeRequests];
```
