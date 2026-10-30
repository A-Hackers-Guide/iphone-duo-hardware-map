# `/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`

iOS 27.2 dyld shared cache image. Version `2.0.0.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/Network.framework/Network`
- `/System/Library/Frameworks/CoreML.framework/CoreML`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 9 classes, 0 protocols, 118 methods, 30 properties

### Class pages

Every class and protocol, with its methods: [`_MLLog`](../objc/_MLLog_RemoteCoreML.md), [`_MLNetworkHeaderEncoding`](../objc/_MLNetworkHeaderEncoding_RemoteCoreML.md), [`_MLNetworkOptions`](../objc/_MLNetworkOptions_RemoteCoreML.md), [`_MLNetworkPacket`](../objc/_MLNetworkPacket_RemoteCoreML.md), [`_MLNetworkUtilities`](../objc/_MLNetworkUtilities_RemoteCoreML.md), [`_MLNetworking`](../objc/_MLNetworking_RemoteCoreML.md), [`_MLRemoteConnection`](../objc/_MLRemoteConnection_RemoteCoreML.md), [`_MLRemoteCoreMLErrors`](../objc/_MLRemoteCoreMLErrors_RemoteCoreML.md), [`_MLServer`](../objc/_MLServer_RemoteCoreML.md)

### Classes

`_MLLog`, `_MLNetworkHeaderEncoding`, `_MLNetworkOptions`, `_MLNetworkPacket`, `_MLNetworkUtilities`, `_MLNetworking`, `_MLRemoteConnection`, `_MLRemoteCoreMLErrors`, `_MLServer`

### Properties

```
@property (T@"NSMutableDictionary",R,N,V_networkOptions) networkOptions;
@property (Tq,R,N,V_receiveTimeout) receiveTimeout;
@property (T@"NSMutableData",&,N,V_buffer) buffer;
@property (T@"NSMutableData",&,N,V_doubleBuffer) doubleBuffer;
@property (TQ,N,V_sizeOfPacket) sizeOfPacket;
@property (TQ,N,V_command) command;
@property (T@"NSObject<OS_nw_connection>",&,N,V_connection) connection;
@property (T@"NSObject<OS_nw_listener>",R,N,V_listener) listener;
@property (T@"_MLNetworkOptions",R,N,V_nwOptions) nwOptions;
@property (T@"NSObject<OS_nw_protocol_stack>",R,N,V_protocol_stack) protocol_stack;
@property (T@"NSObject<OS_nw_parameters>",R,N,V_parameters) parameters;
@property (TB,R,N,V_isClient) isClient;
@property (T@"NSObject<OS_os_log>",R,N,V_logType) logType;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_q) q;
@property (T@"NSObject<OS_nw_connection>",R,N,V_connection) connection;
@property (T@"_MLNetworking",R,N,V_nwObj) nwObj;
@property (T@"_MLNetworkOptions",R,N,V_nwOptions) nwOptions;
@property (T@"_MLNetworkPacket",R,N,V_packet) packet;
@property (T@"NSMutableData",&,N,V_outputResult) outputResult;
@property (TQ,R,N,V_jobCount) jobCount;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_semaphore) semaphore;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_q) q;
@property (T@"_MLNetworking",R,N,V_nwObj) nwObj;
@property (T@"_MLNetworkOptions",R,N,V_nwOptions) nwOptions;
@property (T@"_MLNetworkPacket",R,N,V_packet) packet;
@property (T@?,C,N,V_loadFunction) loadFunction;
@property (T@?,C,N,V_predictFunction) predictFunction;
@property (T@?,C,N,V_unLoadFunction) unLoadFunction;
@property (T@?,C,N,V_textFunction) textFunction;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_q) q;
```

## Strings (78)

```
kMLNetworkUseUDP
kMLNetworkLocalAddr
RemoteClient
kMLNetworkUseTLS
com.apple.remoteCoreMLClientNetwork
B40@?0@\"NSObject<OS_dispatch_data>\"8Q16r^v24Q32
RemoteCommon
kMLNetworkPsk
local
added
udp
v16@?0@\"NSObject<OS_nw_protocol_options>\"8
FAIL
kMLNetworkPortNumber
kMLNetworkUseBonjour
tcp
::
v16@?0@\"NSObject<OS_nw_error>\"8
RemoteDaemon
RemoteTool
com.apple.ml.remotelog
kMLNetworkNameIdentifier
_nwcat._udp
removed
v20@?0@\"NSObject<OS_nw_endpoint>\"8B16
v20@?0i8@\"NSObject<OS_nw_error>\"12
0
com.apple.remoteCoreMLServerNetwork
com.apple.remoteCoreMLClient
v8@?0
%@: Client call timeout.
8080
SUCCESS
kMLNetworkFamily
_nwcat._tcp
RemoteServer
v36@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16B24@\"NSObject<OS_nw_error>\"28
kMLNetworkUseAWDL
kMLNetworkLocalPort
v16@?0@\"NSObject<OS_nw_connection>\"8
com.apple.remoteCoreML
com.apple.remoteCoreMLServer
%@: Start connection error code=%d
%@: Release Semaphore
%@: Begin Packet size = %lu command %lu
%@: Header Error Command = %lu
%@: Call Unload
%@: Recived ACK
%@: Unexpected command = %lu
%@: Connection to %s port %u (%s) succeeded!
%@: nw_connection_state_cancelled 
%@: Client Callback
%@: Command = %lu
%@: send error code=%d.
%@: Sent Success code=%d.
%@: lost client connection
%@: Size of Packet: %zu < Size of current %zu buffer_length %zu.
%@: Timeout waiting for server response.
%@: Incoming Packet size = %lu 
%@: Load
%@: Recived PredictReturnResult
%@: Buffer should be empty = %lu
%@: Send Text Size=%zu.
%@: Sucess NO Timeout %d
%@: Decoded Text: %@
%@: Listener %s on %s (%s.%s.%s)
%@: Listener on port %u (%s) waiting
%@: listener (%s) failed
%@: connect to %s port %u (%s) failed, is waiting
%@: connect to %s port %u (%s) failed
%@: Packet size = %lu
%@: server callback
%@: Listener on port %u (%s) ready!
%@: complete disconnect is_complete=%d ,context=%p
%@ : %@
%@: Call Prediction
%@: Accept incoming connection %p 
%@: connection lost
```
