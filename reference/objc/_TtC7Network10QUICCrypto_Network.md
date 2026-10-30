# `_TtC7Network10QUICCrypto`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 26 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Network.ProtocolEventManager eventManager;
Network.SwiftTLSProtocol.SwiftTLSInstance tlsInstance;
_$sSi outboundCryptoInitialOffset;
_$sSi outboundCrypto1RTTOffset;
_$sSi outboundCryptoHandshakeOffset;
Network.QUICConnection ? parentConnection;
Network.OutboundStreamLinkage tlsLinkage;
Network.InboundStreamLinkage initialLinkage;
Network.InboundStreamLinkage earlyDataLinkage;
Network.InboundStreamLinkage handshakeLinkage;
Network.InboundStreamLinkage applicationLinkage;
Network.ReassemblyQueue initialReassemblyQueue;
Network.ReassemblyQueue handshakeReassemblyQueue;
Network.ReassemblyQueue applicationReassemblyQueue;
Network.FrameArray initialInboundData;
Network.FrameArray handshakeInboundData;
Network.FrameArray applicationInboundData;
Network.StreamSendBuffer initialOutboundData;
Network.StreamSendBuffer handshakeOutboundData;
Network.StreamSendBuffer applicationOutboundData;
Swift.UInt64 initialOutboundDataOffset;
Swift.UInt64 handshakeOutboundDataOffset;
Swift.UInt64 applicationOutboundDataOffset;
_$sSi ciphersuite;
Swift.Bool enableEarlyData;
CollectionsInternal.Deque Network.QUICCrypto.cryptoQueuedPackets cryptoQueue;
```
