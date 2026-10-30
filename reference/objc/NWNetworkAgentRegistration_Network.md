# `NWNetworkAgentRegistration`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 10 properties, 47 instance methods, 4 class methods

## Instance variables

```
i _registrationSocket;
# _networkAgentClass;
@"NSObject<NWNetworkAgent>" _networkAgent;
@"NSUUID" _registeredUUID;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _readSource;
@"NWNetworkAgentSession" _session;
```

## Properties

```
@property (T#,V_networkAgentClass) networkAgentClass;
@property (T@"NSObject<NWNetworkAgent>",&,V_networkAgent) networkAgent;
@property (T@"NSUUID",&,V_registeredUUID) registeredUUID;
@property (Ti,V_registrationSocket) registrationSocket;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSObject<OS_dispatch_source>",&,V_readSource) readSource;
@property (T@"NWNetworkAgentSession",&,V_session) session;
@property (TB,R,N,GisRegistered) registered;
@property (TI,R,N) tokenCount;
@property (TQ,N) useCount;
```

## Class methods

```
+[NWNetworkAgentRegistration useNetworkAgent:returnUseCount:];
+[NWNetworkAgentRegistration addActiveAssertionToNetworkAgent:];
+[NWNetworkAgentRegistration newRegistrationFileDescriptor];
+[NWNetworkAgentRegistration removeActiveAssertionFromNetworkAgent:];
```

## Instance methods

```
-[NWNetworkAgentRegistration isRegistered];
-[NWNetworkAgentRegistration registerNetworkAgent:withFileDescriptor:];
-[NWNetworkAgentRegistration initWithNetworkAgentClass:session:];
-[NWNetworkAgentRegistration flushTokens];
-[NWNetworkAgentRegistration unregisterNetworkAgent];
-[NWNetworkAgentRegistration setReadSource:];
-[NWNetworkAgentRegistration addToken:];
-[NWNetworkAgentRegistration internalRegisterNetworkAgent:withFileDescriptor:];
-[NWNetworkAgentRegistration assignResolvedEndpoints:toClient:];
-[NWNetworkAgentRegistration dealloc];
-[NWNetworkAgentRegistration createReadSourceWithRegistrationSocket:];
-[NWNetworkAgentRegistration networkAgentClass];
-[NWNetworkAgentRegistration tokenCountWithError:];
-[NWNetworkAgentRegistration queue];
-[NWNetworkAgentRegistration agentFileDescriptor];
-[NWNetworkAgentRegistration setNetworkAgentClass:];
-[NWNetworkAgentRegistration setLowWaterMark:];
-[NWNetworkAgentRegistration setRegisteredUUID:];
-[NWNetworkAgentRegistration setSession:];
-[NWNetworkAgentRegistration setRegisteredNetworkAgent:fileDescriptor:];
-[NWNetworkAgentRegistration descriptionWithIndent:showFullContent:];
-[NWNetworkAgentRegistration setUseCount:];
-[NWNetworkAgentRegistration removeNetworkAgentFromInterfaceNamed:];
-[NWNetworkAgentRegistration useCount];
-[NWNetworkAgentRegistration isRegisteredInternal];
-[NWNetworkAgentRegistration setNetworkAgent:];
-[NWNetworkAgentRegistration addNetworkAgentToInterfaceNamed:];
-[NWNetworkAgentRegistration registrationSocket];
-[NWNetworkAgentRegistration description];
-[NWNetworkAgentRegistration assignDiscoveredEndpoints:toClient:];
-[NWNetworkAgentRegistration initWithNetworkAgentClass:];
-[NWNetworkAgentRegistration handleMessageFromAgent];
-[NWNetworkAgentRegistration handleMessageWithType:payload:payloadLength:];
-[NWNetworkAgentRegistration resetError];
-[NWNetworkAgentRegistration networkAgent];
-[NWNetworkAgentRegistration tokenCount];
-[NWNetworkAgentRegistration readSource];
-[NWNetworkAgentRegistration initWithNetworkAgentClass:queue:];
-[NWNetworkAgentRegistration session];
-[NWNetworkAgentRegistration updateNetworkAgent:];
-[NWNetworkAgentRegistration unregisterNetworkAgentInternal];
-[NWNetworkAgentRegistration registerNetworkAgent:];
-[NWNetworkAgentRegistration assignNexusData:toClient:];
-[NWNetworkAgentRegistration dupRegistrationFileDescriptor];
-[NWNetworkAgentRegistration setRegistrationSocket:];
-[NWNetworkAgentRegistration setQueue:];
-[NWNetworkAgentRegistration registeredUUID];
```
