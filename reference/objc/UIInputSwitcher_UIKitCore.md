# `UIInputSwitcher`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 47 instance methods, 2 class methods

## Instance variables

```
@"UIDelayedAction" m_showSwitcherDelay;
@"UIDelayedAction" m_hideSwitcherDelay;
i m_state;
d m_lastGlobeKeyUpTime;
@"NSString" _newMode;
B _usingCapsLockLanguageSwitch;
B _dismissingEmojiPopover;
B _showsLanguageIndicatorOnly;
@"NSString" _loadedIdentifier;
```

## Properties

```
@property (T@"NSString",C,N,V_loadedIdentifier) loadedIdentifier;
@property (TB,N,V_usingCapsLockLanguageSwitch) usingCapsLockLanguageSwitch;
@property (TB,N,V_dismissingEmojiPopover) dismissingEmojiPopover;
@property (TB,N,V_showsLanguageIndicatorOnly) showsLanguageIndicatorOnly;
```

## Class methods

```
+[UIInputSwitcher sharedInstance];
+[UIInputSwitcher activeInstance];
```

## Instance methods

```
-[UIInputSwitcher setSelectedInputMode:];
-[UIInputSwitcher dismissSwitcherWithDelay:];
-[UIInputSwitcher init];
-[UIInputSwitcher dealloc];
-[UIInputSwitcher selectedInputMode];
-[UIInputSwitcher isVisible];
-[UIInputSwitcher switchMode:withHUD:withDelay:];
-[UIInputSwitcher reloadInputModes];
-[UIInputSwitcher nextInputMode];
-[UIInputSwitcher switchMode:withHUD:withDelay:fromCapsLock:];
-[UIInputSwitcher handleSwitchCommand:withHUD:withDelay:];
-[UIInputSwitcher previousInputMode];
-[UIInputSwitcher isVisibleOrHiding];
-[UIInputSwitcher dismissSwitcher:];
-[UIInputSwitcher availableInputModes];
-[UIInputSwitcher setShowingCapsLockSwitcher:];
-[UIInputSwitcher setUsingCapsLockLanguageSwitch:];
-[UIInputSwitcher cancelHideSwitcherTimer];
-[UIInputSwitcher cancelShowSwitcherTimer];
-[UIInputSwitcher cleanUpAfterHide];
-[UIInputSwitcher clearHideSwitcherTimer];
-[UIInputSwitcher clearShowSwitcherTimer];
-[UIInputSwitcher dismissingEmojiPopover];
-[UIInputSwitcher handleEmojiPicker];
-[UIInputSwitcher handleGlobeKeyEvent:switcherIsVisible:];
-[UIInputSwitcher handleModifiersChangedEvent:];
-[UIInputSwitcher handleNavigationEvent:];
-[UIInputSwitcher handleRotate:];
-[UIInputSwitcher handleSwitchCommand:];
-[UIInputSwitcher handleSwitchingKeyEvent:];
-[UIInputSwitcher hideSwitcher];
-[UIInputSwitcher hideSwitcherIfNeeded];
-[UIInputSwitcher inputModeIdentifierWithNextFlag:];
-[UIInputSwitcher loadedIdentifier];
-[UIInputSwitcher needsFullHUD];
-[UIInputSwitcher setDismissingEmojiPopover:];
-[UIInputSwitcher setLoadedIdentifier:];
-[UIInputSwitcher setShowsLanguageIndicatorOnly:];
-[UIInputSwitcher showSwitcherShouldAutoHide:];
-[UIInputSwitcher showSwitcherWithAutoHide];
-[UIInputSwitcher showSwitcherWithoutAutoHide];
-[UIInputSwitcher showsLanguageIndicator:];
-[UIInputSwitcher showsLanguageIndicatorOnly];
-[UIInputSwitcher touchHideSwitcherTimer];
-[UIInputSwitcher touchShowSwitcherTimer];
-[UIInputSwitcher updateHardwareLayout];
-[UIInputSwitcher usingCapsLockLanguageSwitch];
```
