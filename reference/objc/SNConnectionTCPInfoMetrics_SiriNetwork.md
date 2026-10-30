# `SNConnectionTCPInfoMetrics`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 17 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _interfaceName;
@"NSNumber" _rttCurrent;
@"NSNumber" _rttSmoothed;
@"NSNumber" _rttVariance;
@"NSNumber" _rttBest;
@"NSNumber" _packetsSent;
@"NSNumber" _packetsReceived;
@"NSNumber" _bytesSent;
@"NSNumber" _bytesReceived;
@"NSNumber" _bytesRetransmitted;
@"NSNumber" _bytesUnacked;
@"NSNumber" _duplicateBytesReceived;
@"NSNumber" _outOfOrderBytesReceived;
@"NSNumber" _sendBufferBytes;
@"NSNumber" _sendBandwidth;
@"NSNumber" _synRetransmits;
@"NSNumber" _tfoSynDataAcked;
```

## Properties

```
@property (T@"NSString",R,C,N,V_interfaceName) interfaceName;
@property (T@"NSNumber",R,C,N,V_rttCurrent) rttCurrent;
@property (T@"NSNumber",R,C,N,V_rttSmoothed) rttSmoothed;
@property (T@"NSNumber",R,C,N,V_rttVariance) rttVariance;
@property (T@"NSNumber",R,C,N,V_rttBest) rttBest;
@property (T@"NSNumber",R,C,N,V_packetsSent) packetsSent;
@property (T@"NSNumber",R,C,N,V_packetsReceived) packetsReceived;
@property (T@"NSNumber",R,C,N,V_bytesSent) bytesSent;
@property (T@"NSNumber",R,C,N,V_bytesReceived) bytesReceived;
@property (T@"NSNumber",R,C,N,V_bytesRetransmitted) bytesRetransmitted;
@property (T@"NSNumber",R,C,N,V_bytesUnacked) bytesUnacked;
@property (T@"NSNumber",R,C,N,V_duplicateBytesReceived) duplicateBytesReceived;
@property (T@"NSNumber",R,C,N,V_outOfOrderBytesReceived) outOfOrderBytesReceived;
@property (T@"NSNumber",R,C,N,V_sendBufferBytes) sendBufferBytes;
@property (T@"NSNumber",R,C,N,V_sendBandwidth) sendBandwidth;
@property (T@"NSNumber",R,C,N,V_synRetransmits) synRetransmits;
@property (T@"NSNumber",R,C,N,V_tfoSynDataAcked) tfoSynDataAcked;
```

## Instance methods

```
-[SNConnectionTCPInfoMetrics init];
-[SNConnectionTCPInfoMetrics interfaceName];
-[SNConnectionTCPInfoMetrics bytesRetransmitted];
-[SNConnectionTCPInfoMetrics description];
-[SNConnectionTCPInfoMetrics bytesReceived];
-[SNConnectionTCPInfoMetrics packetsReceived];
-[SNConnectionTCPInfoMetrics bytesSent];
-[SNConnectionTCPInfoMetrics packetsSent];
-[SNConnectionTCPInfoMetrics sendBufferBytes];
-[SNConnectionTCPInfoMetrics tfoSynDataAcked];
-[SNConnectionTCPInfoMetrics rttBest];
-[SNConnectionTCPInfoMetrics bytesUnacked];
-[SNConnectionTCPInfoMetrics duplicateBytesReceived];
-[SNConnectionTCPInfoMetrics outOfOrderBytesReceived];
-[SNConnectionTCPInfoMetrics rttCurrent];
-[SNConnectionTCPInfoMetrics rttSmoothed];
-[SNConnectionTCPInfoMetrics rttVariance];
-[SNConnectionTCPInfoMetrics sendBandwidth];
-[SNConnectionTCPInfoMetrics synRetransmits];
-[SNConnectionTCPInfoMetrics initWithInterfaceName:rttCurrent:rttSmoothed:rttVariance:rttBest:packetsSent:packetsReceived:bytesSent:bytesReceived:bytesRetransmitted:bytesUnacked:duplicateBytesReceived:outOfOrderBytesReceived:sendBufferBytes:sendBandwidth:synRetransmits:tfoSynDataAcked:];
```
