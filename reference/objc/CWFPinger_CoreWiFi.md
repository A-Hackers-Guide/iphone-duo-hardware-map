# `CWFPinger`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _stopped;
S _sequenceNumber;
S _identifier;
i _rawSocket;
Q _maxPings;
Q _currentPingCount;
@"NSMutableArray" _latencyValues;
@"NSObject<OS_nw_connection>" _connection;
@"NSObject<OS_dispatch_queue>" _networkQueue;
@? _completion;
```

## Properties

```
@property (T@"NSObject<OS_nw_connection>",&,V_connection) connection;
@property (Ti,V_rawSocket) rawSocket;
@property (T@"NSObject<OS_dispatch_queue>",&,V_networkQueue) networkQueue;
@property (TS,V_sequenceNumber) sequenceNumber;
@property (TS,V_identifier) identifier;
@property (T@?,C,V_completion) completion;
@property (TB,V_stopped) stopped;
@property (TQ,V_maxPings) maxPings;
@property (TQ,V_currentPingCount) currentPingCount;
@property (T@"NSMutableArray",&,V_latencyValues) latencyValues;
@property (Td,R,N) percentLoss;
```

## Instance methods

```
-[CWFPinger setCompletion:];
-[CWFPinger setStopped:];
-[CWFPinger completion];
-[CWFPinger identifier];
-[CWFPinger init];
-[CWFPinger stop];
-[CWFPinger setSequenceNumber:];
-[CWFPinger sequenceNumber];
-[CWFPinger setIdentifier:];
-[CWFPinger connection];
-[CWFPinger setConnection:];
-[CWFPinger stopped];
-[CWFPinger checksumForData:];
-[CWFPinger completePingWithError:];
-[CWFPinger currentPingCount];
-[CWFPinger latencyValues];
-[CWFPinger maxPings];
-[CWFPinger networkQueue];
-[CWFPinger percentLoss];
-[CWFPinger rawSocket];
-[CWFPinger receiveReply];
-[CWFPinger sendPing];
-[CWFPinger setCurrentPingCount:];
-[CWFPinger setLatencyValues:];
-[CWFPinger setMaxPings:];
-[CWFPinger setNetworkQueue:];
-[CWFPinger setRawSocket:];
-[CWFPinger startPingingToHost:withNumberOfPings:completion:];
```
