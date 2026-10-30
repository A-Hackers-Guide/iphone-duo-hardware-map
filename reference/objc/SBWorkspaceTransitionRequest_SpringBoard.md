# `SBWorkspaceTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIAnimationControllerTransitionContextProvider`, `SBWorkspaceApplicationSceneTransitionContextDelegate`, `BSDescriptionProviding`
- 10 instance variables, 20 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _displayConfiguration;
@"SBWorkspace" _workspace;
@"NSUUID" _uniqueID;
@"NSString" _eventLabel;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
B _finalized;
q _interfaceOrientation;
@"SBWorkspaceApplicationSceneTransitionContext" _applicationContext;
@"BSProcessHandle" _originatingProcess;
@"SBWorkspaceTransientOverlayTransitionContext" _transientOverlayContext;
```

## Properties

```
@property (TB,R,N) isMainWorkspaceTransitionRequest;
@property (T@"NSSet",R,C,N) toApplicationSceneEntities;
@property (T@"NSSet",R,C,N) fromApplicationSceneEntities;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBWorkspace",R,N,V_workspace) workspace;
@property (T@"FBSDisplayIdentity",R,N) displayIdentity;
@property (T@"FBSDisplayConfiguration",R,N,V_displayConfiguration) displayConfiguration;
@property (T@"BSProcessHandle",&,N,V_originatingProcess) originatingProcess;
@property (T@"NSString",C,N,V_eventLabel) eventLabel;
@property (T@"NSUUID",R,C,N,V_uniqueID) uniqueID;
@property (TB,R,N,GisFinalized,V_finalized) finalized;
@property (T@"SBWorkspaceApplicationSceneTransitionContext",&,N,V_applicationContext) applicationContext;
@property (T@"SBWorkspaceTransientOverlayTransitionContext",&,N,V_transientOverlayContext) transientOverlayContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWorkspaceTransitionRequest finalize];
-[SBWorkspaceTransitionRequest workspace];
-[SBWorkspaceTransitionRequest setApplicationContext:];
-[SBWorkspaceTransitionRequest compactDescriptionBuilder];
-[SBWorkspaceTransitionRequest displayConfiguration];
-[SBWorkspaceTransitionRequest succinctDescriptionBuilder];
-[SBWorkspaceTransitionRequest init];
-[SBWorkspaceTransitionRequest isMainWorkspaceTransitionRequest];
-[SBWorkspaceTransitionRequest applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBWorkspaceTransitionRequest originatingProcess];
-[SBWorkspaceTransitionRequest layoutStateForApplicationTransitionContext:];
-[SBWorkspaceTransitionRequest descriptionWithMultilinePrefix:];
-[SBWorkspaceTransitionRequest setDisplayConfiguration:];
-[SBWorkspaceTransitionRequest modifyTransientOverlayContext:];
-[SBWorkspaceTransitionRequest uniqueID];
-[SBWorkspaceTransitionRequest succinctDescription];
-[SBWorkspaceTransitionRequest previousLayoutStateForApplicationTransitionContext:];
-[SBWorkspaceTransitionRequest setTransientOverlayContext:];
-[SBWorkspaceTransitionRequest applicationContext];
-[SBWorkspaceTransitionRequest description];
-[SBWorkspaceTransitionRequest fromApplicationSceneEntities];
-[SBWorkspaceTransitionRequest _initWithWorkspace:displayConfiguration:];
-[SBWorkspaceTransitionRequest declineWithReason:];
-[SBWorkspaceTransitionRequest toApplicationSceneEntities];
-[SBWorkspaceTransitionRequest setOriginatingProcess:];
-[SBWorkspaceTransitionRequest displayIdentity];
-[SBWorkspaceTransitionRequest isFinalized];
-[SBWorkspaceTransitionRequest descriptionBuilderWithMultilinePrefix:];
-[SBWorkspaceTransitionRequest eventLabel];
-[SBWorkspaceTransitionRequest modifyApplicationContext:];
-[SBWorkspaceTransitionRequest setEventLabel:];
-[SBWorkspaceTransitionRequest setEventLabelWithFormat:];
-[SBWorkspaceTransitionRequest transientOverlayContext];
```
