# `NWRemoteConnectionActor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSObject<NWRemoteConnectionActorDelegate>" _delegate;
@"NSMutableDictionary" _connections;
@"NSMutableDictionary" _browsers;
```

## Properties

```
@property (T@"NSObject<NWRemoteConnectionActorDelegate>",W,V_delegate) delegate;
@property (T@"NSMutableDictionary",&,V_connections) connections;
@property (T@"NSMutableDictionary",&,V_browsers) browsers;
```

## Instance methods

```
-[NWRemoteConnectionActor initWithDelegate:];
-[NWRemoteConnectionActor observeValueForKeyPath:ofObject:change:context:];
-[NWRemoteConnectionActor connections];
-[NWRemoteConnectionActor setConnections:];
-[NWRemoteConnectionActor setDelegate:];
-[NWRemoteConnectionActor delegate];
-[NWRemoteConnectionActor browsers];
-[NWRemoteConnectionActor receiveRemoteCommand:];
-[NWRemoteConnectionActor scheduleReadsOnConnection:];
-[NWRemoteConnectionActor sendData:forConnection:];
-[NWRemoteConnectionActor setBrowsers:];
-[NWRemoteConnectionActor updateEndpointsForBrowser:];
-[NWRemoteConnectionActor updatePathForConnection:];
```
