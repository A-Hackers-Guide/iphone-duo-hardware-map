# `NWNetworkAgentSession`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 21 instance methods, 0 class methods

## Instance variables

```
i _sessionFD;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _readSource;
@"NSMutableArray" _registrations;
```

## Properties

```
@property (Ti,V_sessionFD) sessionFD;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSObject<OS_dispatch_source>",&,V_readSource) readSource;
@property (T@"NSMutableArray",&,V_registrations) registrations;
```

## Instance methods

```
-[NWNetworkAgentSession initWithQueue:];
-[NWNetworkAgentSession setRegistrations:];
-[NWNetworkAgentSession registrations];
-[NWNetworkAgentSession setReadSource:];
-[NWNetworkAgentSession init];
-[NWNetworkAgentSession dealloc];
-[NWNetworkAgentSession queue];
-[NWNetworkAgentSession initWithFileDescriptor:];
-[NWNetworkAgentSession readSource];
-[NWNetworkAgentSession setQueue:];
-[NWNetworkAgentSession setupReadSource];
-[NWNetworkAgentSession addRegistration:];
-[NWNetworkAgentSession dupSessionFileDescriptor];
-[NWNetworkAgentSession initWithFileDescriptor:queue:];
-[NWNetworkAgentSession readMessageFromFD];
-[NWNetworkAgentSession registrationForAgentUUID:];
-[NWNetworkAgentSession removeRegistration:];
-[NWNetworkAgentSession sessionFD];
-[NWNetworkAgentSession sessionFileDescriptorIsValid];
-[NWNetworkAgentSession setSessionFD:];
-[NWNetworkAgentSession unregisterAll];
```
