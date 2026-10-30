# `FBWorkspace`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RBSAssertionObserving`, `FBSceneClient`, `FBSceneClientProvider`
- 21 instance variables, 8 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"<FBWorkspaceDelegate>" _weak_delegate;
@"FBProcess" _weak_process;
@"FBSceneSynchronizer" _synchronizer;
@"FBWorkspaceIncomingConnection" _lock_incomingConnection;
@"FBWorkspaceEventDispatcherSource" _lock_eventDispatcherSource;
@"NSMutableDictionary" _lock_identityToRemnantsMap;
@"NSMutableArray" _lock_pendedRequests;
@"<BSInvalidatable>" _workspaceServiceInjector;
@"FBWorkspaceEndpointPromise" _lock_outgoingEndpointPromise;
@"FBWorkspaceOutgoingConnection" _lock_outgoingConnection;
@"NSMutableDictionary" _lock_identityToSceneMap;
@"BSCompoundAssertion" _compoundAssertion;
@"RBSAssertion" _lock_lifeAssertion;
@"RBSAssertion" _lock_connectAssertion;
@"RBSAssertion" _lock_afterlifeAssertion;
q _lock_activeInterruptionPolicy;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _shouldInjectEndpoint;
B _lock_didReceiveHandshake;
AB _invalidated;
B _test_rejectAllSceneClients;
```

## Properties

```
@property (T@"<FBWorkspaceDelegate>",W,N) delegate;
@property (T@"FBSceneSynchronizer",&,N,V_synchronizer) synchronizer;
@property (T@"FBProcess",R,W,N) process;
@property (T@"BSAuditToken",R,N) auditToken;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBWorkspace assertionWillInvalidate:];
-[FBWorkspace host:didInvalidateWithTransitionContext:completion:];
-[FBWorkspace sceneID:handleInvocation:completion:];
-[FBWorkspace sendActions:];
-[FBWorkspace init];
-[FBWorkspace _resolveSceneLifecycleStateAndInterruptionPolicy];
-[FBWorkspace process];
-[FBWorkspace assertion:didInvalidateWithError:];
-[FBWorkspace dealloc];
-[FBWorkspace sceneID:sendMessage:withResponse:];
-[FBWorkspace _processCallOutQueue_requestScene:];
-[FBWorkspace workspaceID:sendActions:completion:];
-[FBWorkspace host:didReceiveActions:forExtension:];
-[FBWorkspace setDelegate:];
-[FBWorkspace handshakeWithRemnants:];
-[FBWorkspace _sceneForIdentity:];
-[FBWorkspace registerHost:settings:initialClientSettings:fromRemnant:error:];
-[FBWorkspace _terminateWithReason:];
-[FBWorkspace _unregisterSceneForHost:];
-[FBWorkspace delegate];
-[FBWorkspace _handleSceneRequest:];
-[FBWorkspace _sceneForHost:];
-[FBWorkspace _dropLaunchAssertion];
-[FBWorkspace host:sendInvocation:withReply:];
-[FBWorkspace description];
-[FBWorkspace createSceneWithOptions:completion:];
-[FBWorkspace requestSceneWithOptions:completion:];
-[FBWorkspace auditToken];
-[FBWorkspace setSynchronizer:];
-[FBWorkspace _updateProcessAssertionState];
-[FBWorkspace host:didUpdateSettings:withDiff:transitionContext:completion:];
-[FBWorkspace synchronizer];
-[FBWorkspace unregisterHost:];
-[FBWorkspace sceneID:didUpdateClientSettingsWithDiff:transitionContext:completion:];
-[FBWorkspace sceneID:invalidateWithContext:clientError:];
-[FBWorkspace sceneID:didReceiveActions:forExtension:];
```
