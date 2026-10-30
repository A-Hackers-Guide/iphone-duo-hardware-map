# `SBWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransaction`
- 7 instance variables, 8 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"SBUIAnimationController" _suggestedAnimationController;
@"SBWorkspaceTransitionRequest" _transitionRequestForPendingInterruption;
B _clearsCompletionAsynchronously;
@"SBWorkspaceTransitionRequest" _transitionRequest;
@"SBWindowScene" _windowScene;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
@"SBSceneManager" _sceneManager;
```

## Properties

```
@property (T@"SBWindowScene",R,N,V_windowScene) windowScene;
@property (T@"SBLayoutStateTransitionCoordinator",R,N,V_layoutStateTransitionCoordinator) layoutStateTransitionCoordinator;
@property (T@"SBSceneManager",R,N,V_sceneManager) sceneManager;
@property (TB,N,V_clearsCompletionAsynchronously) clearsCompletionAsynchronously;
@property (T@"FBSDisplayIdentity",R,N) displayIdentity;
@property (T@"FBSDisplayConfiguration",R,N) displayConfiguration;
@property (T@"SBWorkspaceTransitionRequest",R,N,V_transitionRequest) transitionRequest;
@property (T@"SBUIAnimationController",&,N,V_suggestedAnimationController) suggestedAnimationController;
```

## Instance methods

```
-[SBWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBWorkspaceTransaction sceneManager];
-[SBWorkspaceTransaction _didComplete];
-[SBWorkspaceTransaction displayConfiguration];
-[SBWorkspaceTransaction _customizedDescriptionProperties];
-[SBWorkspaceTransaction init];
-[SBWorkspaceTransaction layoutStateTransitionCoordinator];
-[SBWorkspaceTransaction shouldInterceptTransitionRequest:];
-[SBWorkspaceTransaction initWithTransitionRequest:];
-[SBWorkspaceTransaction windowScene];
-[SBWorkspaceTransaction displayIdentity];
-[SBWorkspaceTransaction _childWorkspaceTransactions];
-[SBWorkspaceTransaction _didInterruptForTransitionRequest:];
-[SBWorkspaceTransaction _isInterruptingForTransitionRequest];
-[SBWorkspaceTransaction _performDeviceCoherencyCheck];
-[SBWorkspaceTransaction _transitionRequestForInterruption];
-[SBWorkspaceTransaction _willInterruptForTransitionRequest:];
-[SBWorkspaceTransaction clearsCompletionAsynchronously];
-[SBWorkspaceTransaction interceptTransitionRequest:];
-[SBWorkspaceTransaction interruptForTransitionRequest:];
-[SBWorkspaceTransaction isMainDisplayTransaction];
-[SBWorkspaceTransaction keepAliveForAsyncBlock:];
-[SBWorkspaceTransaction setClearsCompletionAsynchronously:];
-[SBWorkspaceTransaction setSuggestedAnimationController:];
-[SBWorkspaceTransaction suggestedAnimationController];
-[SBWorkspaceTransaction transitionRequest];
```
