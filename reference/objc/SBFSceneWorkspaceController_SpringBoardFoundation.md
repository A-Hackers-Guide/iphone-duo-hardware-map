# `SBFSceneWorkspaceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `BSDescriptionProviding`
- 2 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"FBSceneWorkspace" _sceneWorkspace;
@"<SBFSceneWorkspaceControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSString",R,C,N) sceneWorkspaceIdentifier;
@property (T@"<SBFSceneWorkspaceControllerDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFSceneWorkspaceController enumerateScenesWithBlock:];
-[SBFSceneWorkspaceController debugDescription];
-[SBFSceneWorkspaceController succinctDescriptionBuilder];
-[SBFSceneWorkspaceController descriptionWithMultilinePrefix:];
-[SBFSceneWorkspaceController succinctDescription];
-[SBFSceneWorkspaceController invalidate];
-[SBFSceneWorkspaceController sceneFromIdentityToken:];
-[SBFSceneWorkspaceController delegate];
-[SBFSceneWorkspaceController description];
-[SBFSceneWorkspaceController initWithIdentifier:delegate:];
-[SBFSceneWorkspaceController sceneWorkspaceIdentifier];
-[SBFSceneWorkspaceController sceneFromIdentityTokenStringRepresentation:];
-[SBFSceneWorkspaceController descriptionBuilderWithMultilinePrefix:];
-[SBFSceneWorkspaceController createSceneForProcessIdentity:withOptions:completion:];
```
