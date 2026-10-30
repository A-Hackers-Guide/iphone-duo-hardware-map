# `NWRemoteConnectionDirector`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
Q _maximumDataChunkSize;
@"NSObject<NWRemoteConnectionDirectorDelegate>" _delegate;
^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v} _directorProtocol;
^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v} _defaultOutputHandler;
^{nw_hash_table=} _protocolHashTable;
@"NSMutableArray" _writeRequests;
```

## Properties

```
@property (T@"NSObject<NWRemoteConnectionDirectorDelegate>",W,V_delegate) delegate;
@property (T^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v},V_directorProtocol) directorProtocol;
@property (T^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v},V_defaultOutputHandler) defaultOutputHandler;
@property (T^{nw_hash_table=},V_protocolHashTable) protocolHashTable;
@property (T@"NSMutableArray",&,V_writeRequests) writeRequests;
@property (T^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v},R,N) protocol;
@property (TQ,N,V_maximumDataChunkSize) maximumDataChunkSize;
```

## Instance methods

```
-[NWRemoteConnectionDirector protocol];
-[NWRemoteConnectionDirector initWithDelegate:];
-[NWRemoteConnectionDirector dealloc];
-[NWRemoteConnectionDirector setDelegate:];
-[NWRemoteConnectionDirector delegate];
-[NWRemoteConnectionDirector createCloseConnectionMessageForClientID:];
-[NWRemoteConnectionDirector createOpenConnectionMessageForClientID:endpoint:parameters:];
-[NWRemoteConnectionDirector createSendDataMessageForClientID:data:receiveWindow:];
-[NWRemoteConnectionDirector createStartBrowseMessageForClientID:descriptor:parameters:];
-[NWRemoteConnectionDirector createStopBrowseMessageForClientID:];
-[NWRemoteConnectionDirector dataModeForFlowID:];
-[NWRemoteConnectionDirector defaultOutputHandler];
-[NWRemoteConnectionDirector directorProtocol];
-[NWRemoteConnectionDirector maximumDataChunkSize];
-[NWRemoteConnectionDirector outputHandlerForFlowID:];
-[NWRemoteConnectionDirector protocolHashTable];
-[NWRemoteConnectionDirector receiveData:forClient:];
-[NWRemoteConnectionDirector receiveRemoteReply:];
-[NWRemoteConnectionDirector setDefaultOutputHandler:];
-[NWRemoteConnectionDirector setDefaultOutputProtocolHandler:];
-[NWRemoteConnectionDirector setDirectorProtocol:];
-[NWRemoteConnectionDirector setMaximumDataChunkSize:];
-[NWRemoteConnectionDirector setOutputProtocolHandler:forFlowID:dataMode:];
-[NWRemoteConnectionDirector setProtocolHashTable:];
-[NWRemoteConnectionDirector setWriteRequests:];
-[NWRemoteConnectionDirector writeRequests];
```
