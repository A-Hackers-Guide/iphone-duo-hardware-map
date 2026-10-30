# `CBScalablePipeManager`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBManager`
- 4 instance variables, 3 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _identifiers;
{?="didRegisterEndpoint"b1"didUnregisterEndpoint"b1"pipeDidConnect"b1"pipeDidDisconnect"b1} _delegateFlags;
@"<CBScalablePipeManagerDelegate>" _delegate;
@"NSHashTable" _pipes;
```

## Properties

```
@property (T@"NSHashTable",R,&,N,V_pipes) pipes;
@property (T@"<CBScalablePipeManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,&,N,V_identifiers) identifiers;
```

## Instance methods

```
-[CBScalablePipeManager handleMsg:args:];
-[CBScalablePipeManager identifiers];
-[CBScalablePipeManager initWithDelegate:];
-[CBScalablePipeManager observeValueForKeyPath:ofObject:change:context:];
-[CBScalablePipeManager registerEndpoint:type:priority:];
-[CBScalablePipeManager isMsgAllowedWhenOff:];
-[CBScalablePipeManager initWithDelegate:queue:];
-[CBScalablePipeManager setLinkRequirementsForPeer:packetsPerSecond:inputBytesPerSecond:outputBytesPerSecond:];
-[CBScalablePipeManager getStatistics:];
-[CBScalablePipeManager unregisterEndpoint:];
-[CBScalablePipeManager sharedPairingAgent];
-[CBScalablePipeManager dealloc];
-[CBScalablePipeManager pipes];
-[CBScalablePipeManager handleEndpointRemoved:];
-[CBScalablePipeManager handleHostStateUpdated:];
-[CBScalablePipeManager pipeForName:identifier:];
-[CBScalablePipeManager orphanPipes];
-[CBScalablePipeManager registerEndpoint:type:priority:transport:requireEncryption:];
-[CBScalablePipeManager setDelegate:];
-[CBScalablePipeManager setLinkRequirementsForPeerWithLatency:latencyInMs:inputBytesPerSecond:outputBytesPerSecond:];
-[CBScalablePipeManager unregisterAllEndpoints];
-[CBScalablePipeManager delegate];
-[CBScalablePipeManager handlePipeDisconnected:];
-[CBScalablePipeManager handleEndpointAdded:];
-[CBScalablePipeManager registerEndpoint:type:priority:options:];
-[CBScalablePipeManager handlePipeConnected:];
-[CBScalablePipeManager registerEndpoint:type:priority:transport:];
-[CBScalablePipeManager setLinkRequirementsForPeer:withClientName:packetsPerSecond:inputBytesPerSecond:outputBytesPerSecond:];
```
