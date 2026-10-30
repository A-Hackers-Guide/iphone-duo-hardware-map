# `NWPrivilegedHelper`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_xpc_object>" _listener;
@"NSMutableDictionary" _handlers;
@"NSMutableSet" _allKnownEntitlementSet;
@"NSMutableArray" _allKnownEntitlementGroup;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSObject<OS_xpc_object>",&,V_listener) listener;
@property (T@"NSMutableDictionary",&,V_handlers) handlers;
@property (T@"NSMutableSet",&,V_allKnownEntitlementSet) allKnownEntitlementSet;
@property (T@"NSMutableArray",&,V_allKnownEntitlementGroup) allKnownEntitlementGroup;
```

## Instance methods

```
-[NWPrivilegedHelper setHandlers:];
-[NWPrivilegedHelper handlers];
-[NWPrivilegedHelper initWithQueue:];
-[NWPrivilegedHelper setListener:];
-[NWPrivilegedHelper queue];
-[NWPrivilegedHelper listener];
-[NWPrivilegedHelper setQueue:];
-[NWPrivilegedHelper allKnownEntitlementGroup];
-[NWPrivilegedHelper allKnownEntitlementSet];
-[NWPrivilegedHelper handleRequest:onConnection:];
-[NWPrivilegedHelper registerHandlerFunction:type:allowedEntitlementGroup:];
-[NWPrivilegedHelper registerHelperFunctions];
-[NWPrivilegedHelper setAllKnownEntitlementGroup:];
-[NWPrivilegedHelper setAllKnownEntitlementSet:];
-[NWPrivilegedHelper startThrottlePolicyEventListener];
-[NWPrivilegedHelper startXPCListener];
```
