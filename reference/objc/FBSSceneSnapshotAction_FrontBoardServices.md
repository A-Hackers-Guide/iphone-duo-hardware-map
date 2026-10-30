# `FBSSceneSnapshotAction`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneAction`
- Protocols: `FBSSceneSnapshotRequestDelegate`
- 7 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _requests;
@? _requestHandler;
@? _completionHandler;
@"FBSSceneSnapshotRequestHandle" _outgoingRequestHandle;
i _expired;
@"BSActionResponder" _responder;
@"BSSettings" _clientExtendedData;
```

## Properties

```
@property (T@?,C,N,V_requestHandler) requestHandler;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TB,R,D,GisExpired) expired;
@property (Td,R,D,N) expirationInterval;
@property (T@"BSSettings",C,N,V_clientExtendedData) clientExtendedData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSSceneSnapshotAction clientExtendedData];
-[FBSSceneSnapshotAction snapshotRequest:performWithContext:];
-[FBSSceneSnapshotAction expirationInterval];
-[FBSSceneSnapshotAction setCompletionHandler:];
-[FBSSceneSnapshotAction setClientExtendedData:];
-[FBSSceneSnapshotAction completionHandler];
-[FBSSceneSnapshotAction abortForUsageViolation:];
-[FBSSceneSnapshotAction setInvalidationHandler:];
-[FBSSceneSnapshotAction executeRequestsWithHandler:completionHandler:expirationHandler:];
-[FBSSceneSnapshotAction initWithXPCDictionary:];
-[FBSSceneSnapshotAction isExpired];
-[FBSSceneSnapshotAction requestHandler];
-[FBSSceneSnapshotAction invalidate];
-[FBSSceneSnapshotAction snapshotRequestAllowSnapshot:];
-[FBSSceneSnapshotAction setRequestHandler:];
-[FBSSceneSnapshotAction encodeWithXPCDictionary:];
-[FBSSceneSnapshotAction _finishAllRequests];
-[FBSSceneSnapshotAction _remainsActionable];
-[FBSSceneSnapshotAction setExpired:];
-[FBSSceneSnapshotAction setNullificationHandler:];
-[FBSSceneSnapshotAction initWithRequests:expirationInterval:responseHandler:];
-[FBSSceneSnapshotAction fallbackXPCEncodableClass];
-[FBSSceneSnapshotAction _executeNextRequest];
```
