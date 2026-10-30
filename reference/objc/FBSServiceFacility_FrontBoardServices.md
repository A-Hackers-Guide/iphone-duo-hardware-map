# `FBSServiceFacility`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 7 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"BSServiceQueue" _queue;
@"NSSet" _prerequisiteMilestones;
@"NSMutableSet" _clients;
@"NSSet" _clients_immutable;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clients_immutable_lock;
B _invalidated;
```

## Properties

```
@property (T@"NSSet",R,N) _prerequisiteMilestones;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"BSServiceQueue",R,N,V_queue) queue;
@property (T@"NSSet",R,N) clients;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSServiceFacility clients];
-[FBSServiceFacility identifier];
-[FBSServiceFacility succinctDescriptionBuilder];
-[FBSServiceFacility init];
-[FBSServiceFacility dealloc];
-[FBSServiceFacility queue];
-[FBSServiceFacility descriptionWithMultilinePrefix:];
-[FBSServiceFacility succinctDescription];
-[FBSServiceFacility invalidate];
-[FBSServiceFacility initWithIdentifier:queue:];
-[FBSServiceFacility descriptionBuilderWithMultilinePrefix:];
-[FBSServiceFacility sendMessage:withType:toClients:];
-[FBSServiceFacility _prerequisiteMilestones];
-[FBSServiceFacility noteClientDidConnect:withMessage:];
-[FBSServiceFacility noteClientDidDisconnect:];
-[FBSServiceFacility noteDidReceiveMessage:withType:fromClient:];
-[FBSServiceFacility queue_clientDidConnect:withMessage:];
-[FBSServiceFacility queue_clientDidDisconnect:];
-[FBSServiceFacility queue_handleMessage:withType:fromClient:];
-[FBSServiceFacility shouldAllowClientConnection:withMessage:];
```
