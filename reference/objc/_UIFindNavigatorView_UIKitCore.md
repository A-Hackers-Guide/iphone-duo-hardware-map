# `_UIFindNavigatorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputView`
- 21 instance variables, 19 properties, 50 instance methods, 0 class methods

## Instance variables

```
{?="left"@"UIView""right"@"UIView""bottom"@"UIView"} _separatorViews;
{?="initialized"B"find"@"UIAction""replace"@"UIAction""matchCase"@"UIAction""wholeWords"@"UIAction"} _searchMenu;
@"_UIFindNavigatorViewLayout" _layout;
q _resolvedHorizontalSizeClass;
B _matchCase;
B _wholeWords;
B _usesOpaqueBackground;
B _replaceButtonEnabled;
B _intrinsicHeightDerivedFromAssistantBar;
@"<_UIFindNavigatorViewDelegate>" _findNavigatorDelegate;
q _mode;
Q _visibleSeparatorEdges;
@"UIButton" _doneButton;
@"UIButton" _settingsButton;
@"UILabel" _resultCountLabel;
q _assistantBarStyle;
@"_UIFindNavigatorSearchTextField" _searchTextField;
@"_UIFindNavigatorSearchTextField" _replaceTextField;
@"UIButton" _nextResultButton;
@"UIButton" _previousResultButton;
@"UIButton" _replaceButton;
```

## Properties

```
@property (T@"UIButton",R,N,V_nextResultButton) nextResultButton;
@property (T@"UIButton",R,N,V_previousResultButton) previousResultButton;
@property (T@"UIButton",R,N,V_replaceButton) replaceButton;
@property (T@"<_UIFindNavigatorViewDelegate>",W,N,V_findNavigatorDelegate) findNavigatorDelegate;
@property (Tq,N,V_mode) mode;
@property (TB,N,V_matchCase) matchCase;
@property (TB,N,V_wholeWords) wholeWords;
@property (TB,N,V_usesOpaqueBackground) usesOpaqueBackground;
@property (TQ,N,V_visibleSeparatorEdges) visibleSeparatorEdges;
@property (T@"UIButton",R,N,V_doneButton) doneButton;
@property (T@"UIButton",R,N,V_settingsButton) settingsButton;
@property (T@"UILabel",R,N,V_resultCountLabel) resultCountLabel;
@property (TB,N,V_replaceButtonEnabled) replaceButtonEnabled;
@property (TB,N,V_intrinsicHeightDerivedFromAssistantBar) intrinsicHeightDerivedFromAssistantBar;
@property (Tq,N,V_assistantBarStyle) assistantBarStyle;
@property (T@"_UIFindNavigatorSearchTextField",R,N,V_searchTextField) searchTextField;
@property (T@"_UIFindNavigatorSearchTextField",R,N,V_replaceTextField) replaceTextField;
@property (TB,R,N) adoptsViewportWidthSpec;
@property (Tq,R,N,V_resolvedHorizontalSizeClass) resolvedHorizontalSizeClass;
```

## Instance methods

```
-[_UIFindNavigatorView didMoveToWindow];
-[_UIFindNavigatorView intrinsicContentSize];
-[_UIFindNavigatorView usesOpaqueBackground];
-[_UIFindNavigatorView doneButton];
-[_UIFindNavigatorView becomeFirstResponder];
-[_UIFindNavigatorView layoutSubviews];
-[_UIFindNavigatorView resignFirstResponder];
-[_UIFindNavigatorView setMode:];
-[_UIFindNavigatorView setAssistantBarStyle:];
-[_UIFindNavigatorView sizeThatFits:];
-[_UIFindNavigatorView searchTextField];
-[_UIFindNavigatorView willMoveToWindow:];
-[_UIFindNavigatorView safeAreaInsetsDidChange];
-[_UIFindNavigatorView setUsesOpaqueBackground:];
-[_UIFindNavigatorView mode];
-[_UIFindNavigatorView find:];
-[_UIFindNavigatorView assistantBarStyle];
-[_UIFindNavigatorView traitCollectionDidChange:];
-[_UIFindNavigatorView _canResignIfContainsFirstResponder];
-[_UIFindNavigatorView initWithFrame:];
-[_UIFindNavigatorView _createNavigatorLayoutForTraitCollection:];
-[_UIFindNavigatorView _handleSearchMenuItem:];
-[_UIFindNavigatorView _invalidateSearchSession];
-[_UIFindNavigatorView _linearFocusMovementSequences];
-[_UIFindNavigatorView _navigatorHostingTypeChanged];
-[_UIFindNavigatorView _preferredBackgroundColorChanged];
-[_UIFindNavigatorView _preferredContentSizeDidChange];
-[_UIFindNavigatorView _replacementEnabled];
-[_UIFindNavigatorView _setNavigatorLayout:];
-[_UIFindNavigatorView adoptsViewportWidthSpec];
-[_UIFindNavigatorView findNavigatorDelegate];
-[_UIFindNavigatorView intrinsicHeightDerivedFromAssistantBar];
-[_UIFindNavigatorView matchCase];
-[_UIFindNavigatorView nextResultButton];
-[_UIFindNavigatorView previousResultButton];
-[_UIFindNavigatorView replaceButton];
-[_UIFindNavigatorView replaceButtonEnabled];
-[_UIFindNavigatorView replaceTextField];
-[_UIFindNavigatorView resolvedHorizontalSizeClass];
-[_UIFindNavigatorView resultCountLabel];
-[_UIFindNavigatorView setFindNavigatorDelegate:];
-[_UIFindNavigatorView setIntrinsicHeightDerivedFromAssistantBar:];
-[_UIFindNavigatorView setMatchCase:];
-[_UIFindNavigatorView setReplaceButtonEnabled:];
-[_UIFindNavigatorView setVisibleSeparatorEdges:];
-[_UIFindNavigatorView setWholeWords:];
-[_UIFindNavigatorView settingsButton];
-[_UIFindNavigatorView suggestedFindMenuItems];
-[_UIFindNavigatorView visibleSeparatorEdges];
-[_UIFindNavigatorView wholeWords];
```
