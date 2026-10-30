# `SBPIPSceneContentContainerAdapter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPIPStashableWrapperViewControllerDelegate`, `SBLayoutStateTransitionObserver`, `SBDeviceApplicationSceneHandleObserver`, `SBKeyboardFocusControllerObserver`, `SBKeyboardDismissalParticipant`, `SBPIPContainerViewControllerAdapter`
- 16 instance variables, 8 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"SBPIPContainerViewController<SBPIPContainerViewControllerAdapterContextProviding>" _containerViewController;
@"SBPIPStashableWrapperViewController" _stashableWrappingViewController;
@"UIViewController<SBPIPSceneContentProviding>" _sceneContentViewController;
B _invalidated;
{CGSize="width"d"height"d} _minimumStashTabSize;
@"<SBPIPSceneContentContainerAdapterDelegate>" _delegate;
@"UIApplicationSceneDeactivationAssertion" _sceneDeactivationAssertion;
@"<BSInvalidatable>" _keyboardSuppressionAssertion;
@"__UIKeyboardArbiterManager" _keyboardArbiterManager;
@"<SBKeyboardFocusControlling>" _keyboardFocusController;
@"<BSInvalidatable>" _keyboardFocusObserver;
@"SBKeyboardDismissalManager" _keyboardDismissalManager;
@"<BSInvalidatable>" _keyboardDismissalParticipantHandle;
@"SBKeyboardSuppressionManager" _keyboardSuppressionManager;
@"SBLayoutStateTransitionCoordinator" _transitionCoordinator;
@"SBPIPInteractionSettings" _interactionSettings;
```

## Properties

```
@property (T@"UIViewController<SBPIPSceneContentProviding>",R,N,V_sceneContentViewController) sceneContentViewController;
@property (T@"SBPIPContainerViewController",R,W,N) containerViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSNumber",?,&,N) overrideResourcesUsageReductionTimeout;
@property (TB,?,R,N) shouldSuppressAssociatedElementsInSystemAperture;
```

## Instance methods

```
-[SBPIPSceneContentContainerAdapter layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBPIPSceneContentContainerAdapter keyboardFocusController:externalSceneDidAcquireFocus:];
-[SBPIPSceneContentContainerAdapter dealloc];
-[SBPIPSceneContentContainerAdapter setContainerViewController:];
-[SBPIPSceneContentContainerAdapter invalidate];
-[SBPIPSceneContentContainerAdapter layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBPIPSceneContentContainerAdapter containerViewController];
-[SBPIPSceneContentContainerAdapter containerViewControllerDidEndInteraction:targetWindowScene:];
-[SBPIPSceneContentContainerAdapter containerViewController:handleDestructionRequestForSceneHandle:];
-[SBPIPSceneContentContainerAdapter _dismissKeyboardIfNecessaryForTransitionContext:];
-[SBPIPSceneContentContainerAdapter _effectiveEnvironmentModeForTransitionContext:];
-[SBPIPSceneContentContainerAdapter _hitTestTouch:inWindow:];
-[SBPIPSceneContentContainerAdapter _hostedAppSceneHandle];
-[SBPIPSceneContentContainerAdapter _hostedSceneIsPresentingKeyboard];
-[SBPIPSceneContentContainerAdapter _tapInEnvironmentCanDismiss:];
-[SBPIPSceneContentContainerAdapter _updateDisplayLayoutElementKeyboardFocus:];
-[SBPIPSceneContentContainerAdapter bundleIdentifierForContainerViewController:];
-[SBPIPSceneContentContainerAdapter containerViewController:didSettleOnStashState:];
-[SBPIPSceneContentContainerAdapter containerViewController:didUpdateStashProgress:];
-[SBPIPSceneContentContainerAdapter containerViewController:didUpdateStashState:springSettings:];
-[SBPIPSceneContentContainerAdapter containerViewController:shouldHandleStashingForTransitionContext:];
-[SBPIPSceneContentContainerAdapter containerViewController:wantsStashTabHidden:left:springSettings:completion:];
-[SBPIPSceneContentContainerAdapter containerViewController:willBeginInteractionWithGestureRecognizer:];
-[SBPIPSceneContentContainerAdapter containerViewController:willUpdateStashState:];
-[SBPIPSceneContentContainerAdapter containerViewControllerDidEndSizeChange:];
-[SBPIPSceneContentContainerAdapter containerViewControllerPanGestureDidEnd:];
-[SBPIPSceneContentContainerAdapter containerViewControllerShouldRequireFullScreenKeyboard:];
-[SBPIPSceneContentContainerAdapter containerViewControllerWillBeginSizeChange:behavior:];
-[SBPIPSceneContentContainerAdapter contentViewControllerForContainerViewController:];
-[SBPIPSceneContentContainerAdapter hostedAppSceneHandleForContainerViewController:];
-[SBPIPSceneContentContainerAdapter initWithSceneContentViewController:contentViewLayoutSettings:stashSettings:shadowSettings:interactionSettings:keyboardArbiterManager:keyboardFocusController:keyboardSuppressionManager:keyboardDismissalManager:deactivationManager:transitionCoordinator:delegate:];
-[SBPIPSceneContentContainerAdapter isStashTabHiddenForContainerViewController:];
-[SBPIPSceneContentContainerAdapter keyboardDismissalManager:shouldPreventDismissalForTouch:inWindow:];
-[SBPIPSceneContentContainerAdapter loadSubviewsForContainerViewController:];
-[SBPIPSceneContentContainerAdapter processIdentifierForContainerViewController:];
-[SBPIPSceneContentContainerAdapter sceneContentViewController];
-[SBPIPSceneContentContainerAdapter scenePersistenceIdentifierForContainerViewController:];
-[SBPIPSceneContentContainerAdapter stashableWrapper:didReceivedTapGesture:];
-[SBPIPSceneContentContainerAdapter stashableWrapper:didTransitionToStashed:];
```
