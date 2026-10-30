# `UIInputSwitcherView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardMenuView`
- Protocols: `_UIInputSwitcherSplitMenu`
- 8 instance variables, 6 properties, 61 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" m_inputModes;
@"NSArray" m_inputSwitcherItems;
@"UIInputSwitcherGestureState" m_gestureState;
B _messagesWriteboardFromSwitcher;
B _fileReportFromSwitcher;
B _showsSwitches;
B _isForDictation;
@? m_finishSplitTransitionBlock;
```

## Properties

```
@property (T@"NSArray",R,N,Vm_inputModes) inputModes;
@property (TB,N,V_messagesWriteboardFromSwitcher) messagesWriteboardFromSwitcher;
@property (TB,N,V_fileReportFromSwitcher) fileReportFromSwitcher;
@property (TB,N,V_showsSwitches) showsSwitches;
@property (TB,N,V_isForDictation) isForDictation;
@property (T@?,C,N,Vm_finishSplitTransitionBlock) finishSplitTransitionBlock;
```

## Class methods

```
+[UIInputSwitcherView sharedInstance];
+[UIInputSwitcherView activeInstance];
+[UIInputSwitcherView canShowKeyboardSettings];
```

## Instance methods

```
-[UIInputSwitcherView numberOfItems];
-[UIInputSwitcherView setInputMode:];
-[UIInputSwitcherView tableView:cellForRowAtIndexPath:];
-[UIInputSwitcherView selectedInputMode];
-[UIInputSwitcherView reloadInputModes];
-[UIInputSwitcherView nextInputMode];
-[UIInputSwitcherView removeFromSuperview];
-[UIInputSwitcherView previousInputMode];
-[UIInputSwitcherView initWithFrame:];
-[UIInputSwitcherView preferredSize];
-[UIInputSwitcherView didShow];
-[UIInputSwitcherView _canAddLaunchItem];
-[UIInputSwitcherView _indexOfFastSwitchToggleModeForIdentifier:];
-[UIInputSwitcherView _indexOfInputSwitcherItemWithIdentifier:];
-[UIInputSwitcherView _isHandBiasSwitchVisible];
-[UIInputSwitcherView _itemWithIdentifier:];
-[UIInputSwitcherView _reloadInputSwitcherItems];
-[UIInputSwitcherView _segmentControlValueDidChange:];
-[UIInputSwitcherView _shouldShowFloatingSwitch];
-[UIInputSwitcherView _shouldShowModeSwitches];
-[UIInputSwitcherView _shouldShowSplitSwitch];
-[UIInputSwitcherView buttonPressed:withEvent:location:isForDictation:tapAction:];
-[UIInputSwitcherView buttonPressed:withEvent:location:isLocationInsideViewHitArea:isForDictation:tapAction:];
-[UIInputSwitcherView customizeCell:forItemAtIndex:];
-[UIInputSwitcherView defaultInputMode];
-[UIInputSwitcherView defaultSelectedIndex];
-[UIInputSwitcherView didFinishSplitTransition];
-[UIInputSwitcherView didSelectItemAtIndex:];
-[UIInputSwitcherView fadeWithDelay:];
-[UIInputSwitcherView fileReportFromSwitcher];
-[UIInputSwitcherView finishSplitTransitionBlock];
-[UIInputSwitcherView fontForItemAtIndex:];
-[UIInputSwitcherView inputModes];
-[UIInputSwitcherView isForDictation];
-[UIInputSwitcherView localizedTitleForItemAtIndex:];
-[UIInputSwitcherView messagesWriteboardFromSwitcher];
-[UIInputSwitcherView reportHandBiasToAnalytics:];
-[UIInputSwitcherView returnToKeyboardIfNeeded];
-[UIInputSwitcherView selectInputMode:];
-[UIInputSwitcherView selectNextInputMode];
-[UIInputSwitcherView selectPreviousInputMode];
-[UIInputSwitcherView selectRowForInputMode:];
-[UIInputSwitcherView setFileReportFromSwitcher:];
-[UIInputSwitcherView setFinishSplitTransitionBlock:];
-[UIInputSwitcherView setIsForDictation:];
-[UIInputSwitcherView setMessagesWriteboardFromSwitcher:];
-[UIInputSwitcherView setShowsSwitches:];
-[UIInputSwitcherView shouldSelectItemAtIndex:];
-[UIInputSwitcherView shouldShow];
-[UIInputSwitcherView shouldShowSelectionExtraViewForIndexPath:];
-[UIInputSwitcherView showAsPopupForKey:inLayout:];
-[UIInputSwitcherView showsSwitches];
-[UIInputSwitcherView subtitleFontForItemAtIndex:];
-[UIInputSwitcherView subtitleForItemAtIndex:];
-[UIInputSwitcherView switchAction];
-[UIInputSwitcherView titleForItemAtIndex:];
-[UIInputSwitcherView toggleKeyboardFloatingPreference];
-[UIInputSwitcherView updateSelectionWithPoint:];
-[UIInputSwitcherView usesDeviceLanguageForItemAtIndex:];
-[UIInputSwitcherView willFade];
-[UIInputSwitcherView willFadeForSelectionAtIndex:];
```
