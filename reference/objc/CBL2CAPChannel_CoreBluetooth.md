# `CBL2CAPChannel`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 11 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" incomingPackets;
@? pendingCompletionHandler;
S maxQueuePayloadSize;
B _isIncoming;
B _isPacketBased;
S _PSM;
S _cid;
S _outgoingMTU;
i _socketFD;
@"CBPeer" _peer;
@"NSInputStream" _inputStream;
@"NSOutputStream" _outputStream;
@"CBUUID" _serviceUUID;
@"CBManager" _manager;
```

## Properties

```
@property (T@"CBUUID",&,N,V_serviceUUID) serviceUUID;
@property (TB,N,V_isIncoming) isIncoming;
@property (TB,N,V_isPacketBased) isPacketBased;
@property (TS,V_cid) cid;
@property (Ti,N,V_socketFD) socketFD;
@property (T@"CBManager",W,N,V_manager) manager;
@property (TS,V_outgoingMTU) outgoingMTU;
@property (T@"CBPeer",R,N,V_peer) peer;
@property (T@"NSInputStream",R,N,V_inputStream) inputStream;
@property (T@"NSOutputStream",R,N,V_outputStream) outputStream;
@property (TS,R,N,V_PSM) PSM;
```

## Instance methods

```
-[CBL2CAPChannel sendMsg:args:withReply:];
-[CBL2CAPChannel outputStream];
-[CBL2CAPChannel serviceUUID];
-[CBL2CAPChannel setServiceUUID:];
-[CBL2CAPChannel setManager:];
-[CBL2CAPChannel dealloc];
-[CBL2CAPChannel inputStream];
-[CBL2CAPChannel manager];
-[CBL2CAPChannel peer];
-[CBL2CAPChannel isIncoming];
-[CBL2CAPChannel description];
-[CBL2CAPChannel PSM];
-[CBL2CAPChannel setSocketFD:];
-[CBL2CAPChannel socketFD];
-[CBL2CAPChannel setIsIncoming:];
-[CBL2CAPChannel readPacketsWithCompletionHandler:];
-[CBL2CAPChannel cid];
-[CBL2CAPChannel setCid:];
-[CBL2CAPChannel setOutgoingMTU:];
-[CBL2CAPChannel handleChannelClosed:];
-[CBL2CAPChannel handleDataReceived:];
-[CBL2CAPChannel initWithPeer:manager:info:];
-[CBL2CAPChannel isPacketBased];
-[CBL2CAPChannel managePendingData];
-[CBL2CAPChannel outgoingMTU];
-[CBL2CAPChannel sendData:withCompletion:];
-[CBL2CAPChannel setIsPacketBased:];
```
