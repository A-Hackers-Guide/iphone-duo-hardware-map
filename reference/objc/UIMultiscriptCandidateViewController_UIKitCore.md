# `UIMultiscriptCandidateViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIPredictiveViewController`, `UIKeyboardAutocorrectionObserver`
- 4 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _updatingCandidates;
@"UIViewController<UIPredictiveViewController>" _currentViewController;
@"UIMultiscriptCandidateView" _candidateView;
@"TIAutocorrectionList" _cachedCandidates;
```

## Properties

```
@property (T@"UIViewController<UIPredictiveViewController>",&,N,V_currentViewController) currentViewController;
@property (T@"UIMultiscriptCandidateView",&,N,V_candidateView) candidateView;
@property (T@"TIAutocorrectionList",&,N,V_cachedCandidates) cachedCandidates;
@property (TB,N,V_updatingCandidates) updatingCandidates;
@property (T@"NSArray",?,R,N) displayedCandidates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIMultiscriptCandidateViewController autocorrectionControllerDidClearAutocorrections:];
-[UIMultiscriptCandidateViewController extendsFromKeyplane];
-[UIMultiscriptCandidateViewController hidesExpandableButton];
-[UIMultiscriptCandidateViewController displayedCandidates];
-[UIMultiscriptCandidateViewController dealloc];
-[UIMultiscriptCandidateViewController predictionView];
-[UIMultiscriptCandidateViewController initWithNibName:bundle:];
-[UIMultiscriptCandidateViewController currentViewController];
-[UIMultiscriptCandidateViewController autocorrectionController:didUpdateAutocorrectionList:];
-[UIMultiscriptCandidateViewController viewWillAppear:];
-[UIMultiscriptCandidateViewController _canShowWhileLocked];
-[UIMultiscriptCandidateViewController requiresKeyboard];
-[UIMultiscriptCandidateViewController loadView];
-[UIMultiscriptCandidateViewController preferredHeightForTraitCollection:];
-[UIMultiscriptCandidateViewController overrideUserInterfaceStyle];
-[UIMultiscriptCandidateViewController isVisibleForInputDelegate:inputViews:];
-[UIMultiscriptCandidateViewController alternativeCandidateAction];
-[UIMultiscriptCandidateViewController alternativeCandidates];
-[UIMultiscriptCandidateViewController autocorrectionListDidChange];
-[UIMultiscriptCandidateViewController cachedCandidates];
-[UIMultiscriptCandidateViewController candidateView];
-[UIMultiscriptCandidateViewController reloadArrangedSubviews];
-[UIMultiscriptCandidateViewController setCachedCandidates:];
-[UIMultiscriptCandidateViewController setCandidateView:];
-[UIMultiscriptCandidateViewController setCurrentViewController:];
-[UIMultiscriptCandidateViewController setUpdatingCandidates:];
-[UIMultiscriptCandidateViewController updatingCandidates];
```
