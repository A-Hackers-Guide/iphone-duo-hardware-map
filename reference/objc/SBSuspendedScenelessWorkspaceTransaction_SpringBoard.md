# `SBSuspendedScenelessWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- Protocols: `FBApplicationProcessLaunchTransactionObserver`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSError" _anyLaunchError;
@"NSMapTable" _launchTransactionToSceneEntityMap;
@"NSMutableSet" _outstandingProcessLaunchTransactions;
@"NSMutableSet" _incompleteProcessLaunchTransactions;
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
-[SBSuspendedScenelessWorkspaceTransaction _childTransactionDidComplete:];
-[SBSuspendedScenelessWorkspaceTransaction _didComplete];
-[SBSuspendedScenelessWorkspaceTransaction _begin];
-[SBSuspendedScenelessWorkspaceTransaction transaction:willLaunchProcess:];
-[SBSuspendedScenelessWorkspaceTransaction _sendActivationResultWithError:];
```
