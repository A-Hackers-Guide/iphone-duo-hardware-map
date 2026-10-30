# `_TtCV7Network22QUICConnectionProtocol21QUICConnectionOptions`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 42 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Swift.UInt64 _initialMaxData;
Swift.UInt64 _initialMaxStreamDataBidirectionalLocal;
Swift.UInt64 _initialMaxStreamDataBidirectionalRemote;
Swift.UInt64 _initialMaxStreamDataUnidirectional;
Swift.UInt64 _initialMaxStreamsBidirectional;
Swift.UInt64 _initialMaxStreamsUnidirectional;
Swift.UInt64 _peerMaxStreamDataBidirectionalLocal;
Swift.UInt64 _peerMaxStreamDataBidirectionalRemote;
Swift.UInt64 _peerMaxData;
Swift.UInt64 _peerMaxDataUnidirectional;
Swift.UInt64 _peerMaxStreamsBidirectional;
Swift.UInt64 _peerMaxStreamsUnidirectional;
Network.QUICConnectionOptionsPrivateStorage privateStorage;
Dispatch.DispatchData ? quicState;
Dispatch.DispatchData ? tlsState;
_$sSa -> Swift.UInt8 ? sourceConnectionID;
_$sSa -> Swift.UInt8 ? destinationConnectionID;
Dispatch.DispatchData _$sSg_ABtYbXBSg -> sessionStateUpdateBlock;
DispatchQueue sessionStateUpdateQueue;
DispatchQueue maxStreamsUpdateQueue;
Swift.UInt8 _$s_ -> Swift.UInt64 _$stYbXBSg maxStreamsUpdateBlock;
Network.QLogConfiguration ? qlogConfiguration;
_$sSiSg maximumConcurrentBidirectionalStreams;
_$sSiSg maximumConcurrentUnidirectionalStreams;
Network.QUICStatelessResetToken ? initialStatelessResetToken;
Network.NetworkDuration _idleTimeout;
Network.QUICConnectionProtocol.QUICConnectionOptions.PathRecoveryTimeout _pathRecoveryTimeout;
_$sSbSg enableL4S;
Swift.UInt16 _maxUDPPayloadSize;
Swift.UInt16 _maxDatagramFrameSize;
Swift.Bool _supportWebTransport;
Swift.Bool _supportResetStreamAt;
Swift.UInt16 _initialPacketSize;
Swift.UInt16 _keepaliveCount;
Swift.UInt8 _ackDelaySize;
Swift.UInt8 _maxPathsPerInterface;
Swift.UInt8 _keyIndex;
Swift.UInt16 _pqtlsMode;
Network.NetworkDuration ? pmtudUpdateInterval;
Swift.UInt16 _$sYbXBSg -> pmtudUpdateBlock;
DispatchQueue pmtudUpdateQueue;
Network.QUICConnectionProtocol.QUICConnectionOptions.Flags flags;
```
