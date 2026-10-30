# `CBScalablePipe`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 15 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"CBScalablePipeManager" _pipeManager;
i _socket;
B _reliablePipe;
C _localCLVersion;
C _peerCLVersion;
S _pipeId;
I _localCLFeatures;
I _peerCLFeatures;
@"CBCentral" _central;
@"CBPeer" _peer;
@"NSString" _name;
q _type;
q _priority;
q _peerType;
@"NSInputStream" _input;
@"NSOutputStream" _output;
^v _channel;
```

## Properties

```
@property (T@"CBCentral",R,N,V_central) central;
@property (T@"CBPeer",R,N,V_peer) peer;
@property (T@"NSString",R,N,V_name) name;
@property (TS,R,N,V_pipeId) pipeId;
@property (Tq,R,N,V_type) type;
@property (Tq,R,N,V_priority) priority;
@property (TB,R,N,V_reliablePipe) reliablePipe;
@property (Tq,R,N,V_peerType) peerType;
@property (T@"NSInputStream",R,N,V_input) input;
@property (T@"NSOutputStream",R,N,V_output) output;
@property (T^v,R,N,V_channel) channel;
@property (TC,R,N,V_localCLVersion) localCLVersion;
@property (TC,R,N,V_peerCLVersion) peerCLVersion;
@property (TI,R,N,V_localCLFeatures) localCLFeatures;
@property (TI,R,N,V_peerCLFeatures) peerCLFeatures;
```

## Instance methods

```
-[CBScalablePipe channel];
-[CBScalablePipe priority];
-[CBScalablePipe input];
-[CBScalablePipe peerType];
-[CBScalablePipe dealloc];
-[CBScalablePipe type];
-[CBScalablePipe peer];
-[CBScalablePipe description];
-[CBScalablePipe output];
-[CBScalablePipe name];
-[CBScalablePipe central];
-[CBScalablePipe localCLFeatures];
-[CBScalablePipe initWithPipeManager:info:];
-[CBScalablePipe localCLVersion];
-[CBScalablePipe peerCLFeatures];
-[CBScalablePipe peerCLVersion];
-[CBScalablePipe pipeId];
-[CBScalablePipe reliablePipe];
-[CBScalablePipe setOrphan];
```
