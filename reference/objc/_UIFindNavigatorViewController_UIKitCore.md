# `_UIFindNavigatorViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewController`
- Protocols: `_UIFindNavigatorViewDelegate`, `UIPredictiveViewController`
- 10 instance variables, 11 properties, 54 instance methods, 0 class methods

## Instance variables

```
q _assistantBarStyle;
@"_UIFindNavigatorView" _findNavigatorView;
@"NSArray" _extraKeyCommands;
@"NSString" _lastSearchQuery;
@"UITextSearchOptions" _lastSearchOptions;
B _performingReplacement;
@"UIFindSession" _findSession;
@"<_UIFindNavigatorViewControllerDelegate>" _findNavigatorViewControllerDelegate;
@"UIResponder" _parentResponder;
Q _tintTechnique;
```

## Properties

```
@property (TB,R,N) hostedInKeyboard;
@property (T@"UIFindSession",&,N,V_findSession) findSession;
@property (T@"_UIFindNavigatorView",R,N) findNavigatorView;
@property (T@"<_UIFindNavigatorViewControllerDelegate>",W,N,V_findNavigatorViewControllerDelegate) findNavigatorViewControllerDelegate;
@property (T@"UIResponder",W,N,V_parentResponder) parentResponder;
@property (TQ,N,V_tintTechnique) tintTechnique;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",?,R,N) displayedCandidates;
```

## Instance methods

```
-[_UIFindNavigatorViewController parentResponder];
-[_UIFindNavigatorViewController _performAutoSearch];
-[_UIFindNavigatorViewController _handleHighlightPreviousResult:];
-[_UIFindNavigatorViewController _configuredSearchOptions];
-[_UIFindNavigatorViewController _textViewDidChangeNotification:];
-[_UIFindNavigatorViewController findNavigator:didInvokeNextResultInDirection:];
-[_UIFindNavigatorViewController buildMenuWithBuilder:];
-[_UIFindNavigatorViewController undoManager];
-[_UIFindNavigatorViewController _finishSearchingOnResignIfNecessary];
-[_UIFindNavigatorViewController resignFirstResponderAndFinishSearching];
-[_UIFindNavigatorViewController viewDidLoad];
-[_UIFindNavigatorViewController keyCommands];
-[_UIFindNavigatorViewController findNavigator:didChangeMode:];
-[_UIFindNavigatorViewController findNavigatorView];
-[_UIFindNavigatorViewController parentFocusEnvironment];
-[_UIFindNavigatorViewController viewWillMoveToWindow:];
-[_UIFindNavigatorViewController hostedInKeyboard];
-[_UIFindNavigatorViewController setAssistantBarStyle:];
-[_UIFindNavigatorViewController findPrevious:];
-[_UIFindNavigatorViewController _handleSearchReturn:];
-[_UIFindNavigatorViewController _canShowWhileLocked];
-[_UIFindNavigatorViewController _handleDone:];
-[_UIFindNavigatorViewController _performSearchWithQuery:options:];
-[_UIFindNavigatorViewController _searchTextFieldChanged:];
-[_UIFindNavigatorViewController _updateReturnKeyType];
-[_UIFindNavigatorViewController findNavigatorDidInvalidateSearchSession:];
-[_UIFindNavigatorViewController loadView];
-[_UIFindNavigatorViewController findNavigatorViewControllerDelegate];
-[_UIFindNavigatorViewController _didEnterSearchQuery:];
-[_UIFindNavigatorViewController find:];
-[_UIFindNavigatorViewController preferredWidthForTraitCollection:];
-[_UIFindNavigatorViewController setFindNavigatorViewControllerDelegate:];
-[_UIFindNavigatorViewController _replaceFieldDidChange:];
-[_UIFindNavigatorViewController _updateResultsCount];
-[_UIFindNavigatorViewController _windowDidChangeToFirstResponder:];
-[_UIFindNavigatorViewController findNavigatorShouldShowReplacementOption:];
-[_UIFindNavigatorViewController setFindSession:];
-[_UIFindNavigatorViewController nextResponder];
-[_UIFindNavigatorViewController _handleInsertNewline:];
-[_UIFindNavigatorViewController preferredHeightForTraitCollection:];
-[_UIFindNavigatorViewController findSession];
-[_UIFindNavigatorViewController findNext:];
-[_UIFindNavigatorViewController setParentResponder:];
-[_UIFindNavigatorViewController _dismissesKeyboardOnReturn];
-[_UIFindNavigatorViewController _didEnterReplacementString:];
-[_UIFindNavigatorViewController _recomputeConfiguredSearchOptions];
-[_UIFindNavigatorViewController _updateReplaceButtonEnabled];
-[_UIFindNavigatorViewController findNavigator:didInvokeReplaceReplacingAll:];
-[_UIFindNavigatorViewController setTintTechnique:];
-[_UIFindNavigatorViewController tintTechnique];
-[_UIFindNavigatorViewController findAndReplace:];
-[_UIFindNavigatorViewController isVisibleForInputDelegate:inputViews:];
-[_UIFindNavigatorViewController updateViewForActiveFindSession];
-[_UIFindNavigatorViewController allowsCompactAssistantBar];
```
