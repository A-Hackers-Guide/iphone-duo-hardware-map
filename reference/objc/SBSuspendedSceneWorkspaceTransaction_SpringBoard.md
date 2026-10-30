# `SBSuspendedSceneWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- Protocols: `FBProcessObserver`
- 2 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSError" _anyLaunchError;
@"NSMutableSet" _outstandingProcessIdentities;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSuspendedSceneWorkspaceTransaction _didComplete];
-[SBSuspendedSceneWorkspaceTransaction _begin];
-[SBSuspendedSceneWorkspaceTransaction _addSceneEntityToAppRecency:];
-[SBSuspendedSceneWorkspaceTransaction _addOutstandingProcessIdentity:];
-[SBSuspendedSceneWorkspaceTransaction processDidExit:];
-[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:];
-[SBSuspendedSceneWorkspaceTransaction _sendActivationResultWithError:];
-[SBSuspendedSceneWorkspaceTransaction main_processDidExit:];
```
