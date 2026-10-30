# `FBSceneWorkspace`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneCreating_Internal`, `FBWorkspaceEventDispatcherTarget`, `FBSceneEventCoordinating`, `BSDescriptionProviding`
- 13 instance variables, 7 properties, 37 instance methods, 3 class methods

## Instance variables

```
@"FBProcessManager" _processManager;
@"<BSInvalidatable>" _eventDispatcherTargetRegistration;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"FBSceneManagerObserver" _delegate;
@"NSMutableOrderedSet" _lock_observers;
@"NSMutableDictionary" _allScenesByID;
Q _synchronizationBlockDepth;
@"FBSMutableSceneDefinition" _buildingDefinition;
@"FBSMutableSceneParameters" _buildingParameters;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _invalidated;
B _suppressConnectionHandshakes;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"<FBSceneWorkspaceDelegate>",W,D,N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) workspaceIdentifier;
```

## Class methods

```
+[FBSceneWorkspace debugDescription];
+[FBSceneWorkspace sceneIdentityTokenForIdentifier:workspaceIdentifier:];
+[FBSceneWorkspace workspaceWithIdentifier:];
```

## Instance methods

```
-[FBSceneWorkspace _objc_initiateDealloc];
-[FBSceneWorkspace debugDescription];
-[FBSceneWorkspace identifier];
-[FBSceneWorkspace succinctDescriptionBuilder];
-[FBSceneWorkspace removeObserver:];
-[FBSceneWorkspace init];
-[FBSceneWorkspace dealloc];
-[FBSceneWorkspace sceneWithIdentifier:];
-[FBSceneWorkspace descriptionWithMultilinePrefix:];
-[FBSceneWorkspace setIdentity:];
-[FBSceneWorkspace sceneDidInvalidate:];
-[FBSceneWorkspace setClientIdentity:];
-[FBSceneWorkspace scene:willUpdateSettings:];
-[FBSceneWorkspace setSpecification:];
-[FBSceneWorkspace succinctDescription];
-[FBSceneWorkspace workspaceIdentifier];
-[FBSceneWorkspace addObserver:];
-[FBSceneWorkspace invalidate];
-[FBSceneWorkspace setIdentifier:];
-[FBSceneWorkspace setDelegate:];
-[FBSceneWorkspace sceneWithIdentityToken:];
-[FBSceneWorkspace delegate];
-[FBSceneWorkspace description];
-[FBSceneWorkspace createScene:];
-[FBSceneWorkspace initWithIdentifier:];
-[FBSceneWorkspace descriptionBuilderWithMultilinePrefix:];
-[FBSceneWorkspace allScenes];
-[FBSceneWorkspace configureParameters:];
-[FBSceneWorkspace createSceneFromRemnant:withSettings:transitionContext:];
-[FBSceneWorkspace createSceneWithDefinition:];
-[FBSceneWorkspace didAddScene:];
-[FBSceneWorkspace didReceiveHandshake:];
-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:];
-[FBSceneWorkspace scene:didApplyUpdate:];
-[FBSceneWorkspace scene:didCompleteUpdate:];
-[FBSceneWorkspace scene:didPrepareUpdate:];
-[FBSceneWorkspace sceneIdentityTokenForIdentifier:];
```
