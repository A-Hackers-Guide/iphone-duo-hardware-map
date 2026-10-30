# `FBServiceFacilityServerClientHandle`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSServiceFacilityClientHandle_Internal`, `BSInvalidatable`
- 5 instance variables, 11 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSString" _facilityID;
@"BSServiceConnection" _connection;
@"FBProcess" _process;
@"BSProcessHandle" _processHandle;
@"<FBSServiceFacilityClientContext>" _context;
```

## Properties

```
@property (T@"<BSXPCServiceConnectionMessaging>",R,N) clientHandle_messageBuilder;
@property (Ti,R,N) pid;
@property (T@"BSProcessHandle",R,N,V_processHandle) processHandle;
@property (T@"RBSProcessIdentity",R,C,N) processIdentity;
@property (TB,R,N,GisSuspended) suspended;
@property (T@"NSString",R,C,N,V_facilityID) facilityID;
@property (T@"<FBSServiceFacilityClientContext>",&,N,V_context) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBServiceFacilityServerClientHandle processIdentity];
-[FBServiceFacilityServerClientHandle clientHandle_messageBuilder];
-[FBServiceFacilityServerClientHandle isSuspended];
-[FBServiceFacilityServerClientHandle initWithFacilityID:connection:];
-[FBServiceFacilityServerClientHandle facilityID];
-[FBServiceFacilityServerClientHandle invalidate];
-[FBServiceFacilityServerClientHandle pid];
-[FBServiceFacilityServerClientHandle setContext:];
-[FBServiceFacilityServerClientHandle processHandle];
-[FBServiceFacilityServerClientHandle description];
-[FBServiceFacilityServerClientHandle prettyProcessDescription];
-[FBServiceFacilityServerClientHandle context];
```
