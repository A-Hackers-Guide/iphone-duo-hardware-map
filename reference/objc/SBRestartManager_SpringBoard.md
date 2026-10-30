# `SBRestartManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 4 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"<SBRestartManagerDelegate>" _delegate;
@"SBInitialRestartState" _initialRestartState;
@"SBStartupTransitionController" _startupController;
@"SBRestartTransitionRequest" _pendingRestartTransitionRequest;
@"<SBRestartManagerWorkspaceDataSource>" _workspaceDataSource;
B _isShuttingDown;
B _isRestartImminent;
@"NSMutableSet" _pendingExternallyControlledRestartReasons;
@"FBSystemService" _systemService;
B _initialized;
```

## Properties

```
@property (T@"BSTransaction<SBStartupTransition>",R,D,N) startupTransition;
@property (T@"SBRestartTransitionRequest",R,N,V_pendingRestartTransitionRequest) pendingRestartTransitionRequest;
@property (TB,R,D,N,GisPendingExit) pendingExit;
@property (TB,R,N,GisInitialized,V_initialized) initialized;
```

## Instance methods

```
-[SBRestartManager succinctDescriptionBuilder];
-[SBRestartManager descriptionWithMultilinePrefix:];
-[SBRestartManager succinctDescription];
-[SBRestartManager description];
-[SBRestartManager isInitialized];
-[SBRestartManager descriptionBuilderWithMultilinePrefix:];
-[SBRestartManager isPendingExit];
-[SBRestartManager rebootWithContext:];
-[SBRestartManager pendingRestartTransitionRequest];
-[SBRestartManager _exitIsImminent];
-[SBRestartManager ___waitForeverForRunningBoardKill];
-[SBRestartManager _addPendingExternallyControlledRestartReason:];
-[SBRestartManager _doRestartForTransition:];
-[SBRestartManager _initWithWorkspaceDataSource:startupController:systemService:delegate:];
-[SBRestartManager _isPendingExitIncludingExternallyControlledReasons:];
-[SBRestartManager _killAllAppsForPendingExitWithReason:description:expiration:completion:];
-[SBRestartManager _persistStartupTransitionContextFromRebootContext:];
-[SBRestartManager _persistStartupTransitionContextFromRestartRequest:];
-[SBRestartManager _persistStartupTransitionContextFromShutdownContext:];
-[SBRestartManager _persistentSnapshotOverlayDescriptorsWithName:];
-[SBRestartManager _playShutdownSound:];
-[SBRestartManager _postShutdownNotification];
-[SBRestartManager _reallyRestartWithTransitionRequest:];
-[SBRestartManager _removePendingExternallyControlledRestartReason:];
-[SBRestartManager _restartWithTransitionRequest:];
-[SBRestartManager _shutdownSoundDidComplete:completion:];
-[SBRestartManager _shutdownUsingOptions:];
-[SBRestartManager initWithWorkspaceDataSource:delegate:];
-[SBRestartManager initializeAndRunStartupTransition:];
-[SBRestartManager rebootForReason:];
-[SBRestartManager restartWithTransitionRequest:];
-[SBRestartManager runStartupTransitionWithInitialRestartState:callbackBlock:];
-[SBRestartManager shutdownForReason:];
-[SBRestartManager shutdownWithContext:];
-[SBRestartManager startupTransition];
```
