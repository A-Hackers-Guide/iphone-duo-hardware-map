# `SBPIPControllerCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBIdleTimerProviding`, `SBApplicationHosting`
- 4 instance variables, 6 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _controllersByType;
@"SBWindowSceneManager" _windowSceneManager;
@"NSMutableSet" _pictureInPictureWindowsHiddenReasons;
@"BSCompoundAssertion" _preventPIPFromStartingUnderControllerCenterCompoundAssertion;
```

## Properties

```
@property (T@"SBWindowSceneManager",&,N,V_windowSceneManager) windowSceneManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBPIPControllerCoordinator shouldStartPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:pipContentType:];
-[SBPIPControllerCoordinator handleDestructionRequestForSceneHandles:];
-[SBPIPControllerCoordinator tetheringModeForScenePersistenceIdentifier:pipContentType:];
-[SBPIPControllerCoordinator _activeMediaPegasusAdapterOnWindowScene:];
-[SBPIPControllerCoordinator initWithDisplayContentModeCoordinator:];
-[SBPIPControllerCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBPIPControllerCoordinator toggleProminenceForActiveMediaPictureInPicture];
-[SBPIPControllerCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBPIPControllerCoordinator handlesRotationIndependentOfCoverSheet];
-[SBPIPControllerCoordinator hostedAppWillRotateToInterfaceOrientation:];
-[SBPIPControllerCoordinator restoreFirstActivePictureInPictureFromBundleIdentifiers:forDisplayContentModeSwap:];
-[SBPIPControllerCoordinator splitPIPContextForRestoringSplitPIPOnWindowScene:layoutElements:interfaceOrientation:];
-[SBPIPControllerCoordinator conformsToSBApplicationHosting];
-[SBPIPControllerCoordinator windowSceneManager];
-[SBPIPControllerCoordinator hostedAppSceneHandle];
-[SBPIPControllerCoordinator canHostAnApp];
-[SBPIPControllerCoordinator acquireAssertionToPreventVideoCallPIPFromStartingUnderControlCenter:];
-[SBPIPControllerCoordinator isPresentingPictureInPictureRequiringMedusaKeyboard];
-[SBPIPControllerCoordinator hostedAppSceneHandles];
-[SBPIPControllerCoordinator isPresentingPictureInPictureRequiringFullScreenKeyboard];
-[SBPIPControllerCoordinator setWindowSceneManager:];
-[SBPIPControllerCoordinator hasIdleTimerBehaviors];
-[SBPIPControllerCoordinator setPictureInPictureWindowsHidden:withReason:];
-[SBPIPControllerCoordinator _enumerateControllersByDescendingPriority:];
-[SBPIPControllerCoordinator bundleIdentifiersForVisiblePictureInPictureWindowsInWindowScene:];
-[SBPIPControllerCoordinator controllerForType:];
-[SBPIPControllerCoordinator moveAllPictureInPictureControllersToWindowScene:];
-[SBPIPControllerCoordinator isAnyPictureInPictureWindowVisible];
-[SBPIPControllerCoordinator isHostingAnApp];
-[SBPIPControllerCoordinator registerController:forType:];
-[SBPIPControllerCoordinator coordinatorRequestedIdleTimerBehavior:];
```
