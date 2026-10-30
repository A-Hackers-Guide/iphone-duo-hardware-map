# `NWResolver`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 9 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NWEndpoint" _endpoint;
@"NWParameters" _parameters;
@"NSObject<OS_nw_resolver>" _internalResolver;
q _internalStatus;
@"NSSet" _internalResolvedEndpoints;
@"NSArray" _internalResolvedEndpointArray;
```

## Properties

```
@property (T@"NSObject<OS_nw_resolver>",R,V_internalResolver) internalResolver;
@property (Tq,V_internalStatus) internalStatus;
@property (T@"NSSet",&,V_internalResolvedEndpoints) internalResolvedEndpoints;
@property (T@"NSArray",&,V_internalResolvedEndpointArray) internalResolvedEndpointArray;
@property (Tq,R,N) status;
@property (T@"NWEndpoint",R,V_endpoint) endpoint;
@property (T@"NWParameters",R,V_parameters) parameters;
@property (T@"NSSet",R,N) resolvedEndpoints;
@property (T@"NSArray",R,N) resolvedEndpointArray;
```

## Class methods

```
+[NWResolver automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[NWResolver parameters];
-[NWResolver initWithPath:];
-[NWResolver dealloc];
-[NWResolver endpoint];
-[NWResolver status];
-[NWResolver initWithEndpoint:parameters:];
-[NWResolver copyResolvedEndpointArray];
-[NWResolver copyResolvedEndpoints];
-[NWResolver internalResolvedEndpointArray];
-[NWResolver internalResolvedEndpoints];
-[NWResolver internalResolver];
-[NWResolver internalStatus];
-[NWResolver resolvedEndpointArray];
-[NWResolver resolvedEndpoints];
-[NWResolver setInternalResolvedEndpointArray:];
-[NWResolver setInternalResolvedEndpoints:];
-[NWResolver setInternalStatus:];
-[NWResolver setUpdateHandler];
```
