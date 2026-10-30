# `CBRFCOMMChannel`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 20 instance methods, 0 class methods

## Instance variables

```
C _channelID;
B _isIncoming;
C _dataBits;
C _parity;
C _stopBits;
S _mtu;
i _socketFD;
I _baudRate;
@"CBClassicPeer" _peer;
@"NSInputStream" _inputStream;
@"NSOutputStream" _outputStream;
@"CBUUID" _serviceUUID;
```

## Properties

```
@property (Ti,R,N,V_socketFD) socketFD;
@property (T@"CBClassicPeer",R,N,V_peer) peer;
@property (T@"NSInputStream",R,N,V_inputStream) inputStream;
@property (T@"NSOutputStream",R,N,V_outputStream) outputStream;
@property (T@"CBUUID",R,N,V_serviceUUID) serviceUUID;
@property (TC,R,N,V_channelID) channelID;
@property (TS,R,N,V_mtu) mtu;
@property (TB,R,N,V_isIncoming) isIncoming;
@property (TI,N,V_baudRate) baudRate;
@property (TC,N,V_dataBits) dataBits;
@property (TC,N,V_parity) parity;
@property (TC,N,V_stopBits) stopBits;
```

## Instance methods

```
-[CBRFCOMMChannel mtu];
-[CBRFCOMMChannel outputStream];
-[CBRFCOMMChannel serviceUUID];
-[CBRFCOMMChannel dealloc];
-[CBRFCOMMChannel channelID];
-[CBRFCOMMChannel inputStream];
-[CBRFCOMMChannel peer];
-[CBRFCOMMChannel isIncoming];
-[CBRFCOMMChannel description];
-[CBRFCOMMChannel baudRate];
-[CBRFCOMMChannel setBaudRate:];
-[CBRFCOMMChannel socketFD];
-[CBRFCOMMChannel configureChannelPortParams:dataBits:parity:stopBits:];
-[CBRFCOMMChannel dataBits];
-[CBRFCOMMChannel initWithPeer:info:];
-[CBRFCOMMChannel parity];
-[CBRFCOMMChannel setDataBits:];
-[CBRFCOMMChannel setParity:];
-[CBRFCOMMChannel setStopBits:];
-[CBRFCOMMChannel stopBits];
```
