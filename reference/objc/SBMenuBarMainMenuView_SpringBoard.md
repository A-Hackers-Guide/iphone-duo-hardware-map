# `SBMenuBarMainMenuView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- Protocols: `UIGestureRecognizerDelegate`
- 14 instance variables, 19 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _presentingMenuForPointerHoverOrDrag;
B _presentingMenuForKeyPress;
B _presentingMenuForTouchDrag;
B _dismissingMenuForPointerHoverOrDrag;
B _dismissingMenuForTouchDrag;
B _transitioningMenuForPointerClick;
@"_UIMainMenu" _mainMenu;
q _type;
@"<SBMenuBarMainMenuViewDelegate>" _delegate;
@"NSArray" _overflowMenus;
@"<UITraitChangeRegistration>" _traitChangeObservationToken;
@"<BSInvalidatable>" _keyboardFocusLockAssertion;
@"<_UIInvalidatable>" _sceneFocusSystemAssertion;
@"UITapGestureRecognizer" _dismissTapRecognizer;
```

## Properties

```
@property (T@"<UITraitChangeRegistration>",&,N,V_traitChangeObservationToken) traitChangeObservationToken;
@property (T@"<BSInvalidatable>",&,N,V_keyboardFocusLockAssertion) keyboardFocusLockAssertion;
@property (T@"<_UIInvalidatable>",&,N,V_sceneFocusSystemAssertion) sceneFocusSystemAssertion;
@property (T@"UITapGestureRecognizer",&,N,V_dismissTapRecognizer) dismissTapRecognizer;
@property (TB,N,V_transitioningMenuForPointerClick) transitioningMenuForPointerClick;
@property (T@"_UIMainMenu",R,N,V_mainMenu) mainMenu;
@property (Tq,R,N,V_type) type;
@property (T@"<SBMenuBarMainMenuViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",&,N,V_overflowMenus) overflowMenus;
@property (TB,N,GisPresentingMenuForPointerHoverOrDrag,V_presentingMenuForPointerHoverOrDrag) presentingMenuForPointerHoverOrDrag;
@property (TB,N,GisPresentingMenuForKeyPress,V_presentingMenuForKeyPress) presentingMenuForKeyPress;
@property (TB,N,GisPresentingMenuForTouchDrag,V_presentingMenuForTouchDrag) presentingMenuForTouchDrag;
@property (TB,N,GisDismissingMenuForPointerHoverOrDrag,V_dismissingMenuForPointerHoverOrDrag) dismissingMenuForPointerHoverOrDrag;
@property (TB,N,GisDismissingMenuForTouchDrag,V_dismissingMenuForTouchDrag) dismissingMenuForTouchDrag;
@property (TB,R,N,GisTransitioningMenuForInteraction) transitioningMenuForInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMenuBarMainMenuView contextMenuInteraction:willEndForConfiguration:animator:];
-[SBMenuBarMainMenuView gestureRecognizer:shouldReceiveTouch:];
-[SBMenuBarMainMenuView contextMenuInteraction:configurationForMenuAtLocation:];
-[SBMenuBarMainMenuView dealloc];
-[SBMenuBarMainMenuView menuAttachmentPointForConfiguration:];
-[SBMenuBarMainMenuView contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[SBMenuBarMainMenuView setKeyboardFocusLockAssertion:];
-[SBMenuBarMainMenuView touchesBegan:withEvent:];
-[SBMenuBarMainMenuView keyboardFocusLockAssertion];
-[SBMenuBarMainMenuView setDelegate:];
-[SBMenuBarMainMenuView type];
-[SBMenuBarMainMenuView delegate];
-[SBMenuBarMainMenuView _contextMenuInteraction:styleForMenuWithConfiguration:];
-[SBMenuBarMainMenuView _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[SBMenuBarMainMenuView mainMenu];
-[SBMenuBarMainMenuView _handleTapToDismiss:];
-[SBMenuBarMainMenuView setTraitChangeObservationToken:];
-[SBMenuBarMainMenuView initWithMainMenu:type:delegate:];
-[SBMenuBarMainMenuView _focusSpringBoardForMenuBar:];
-[SBMenuBarMainMenuView _menuBarTitleFontFromStatusBarFont:];
-[SBMenuBarMainMenuView dismissTapRecognizer];
-[SBMenuBarMainMenuView displayTitleWithAttributes:];
-[SBMenuBarMainMenuView isDismissingMenuForPointerHoverOrDrag];
-[SBMenuBarMainMenuView isDismissingMenuForTouchDrag];
-[SBMenuBarMainMenuView isPresentingMenuForKeyPress];
-[SBMenuBarMainMenuView isPresentingMenuForPointerHoverOrDrag];
-[SBMenuBarMainMenuView isPresentingMenuForTouchDrag];
-[SBMenuBarMainMenuView isTransitioningMenuForInteraction];
-[SBMenuBarMainMenuView overflowMenus];
-[SBMenuBarMainMenuView sceneFocusSystemAssertion];
-[SBMenuBarMainMenuView setDismissTapRecognizer:];
-[SBMenuBarMainMenuView setDismissingMenuForPointerHoverOrDrag:];
-[SBMenuBarMainMenuView setDismissingMenuForTouchDrag:];
-[SBMenuBarMainMenuView setOverflowMenus:];
-[SBMenuBarMainMenuView setPresentingMenuForKeyPress:];
-[SBMenuBarMainMenuView setPresentingMenuForPointerHoverOrDrag:];
-[SBMenuBarMainMenuView setPresentingMenuForTouchDrag:];
-[SBMenuBarMainMenuView setSceneFocusSystemAssertion:];
-[SBMenuBarMainMenuView setTransitioningMenuForPointerClick:];
-[SBMenuBarMainMenuView traitChangeObservationToken];
-[SBMenuBarMainMenuView transitioningMenuForPointerClick];
```
