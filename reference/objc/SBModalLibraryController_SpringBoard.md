# `SBModalLibraryController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLayoutStateTransitionObserver`, `SBHLibraryViewControllerObserver`, `SBHModalLibraryPresentationDelegate`, `SBHModalLibraryPresentationObserver`, `SBIdleTimerProviding`, `BSInvalidatable`
- 12 instance variables, 19 properties, 48 instance methods, 0 class methods

## Instance variables

```
B _presentingOrTransitioningSearch;
B _invalidated;
@"SBLibraryViewController" _libraryViewController;
@"SBHIconManager" _iconManager;
@"SBFloatingDockController" _floatingDockController;
@"SBWindowScene" _windowScene;
@"SBHModalLibraryPresenter" _libraryPresenter;
@"UIApplicationSceneDeactivationAssertion" _resignActiveAssertion;
@"<BSInvalidatable>" _keyboardWindowLevelAssertion;
@"SBFloatingDockBehaviorAssertion" _floatingDockBehaviorAssertion;
@"<BSInvalidatable>" _libraryDisplayLayoutElementAssertion;
@"<BSInvalidatable>" _libraryWindowKeyboardFocusAssertion;
```

## Properties

```
@property (T@"SBHIconManager",R,N,V_iconManager) iconManager;
@property (T@"SBFloatingDockController",R,W,N,V_floatingDockController) floatingDockController;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"SBHModalLibraryPresenter",R,N,V_libraryPresenter) libraryPresenter;
@property (T@"UIApplicationSceneDeactivationAssertion",R,N,V_resignActiveAssertion) resignActiveAssertion;
@property (T@"<BSInvalidatable>",&,N,V_keyboardWindowLevelAssertion) keyboardWindowLevelAssertion;
@property (T@"SBFloatingDockBehaviorAssertion",&,N,V_floatingDockBehaviorAssertion) floatingDockBehaviorAssertion;
@property (T@"<BSInvalidatable>",&,N,V_libraryDisplayLayoutElementAssertion) libraryDisplayLayoutElementAssertion;
@property (T@"<BSInvalidatable>",&,N,V_libraryWindowKeyboardFocusAssertion) libraryWindowKeyboardFocusAssertion;
@property (TB,N,GisPresentingOrTransitioningSearch,V_presentingOrTransitioningSearch) presentingOrTransitioningSearch;
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (T@"SBLibraryViewController",R,N,V_libraryViewController) libraryViewController;
@property (TB,R,N,GisPresentingLibraryInForeground) presentingLibraryInForeground;
@property (TB,R,N,GisPresentingLibrary) presentingLibrary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBModalLibraryController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBModalLibraryController iconManager];
-[SBModalLibraryController libraryViewController:willPresentSearchController:];
-[SBModalLibraryController floatingDockController];
-[SBModalLibraryController libraryViewController:didDismissSearchController:];
-[SBModalLibraryController resignActiveAssertion];
-[SBModalLibraryController setFloatingDockBehaviorAssertion:];
-[SBModalLibraryController dealloc];
-[SBModalLibraryController isInvalidated];
-[SBModalLibraryController setInvalidated:];
-[SBModalLibraryController invalidate];
-[SBModalLibraryController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBModalLibraryController floatingDockBehaviorAssertion];
-[SBModalLibraryController _currentLayoutState];
-[SBModalLibraryController hasIdleTimerBehaviors];
-[SBModalLibraryController windowScene];
-[SBModalLibraryController dismissLibraryAnimated:completion:];
-[SBModalLibraryController coordinatorRequestedIdleTimerBehavior:];
-[SBModalLibraryController isPresentingLibraryInForeground];
-[SBModalLibraryController isPresentingLibrary];
-[SBModalLibraryController libraryPresenter];
-[SBModalLibraryController libraryViewController];
-[SBModalLibraryController modalLibraryPresenter:didDismissLibrary:];
-[SBModalLibraryController modalLibraryPresenter:didPassCriticalDismissalPoint:];
-[SBModalLibraryController modalLibraryPresenter:didPresentLibrary:];
-[SBModalLibraryController modalLibraryPresenter:willDismissLibrary:];
-[SBModalLibraryController modalLibraryPresenter:willPresentLibrary:];
-[SBModalLibraryController modalLibraryPresenterShouldAllowSwipeToDismissGesture:];
-[SBModalLibraryController presentLibraryAnimated:completion:];
-[SBModalLibraryController toggleLibraryPresentedAnimated:completion:];
-[SBModalLibraryController _configureFloatingDockBehaviorAssertionForPresented:];
-[SBModalLibraryController _didCompleteTransitionWithLibraryToPresented:];
-[SBModalLibraryController _evaluateKeyboardWindowLevelAssertion];
-[SBModalLibraryController _evaluateResignActiveAssertion];
-[SBModalLibraryController _evaluateWindowStatus];
-[SBModalLibraryController _prepareLibraryViewControllerForDismissal:];
-[SBModalLibraryController _setLibraryDisplayLayoutElementActive:];
-[SBModalLibraryController _willPerformTransitionWithLibraryToPresented:];
-[SBModalLibraryController initWithIconManager:libraryViewController:floatingDockController:windowScene:];
-[SBModalLibraryController isPresentingOrTransitioningSearch];
-[SBModalLibraryController keyboardWindowLevelAssertion];
-[SBModalLibraryController libraryDisplayLayoutElementAssertion];
-[SBModalLibraryController libraryWindowKeyboardFocusAssertion];
-[SBModalLibraryController presentLibraryCategoryPodForCategoryIdentifier:animated:completion:];
-[SBModalLibraryController setKeyboardWindowLevelAssertion:];
-[SBModalLibraryController setLibraryDisplayLayoutElementAssertion:];
-[SBModalLibraryController setLibraryWindowKeyboardFocusAssertion:];
-[SBModalLibraryController setPresentingOrTransitioningSearch:];
```
