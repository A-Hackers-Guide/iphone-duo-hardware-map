# `SBLayoutStateTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _complete;
B _animationsDisabled;
@"SBLayoutState" _fromLayoutState;
@"SBLayoutState" _toLayoutState;
@"NSError" _error;
@"SBWorkspaceTransaction" _workspaceTransaction;
@"SBWorkspaceApplicationSceneTransitionContext" _applicationTransitionContext;
```

## Properties

```
@property (T@"SBWorkspaceTransaction",R,W,N,V_workspaceTransaction) workspaceTransaction;
@property (T@"SBWorkspaceApplicationSceneTransitionContext",R,W,N,V_applicationTransitionContext) applicationTransitionContext;
@property (T@"SBLayoutState",R,N,V_fromLayoutState) fromLayoutState;
@property (T@"SBLayoutState",R,N,V_toLayoutState) toLayoutState;
@property (TB,R,N,GisComplete,V_complete) complete;
@property (T@"NSError",R,N,V_error) error;
@property (TB,R,N,GisInterrupted) interrupted;
@property (TB,R,N,V_animationsDisabled) animationsDisabled;
```

## Instance methods

```
-[SBLayoutStateTransitionContext isInterrupted];
-[SBLayoutStateTransitionContext isComplete];
-[SBLayoutStateTransitionContext init];
-[SBLayoutStateTransitionContext error];
-[SBLayoutStateTransitionContext fromLayoutState];
-[SBLayoutStateTransitionContext animationsDisabled];
-[SBLayoutStateTransitionContext applicationTransitionContext];
-[SBLayoutStateTransitionContext initWithWorkspaceTransaction:];
-[SBLayoutStateTransitionContext toLayoutState];
-[SBLayoutStateTransitionContext transitionCompletedWithError:];
-[SBLayoutStateTransitionContext workspaceTransaction];
```
