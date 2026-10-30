# `SecEscrowRequest`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SecEscrowRequestable`
- 1 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SecEscrowRequest request:];
```

## Instance methods

```
-[SecEscrowRequest dealloc];
-[SecEscrowRequest initWithConnection:];
-[SecEscrowRequest connection];
-[SecEscrowRequest setConnection:];
-[SecEscrowRequest cachePrerecord:serializedPrerecord:error:];
-[SecEscrowRequest escrowCompletedWithinLastSeconds:];
-[SecEscrowRequest fetchPrerecord:error:];
-[SecEscrowRequest fetchRequestWaitingOnPasscode:];
-[SecEscrowRequest fetchStatuses:];
-[SecEscrowRequest pendingEscrowUpload:];
-[SecEscrowRequest resetAllRequests:];
-[SecEscrowRequest storePrerecordsInEscrow:];
-[SecEscrowRequest triggerEscrowUpdate:error:];
-[SecEscrowRequest triggerEscrowUpdate:options:error:];
```
