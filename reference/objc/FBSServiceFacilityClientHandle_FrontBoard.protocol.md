# `FBSServiceFacilityClientHandle` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (Ti,R,N) pid;
@property (T@"BSProcessHandle",R,N) processHandle;
@property (T@"RBSProcessIdentity",R,C,N) processIdentity;
@property (TB,R,N,GisSuspended) suspended;
@property (T@"NSString",R,C,N) facilityID;
@property (T@"<FBSServiceFacilityClientContext>",&,N) context;
```

## Instance methods

```
-[FBSServiceFacilityClientHandle processIdentity];
-[FBSServiceFacilityClientHandle isSuspended];
-[FBSServiceFacilityClientHandle facilityID];
-[FBSServiceFacilityClientHandle pid];
-[FBSServiceFacilityClientHandle setContext:];
-[FBSServiceFacilityClientHandle processHandle];
-[FBSServiceFacilityClientHandle context];
```
