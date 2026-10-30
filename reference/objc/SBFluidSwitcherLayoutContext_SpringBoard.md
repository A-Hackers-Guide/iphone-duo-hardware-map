# `SBFluidSwitcherLayoutContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBAppInteractionEventSourceObserving`
- 11 instance variables, 19 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _hasUserInteractedWithActiveApplication;
@"SBFluidSwitcherGesture" _activeGesture;
@"SBWorkspaceApplicationSceneTransitionContext" _activeTransitionContext;
@"SBMainDisplayLayoutState" _currentLayoutState;
@"SBMainDisplayLayoutState" _previousLayoutState;
q _previousInterfaceOrientation;
@"SBAppLayout" _currentAppLayout;
@"SBAppLayout" _transitioningFromAppLayout;
@"SBAppLayout" _transitioningToAppLayout;
@"NSDate" _lastTransitionCompletionDate;
@"SBHomeGestureSettings" _homeGestureSettings;
```

## Properties

```
@property (T@"SBMainDisplayLayoutState",&,N,V_currentLayoutState) currentLayoutState;
@property (T@"SBMainDisplayLayoutState",&,N,V_previousLayoutState) previousLayoutState;
@property (Tq,N,V_previousInterfaceOrientation) previousInterfaceOrientation;
@property (T@"SBAppLayout",&,N,V_currentAppLayout) currentAppLayout;
@property (T@"SBAppLayout",&,N,V_transitioningFromAppLayout) transitioningFromAppLayout;
@property (T@"SBAppLayout",&,N,V_transitioningToAppLayout) transitioningToAppLayout;
@property (T@"NSDate",&,N,V_lastTransitionCompletionDate) lastTransitionCompletionDate;
@property (TB,N,V_hasUserInteractedWithActiveApplication) hasUserInteractedWithActiveApplication;
@property (T@"SBHomeGestureSettings",&,N,V_homeGestureSettings) homeGestureSettings;
@property (T@"SBMainDisplayLayoutState",R,N) layoutState;
@property (T@"SBFluidSwitcherGesture",&,N,V_activeGesture) activeGesture;
@property (T@"SBWorkspaceApplicationSceneTransitionContext",R,N,V_activeTransitionContext) activeTransitionContext;
@property (T@"SBMainDisplayLayoutState",R,N) transitioningFromLayoutState;
@property (T@"SBMainDisplayLayoutState",R,N) transitioningToLayoutState;
@property (Td,R,N) secondsSinceLastTransitionCompletion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherLayoutContext setCurrentLayoutState:];
-[SBFluidSwitcherLayoutContext previousLayoutState];
-[SBFluidSwitcherLayoutContext didEndTransitioningToLayoutStateWithContext:];
-[SBFluidSwitcherLayoutContext layoutState];
-[SBFluidSwitcherLayoutContext transitioningToAppLayout];
-[SBFluidSwitcherLayoutContext eventSource:userTouchedApplication:];
-[SBFluidSwitcherLayoutContext wantsUserClickInAppInteractionEvent];
-[SBFluidSwitcherLayoutContext setPreviousLayoutState:];
-[SBFluidSwitcherLayoutContext homeGestureSettings];
-[SBFluidSwitcherLayoutContext currentAppLayout];
-[SBFluidSwitcherLayoutContext succinctDescriptionBuilder];
-[SBFluidSwitcherLayoutContext shouldAddAppLayoutToFront:whenEndingGestureOfType:layoutContext:];
-[SBFluidSwitcherLayoutContext dealloc];
-[SBFluidSwitcherLayoutContext initWithLayoutState:];
-[SBFluidSwitcherLayoutContext _shouldUpdateSwitcherModelBasedOnTimeOrUserInteraction];
-[SBFluidSwitcherLayoutContext transitioningFromAppLayout];
-[SBFluidSwitcherLayoutContext supportedOrientationsForGestureWithCurrentInterfaceOrientation:];
-[SBFluidSwitcherLayoutContext descriptionWithMultilinePrefix:];
-[SBFluidSwitcherLayoutContext setLastTransitionCompletionDate:];
-[SBFluidSwitcherLayoutContext willBeginTransitioningToLayoutStateWithContext:];
-[SBFluidSwitcherLayoutContext lastTransitionCompletionDate];
-[SBFluidSwitcherLayoutContext setHasUserInteractedWithActiveApplication:];
-[SBFluidSwitcherLayoutContext setTransitioningToAppLayout:];
-[SBFluidSwitcherLayoutContext setActiveGesture:];
-[SBFluidSwitcherLayoutContext transitioningToLayoutState];
-[SBFluidSwitcherLayoutContext succinctDescription];
-[SBFluidSwitcherLayoutContext setHomeGestureSettings:];
-[SBFluidSwitcherLayoutContext currentLayoutState];
-[SBFluidSwitcherLayoutContext shouldAddAppLayoutToFront:forTransitionWithContext:recentAppLayouts:transitionCompleted:windowManagementContext:];
-[SBFluidSwitcherLayoutContext transitioningFromLayoutState];
-[SBFluidSwitcherLayoutContext activeGesture];
-[SBFluidSwitcherLayoutContext setTransitioningFromAppLayout:];
-[SBFluidSwitcherLayoutContext shouldAddAppLayoutToFront:whenBeginningGestureOfType:layoutContext:];
-[SBFluidSwitcherLayoutContext description];
-[SBFluidSwitcherLayoutContext hasUserInteractedWithActiveApplication];
-[SBFluidSwitcherLayoutContext setCurrentAppLayout:];
-[SBFluidSwitcherLayoutContext setPreviousInterfaceOrientation:];
-[SBFluidSwitcherLayoutContext previousInterfaceOrientation];
-[SBFluidSwitcherLayoutContext secondsSinceLastTransitionCompletion];
-[SBFluidSwitcherLayoutContext descriptionBuilderWithMultilinePrefix:];
-[SBFluidSwitcherLayoutContext activeTransitionContext];
-[SBFluidSwitcherLayoutContext userDidClickInApp];
```
