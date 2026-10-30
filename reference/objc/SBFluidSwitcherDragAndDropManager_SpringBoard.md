# `SBFluidSwitcherDragAndDropManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSTransactionObserver`, `SBApplicationDropSessionSceneProviding`, `UIDropInteractionDelegate_Private`, `UIDragInteractionDelegate_Private`, `SBDragAndDropWorkspaceTransactionDelegate`
- 15 instance variables, 19 properties, 71 instance methods, 0 class methods

## Instance variables

```
B _windowDragHandledByDruid;
B _hasAddedSwitcherWindowAsDragTarget;
@"SBSwitcherController" _switcherController;
@"SBFluidSwitcherViewController" _switcherContentController;
@"SBSceneManager" _sceneManager;
@"SBApplicationController" _applicationController;
@"<SBFluidSwitcherDragAndDropManagerDelegate>" _delegate;
@"UIDropInteraction" _dropInteraction;
@"SBDragAndDropWorkspaceTransaction" _activeTransaction;
@"NSMapTable" _activeDropSessions;
@"SBWindowDragInteraction" _windowDragInteraction;
@"<UIDragSession>" _windowDragSession;
@? _windowDragSessionPrepareCompletionBlock;
@"NSString" _windowDragSceneIdentifier;
@"NSMutableSet" _requiredContextIdentifiersForMedusaDraggingDestination;
```

## Properties

```
@property (T@"SBSwitcherController",R,W,N,V_switcherController) switcherController;
@property (T@"SBFluidSwitcherViewController",R,W,N,V_switcherContentController) switcherContentController;
@property (T@"SBSceneManager",R,W,N,V_sceneManager) sceneManager;
@property (T@"SBApplicationController",R,W,N,V_applicationController) applicationController;
@property (T@"<SBFluidSwitcherDragAndDropManagerDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIDropInteraction",&,N,V_dropInteraction) dropInteraction;
@property (T@"SBDragAndDropWorkspaceTransaction",&,N,V_activeTransaction) activeTransaction;
@property (T@"NSMapTable",&,N,V_activeDropSessions) activeDropSessions;
@property (T@"SBWindowDragInteraction",&,N,V_windowDragInteraction) windowDragInteraction;
@property (T@"<UIDragSession>",&,N,V_windowDragSession) windowDragSession;
@property (T@?,C,N,V_windowDragSessionPrepareCompletionBlock) windowDragSessionPrepareCompletionBlock;
@property (T@"NSString",&,N,V_windowDragSceneIdentifier) windowDragSceneIdentifier;
@property (TB,N,V_windowDragHandledByDruid) windowDragHandledByDruid;
@property (TB,N,V_hasAddedSwitcherWindowAsDragTarget) hasAddedSwitcherWindowAsDragTarget;
@property (T@"NSMutableSet",&,N,V_requiredContextIdentifiersForMedusaDraggingDestination) requiredContextIdentifiersForMedusaDraggingDestination;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherDragAndDropManager dragInteraction:previewForLiftingItem:session:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:itemsForBeginningSession:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:previewForCancellingItem:withDefault:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:item:willAnimateCancelWithAnimator:];
-[SBFluidSwitcherDragAndDropManager switcherController];
-[SBFluidSwitcherDragAndDropManager dropInteraction:sessionDidEnter:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:sessionDidMove:];
-[SBFluidSwitcherDragAndDropManager dropInteraction:sessionDidUpdate:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:session:didEndWithOperation:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:sessionWillBegin:];
-[SBFluidSwitcherDragAndDropManager sceneManager];
-[SBFluidSwitcherDragAndDropManager dropInteraction:concludeDrop:];
-[SBFluidSwitcherDragAndDropManager newSceneIdentityForApplication:];
-[SBFluidSwitcherDragAndDropManager applicationController];
-[SBFluidSwitcherDragAndDropManager transactionDidComplete:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:session:willEndWithOperation:];
-[SBFluidSwitcherDragAndDropManager dropInteraction:performDrop:];
-[SBFluidSwitcherDragAndDropManager dropInteraction];
-[SBFluidSwitcherDragAndDropManager dropInteraction:canHandleSession:];
-[SBFluidSwitcherDragAndDropManager _requiredContextIDsForDragSessionInView:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:sessionIsRestrictedToDraggingApplication:];
-[SBFluidSwitcherDragAndDropManager dealloc];
-[SBFluidSwitcherDragAndDropManager dropInteraction:item:willAnimateDropWithAnimator:];
-[SBFluidSwitcherDragAndDropManager activeTransaction];
-[SBFluidSwitcherDragAndDropManager setActiveTransaction:];
-[SBFluidSwitcherDragAndDropManager delegate];
-[SBFluidSwitcherDragAndDropManager dropInteraction:sessionDidExit:];
-[SBFluidSwitcherDragAndDropManager dragInteraction:willAnimateLiftWithAnimator:session:];
-[SBFluidSwitcherDragAndDropManager dropInteraction:sessionDidEnd:];
-[SBFluidSwitcherDragAndDropManager dropInteraction:previewForDroppingItem:withDefault:];
-[SBFluidSwitcherDragAndDropManager _dragInteraction:customSpringAnimationBehaviorForCancellingItem:];
-[SBFluidSwitcherDragAndDropManager _dragInteraction:prepareForSession:completion:];
-[SBFluidSwitcherDragAndDropManager _dragInteractionDidCancelLiftWithoutDragging:];
-[SBFluidSwitcherDragAndDropManager _dropInteraction:customSpringAnimationBehaviorForDroppingItem:];
-[SBFluidSwitcherDragAndDropManager setDropInteraction:];
-[SBFluidSwitcherDragAndDropManager _continuousExposeStripsOccluded];
-[SBFluidSwitcherDragAndDropManager isDragAndDropTransactionRunning];
-[SBFluidSwitcherDragAndDropManager _addMedusaDraggingDestinationWindow:];
-[SBFluidSwitcherDragAndDropManager _anyActiveAndVisibleSceneEntityMatches:];
-[SBFluidSwitcherDragAndDropManager _beginTrackingDropSessionIfNeeded:];
-[SBFluidSwitcherDragAndDropManager _removeMedusaDraggingDestinationWindow:];
-[SBFluidSwitcherDragAndDropManager _requiredContextIdentifiersForMedusaDraggingDestination];
-[SBFluidSwitcherDragAndDropManager _windowDragSessionDidEnd];
-[SBFluidSwitcherDragAndDropManager _workspaceWouldAllowTransitionToApplication:];
-[SBFluidSwitcherDragAndDropManager activeDropSessions];
-[SBFluidSwitcherDragAndDropManager dragAndDropTransaction:didBeginGesture:];
-[SBFluidSwitcherDragAndDropManager dragAndDropTransaction:didEndGesture:];
-[SBFluidSwitcherDragAndDropManager dragAndDropTransaction:didPlatterizeWindowDragWithSceneIdentifier:];
-[SBFluidSwitcherDragAndDropManager dragAndDropTransaction:didUpdateGesture:];
-[SBFluidSwitcherDragAndDropManager handleWindowDragGestureRecognizer:];
-[SBFluidSwitcherDragAndDropManager hasAddedSwitcherWindowAsDragTarget];
-[SBFluidSwitcherDragAndDropManager initWithSwitcherController:delegate:];
-[SBFluidSwitcherDragAndDropManager isApplicationActiveAndVisible:];
-[SBFluidSwitcherDragAndDropManager mostRecentSceneIdentityExcludingLiveScenesForApplication:];
-[SBFluidSwitcherDragAndDropManager preferredSceneIdentityForApplication:targetContentIdentifier:preferNewScene:];
-[SBFluidSwitcherDragAndDropManager requiredContextIdentifiersForMedusaDraggingDestination];
-[SBFluidSwitcherDragAndDropManager setActiveDropSessions:];
-[SBFluidSwitcherDragAndDropManager setHasAddedSwitcherWindowAsDragTarget:];
-[SBFluidSwitcherDragAndDropManager setRequiredContextIdentifiersForMedusaDraggingDestination:];
-[SBFluidSwitcherDragAndDropManager setWindowDragHandledByDruid:];
-[SBFluidSwitcherDragAndDropManager setWindowDragInteraction:];
-[SBFluidSwitcherDragAndDropManager setWindowDragSceneIdentifier:];
-[SBFluidSwitcherDragAndDropManager setWindowDragSession:];
-[SBFluidSwitcherDragAndDropManager setWindowDragSessionPrepareCompletionBlock:];
-[SBFluidSwitcherDragAndDropManager shouldBeginWindowDragGesture];
-[SBFluidSwitcherDragAndDropManager switcherContentController];
-[SBFluidSwitcherDragAndDropManager windowDragHandledByDruid];
-[SBFluidSwitcherDragAndDropManager windowDragInteraction];
-[SBFluidSwitcherDragAndDropManager windowDragSceneIdentifier];
-[SBFluidSwitcherDragAndDropManager windowDragSession];
-[SBFluidSwitcherDragAndDropManager windowDragSessionPrepareCompletionBlock];
```
