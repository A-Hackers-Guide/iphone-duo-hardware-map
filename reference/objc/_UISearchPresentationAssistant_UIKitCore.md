# `_UISearchPresentationAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDimmingViewDelegate`
- 7 instance variables, 7 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"UIPresentationController" _searchPresentationController;
@"UIView" _searchBarContainerView;
@"UIDimmingView" _dimmingView;
B _isFormSheetPresentation;
B _presentationWasAnimated;
@"UIPresentationController<_UISearchControllerPresenting>" _adaptivePresentationController;
@"<UIViewControllerTransitionCoordinator>" _transitioningToSizeCoordinator;
```

## Properties

```
@property (TB,N,V_presentationWasAnimated) presentationWasAnimated;
@property (T@"UIPresentationController<_UISearchControllerPresenting>",N,V_adaptivePresentationController) adaptivePresentationController;
@property (T@"<UIViewControllerTransitionCoordinator>",&,N,V_transitioningToSizeCoordinator) transitioningToSizeCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISearchPresentationAssistant presentationWasAnimated];
-[_UISearchPresentationAssistant dimmingView];
-[_UISearchPresentationAssistant _searchBarContainerSuperview];
-[_UISearchPresentationAssistant dimmingViewWasTapped:];
-[_UISearchPresentationAssistant _currentTransitionIsRotating];
-[_UISearchPresentationAssistant dealloc];
-[_UISearchPresentationAssistant adaptivePresentationController];
-[_UISearchPresentationAssistant setAdaptivePresentationController:];
-[_UISearchPresentationAssistant searchBarContainerView];
-[_UISearchPresentationAssistant _statusBarPreferredHiddenForInterfaceOrientation:];
-[_UISearchPresentationAssistant _containerFrame];
-[_UISearchPresentationAssistant removeContainerViewFromSuperview];
-[_UISearchPresentationAssistant statusBarAdjustment];
-[_UISearchPresentationAssistant _outermostNavigationControllerForPresentingViewController:];
-[_UISearchPresentationAssistant locateOriginNavigationController];
-[_UISearchPresentationAssistant presentationIsPopoverToOverFullScreenAdaptation];
-[_UISearchPresentationAssistant initWithSearchPresentationController:];
-[_UISearchPresentationAssistant resultsControllerContentOffset];
-[_UISearchPresentationAssistant shouldAccountForStatusBar];
-[_UISearchPresentationAssistant _searchControllerPresenting];
-[_UISearchPresentationAssistant setPresentationWasAnimated:];
-[_UISearchPresentationAssistant _statusBarPreferredHidden];
-[_UISearchPresentationAssistant setTransitioningToSizeCoordinator:];
-[_UISearchPresentationAssistant _statusBarHeightChangeDueToRotation];
-[_UISearchPresentationAssistant searchBarWillResizeForScopeBar];
-[_UISearchPresentationAssistant searchBarToBecomeTopAttached];
-[_UISearchPresentationAssistant transitioningToSizeCoordinator];
-[_UISearchPresentationAssistant ensureAppropriatelySizedSearchBar:];
-[_UISearchPresentationAssistant updateSearchBarContainerFrame];
-[_UISearchPresentationAssistant optimalFrameForSearchBar:];
-[_UISearchPresentationAssistant locatePresentingNavigationController];
```
