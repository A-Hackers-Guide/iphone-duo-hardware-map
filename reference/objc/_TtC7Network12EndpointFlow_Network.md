# `_TtC7Network12EndpointFlow`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 15 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Network.NetworkLoggerState log;
Network.Endpoint localEndpoint;
Network.Endpoint remoteEndpoint;
Network.Parameters parameters;
Network.NetworkContext context;
Swift.UInt64 identifier;
CollectionsInternal.UniqueDeque Network.WriteRequest writeRequests;
_$sSa -> Network.ReadRequest readRequests;
Network.EndpointFlow.State _$scSg -> stateUpdateHandler;
Swift.Bool reuse;
Network.EndpointFlow.State _state;
Network.SystemUUID connectionID;
Network.ProtocolInstanceReference ? quicConnectionReference;
Network.EndpointFlowPrivateStorage privateStorage;
Network.EndpointFlow.FlowProtocol ? flowProtocol;
```
