# `_TtC7Network3Ack`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 20 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Network.LogPrefixer log;
Network.AckSpace initialAckSpace;
Network.AckSpace handshakeAckSpace;
Network.AckSpace applicationAckSpace;
_$sSi localDelayExponent;
_$sSi remoteDelayExponent;
_$sSi unackedPacketCount;
Network.NetworkClock.Instant lastSentTime;
Swift.UInt8 ? timerID;
Network.QUICConnection ? connection;
Swift.Bool disableAckCompression;
Network.Ack.Flags flags;
_$sSi delaySize;
_$sSi immediateAcks;
_$sSi packetThreshold;
_$sSi sentFrequencyThreshold;
Network.NetworkDuration maxDelay;
Swift.UInt64 sentFrequencyTimestamp;
_$sSi nextFrequencySequence;
_$sSi receivedFrequencySequence;
```
