# `UIPredictionViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `TUIPredictionViewDelegate`, `UIKeyboardAutocorrectionObserver`, `UIPredictiveViewController`
- 10 instance variables, 11 properties, 47 instance methods, 1 class methods

## Instance variables

```
@"NSTimer" _updateUITimer;
@"NSDate" _lastUIUpdateTime;
@"UIInputViewSetPlacement" _savedPlacement;
Q _pushTimeStamp;
@"TUIPredictionView" _predictionView;
@"TUIHostingInputCandidateController" _hostingInputCandidateController;
@"TIAutocorrectionList" _cachedAutocorrectionList;
@"_UIKeyboardCandidateGenerationContext" _cachedCandidateGenerationContext;
@"_UIInProcessAndHostedInputCandidateViewContainer" _hostedViewContainer;
@"UIViewController" _disambiguationViewController;
```

## Properties

```
@property (T@"TIAutocorrectionList",&,N,V_cachedAutocorrectionList) cachedAutocorrectionList;
@property (T@"_UIKeyboardCandidateGenerationContext",&,N,V_cachedCandidateGenerationContext) cachedCandidateGenerationContext;
@property (T@"_UIInProcessAndHostedInputCandidateViewContainer",&,N,V_hostedViewContainer) hostedViewContainer;
@property (T@"UIViewController",&,N,V_disambiguationViewController) disambiguationViewController;
@property (T@"TUIPredictionView",R,N,V_predictionView) predictionView;
@property (T@"TUIHostingInputCandidateController",R,N,V_hostingInputCandidateController) hostingInputCandidateController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",?,R,N) displayedCandidates;
```

## Class methods

```
+[UIPredictionViewController _currentInputModeShowsMultiscriptOrTransliterationCandidates];
```

## Instance methods

```
-[UIPredictionViewController autocorrectionControllerDidClearAutocorrections:];
-[UIPredictionViewController extendsFromKeyplane];
-[UIPredictionViewController _registerForNotifications];
-[UIPredictionViewController hidesExpandableButton];
-[UIPredictionViewController displayedCandidates];
-[UIPredictionViewController _updateAutocorrectionList:candidateGenerationContext:];
-[UIPredictionViewController setCachedCandidateGenerationContext:];
-[UIPredictionViewController _shouldShowTextEffectsButtonForAutocorrectionList:];
-[UIPredictionViewController setHostedViewContainer:];
-[UIPredictionViewController viewWillDisappear:];
-[UIPredictionViewController _teardownHostedView];
-[UIPredictionViewController dealloc];
-[UIPredictionViewController viewDidLoad];
-[UIPredictionViewController predictionView];
-[UIPredictionViewController _inputResponderDidChangeNotification:];
-[UIPredictionViewController _initializePredictiveViewAndSecurePredictiveView];
-[UIPredictionViewController initWithNibName:bundle:];
-[UIPredictionViewController autocorrectionController:didUpdateAutocorrectionList:];
-[UIPredictionViewController viewWillAppear:];
-[UIPredictionViewController _registerAsAutocorrectionObserver];
-[UIPredictionViewController _canShowWhileLocked];
-[UIPredictionViewController requiresKeyboard];
-[UIPredictionViewController _autocorrectionListMayCausePredictionViewToReappear:];
-[UIPredictionViewController predictionView:didSelectCandidate:];
-[UIPredictionViewController contextMenuDidDismiss];
-[UIPredictionViewController _initalizeLegacyView];
-[UIPredictionViewController setCachedAutocorrectionList:];
-[UIPredictionViewController _clearTextSuggestions];
-[UIPredictionViewController _isVisibleForAutocorrectionType:];
-[UIPredictionViewController preferredHeightForTraitCollection:];
-[UIPredictionViewController cachedAutocorrectionList];
-[UIPredictionViewController hostedPredictionViewDidSelectCandidate:authenticationMessage:];
-[UIPredictionViewController _lazilyCreateHostedView];
-[UIPredictionViewController _autocorrectionListContainsContinuousPathConversions:];
-[UIPredictionViewController _showDisambiguationUIForCandidate:inView:];
-[UIPredictionViewController _performThrottledUpdateUIWithAutocorrectionList:candidateGenerationContext:];
-[UIPredictionViewController cachedCandidateGenerationContext];
-[UIPredictionViewController disambiguationViewController];
-[UIPredictionViewController _currentTextSuggestions];
-[UIPredictionViewController _throttledUpdateUIWithAutocorrectionList:candidateGenerationContext:];
-[UIPredictionViewController setDisambiguationViewController:];
-[UIPredictionViewController _inputModeDidChange];
-[UIPredictionViewController hostingInputCandidateController];
-[UIPredictionViewController contextMenuDidSelectCandidate:];
-[UIPredictionViewController hostedViewContainer];
-[UIPredictionViewController _makeHostedInputCandidateViewProminent:];
-[UIPredictionViewController isVisibleForInputDelegate:inputViews:];
```
