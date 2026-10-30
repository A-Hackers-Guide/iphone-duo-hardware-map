# `UIKeyboardLayoutCursor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardLayoutStar`
- Protocols: `UIKBAlertControllerDelegate`
- 24 instance variables, 15 properties, 119 instance methods, 2 class methods

## Instance variables

```
@"UIKBTree" _indirectKeyboard;
@"UIView" _selectionView;
@"NSArray" _keyplaneKeys;
q _selectedKeyIndex;
B _ignoreEventsUntilPressEnds;
@"UILexicon" _recentInputs;
B _disableTouchInput;
@"UIKBTree" _cachedMultitapKeyplane;
B _cachedCanMultitap;
@"UILabel" _dictationHelpLabel;
B _didVariantDelete;
B _isForwardingEvent;
i _overridenSelectedKeyType;
{CGPoint="x"d"y"d} _keyplaneSwitchSelectedKeyFrameCenter;
B _selectInitialKey;
B _suppressOperations;
B _overrideInitialKey;
B _shouldConfigureFloatingContentView;
B _shouldToggleLetterCaseNext;
@"UIAlertController" _recentInputsAlert;
@"NSString" _keyplaneBeforeDictation;
q _selectedKeyBeforeDictation;
Q _lastSelectedKeyIndex;
@"UIWindow" _focusWindow;
```

## Properties

```
@property (T@"UIAlertController",&,N,V_recentInputsAlert) recentInputsAlert;
@property (T@"NSString",&,N,V_keyplaneBeforeDictation) keyplaneBeforeDictation;
@property (Tq,N,V_selectedKeyBeforeDictation) selectedKeyBeforeDictation;
@property (TB,N,V_suppressOperations) suppressOperations;
@property (TB,N,V_overrideInitialKey) overrideInitialKey;
@property (TQ,N,V_lastSelectedKeyIndex) lastSelectedKeyIndex;
@property (TB,N,V_shouldConfigureFloatingContentView) shouldConfigureFloatingContentView;
@property (TB,N,V_shouldToggleLetterCaseNext) shouldToggleLetterCaseNext;
@property (TB,R,N,GisSlimLinearKeyboardTV) slimLinearKeyboardTV;
@property (T@"UIWindow",W,N,V_focusWindow) focusWindow;
@property (T@"UIKBTree",R,N) currentKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardLayoutCursor carKeyboardNameForKeyboard:screenTraits:];
+[UIKeyboardLayoutCursor keyboardSizeForInputMode:screenTraits:keyboardType:];
```

## Instance methods

```
-[UIKeyboardLayoutCursor longPressAction];
-[UIKeyboardLayoutCursor remoteControlReceivedWithEvent:];
-[UIKeyboardLayoutCursor _moveWithEvent:];
-[UIKeyboardLayoutCursor setShift:];
-[UIKeyboardLayoutCursor currentKey];
-[UIKeyboardLayoutCursor diacriticForwardCompose];
-[UIKeyboardLayoutCursor setKeyboardAppearance:];
-[UIKeyboardLayoutCursor isAlphabeticPlane];
-[UIKeyboardLayoutCursor _wheelChangedWithEvent:];
-[UIKeyboardLayoutCursor setRenderConfig:];
-[UIKeyboardLayoutCursor keyViewAnimator];
-[UIKeyboardLayoutCursor setKeyplaneName:];
-[UIKeyboardLayoutCursor pressesCancelled:withEvent:];
-[UIKeyboardLayoutCursor pressesEnded:withEvent:];
-[UIKeyboardLayoutCursor dealloc];
-[UIKeyboardLayoutCursor canHandlePresses:withEvent:];
-[UIKeyboardLayoutCursor canMultitap];
-[UIKeyboardLayoutCursor pressesBegan:withEvent:];
-[UIKeyboardLayoutCursor pressesChanged:withEvent:];
-[UIKeyboardLayoutCursor willMoveToWindow:];
-[UIKeyboardLayoutCursor isKanaPlane];
-[UIKeyboardLayoutCursor usesAutoShift];
-[UIKeyboardLayoutCursor initWithFrame:];
-[UIKeyboardLayoutCursor restoreFocusFromEntryPoint:];
-[UIKeyboardLayoutCursor supportsContinuousPath];
-[UIKeyboardLayoutCursor alertDidDismiss];
-[UIKeyboardLayoutCursor setFocusWindow:];
-[UIKeyboardLayoutCursor shouldMergeKey:];
-[UIKeyboardLayoutCursor targetKeyIndexFromPoint:inKeys:];
-[UIKeyboardLayoutCursor canHandleEvent:];
-[UIKeyboardLayoutCursor setHighlightedVariantIndex:key:];
-[UIKeyboardLayoutCursor targetKeyIndexAtOffset:fromKey:];
-[UIKeyboardLayoutCursor _handleMoveWithEvent:];
-[UIKeyboardLayoutCursor _handlePresses:withEvent:];
-[UIKeyboardLayoutCursor _handleRemoteControlReceivedWithEvent:];
-[UIKeyboardLayoutCursor _handleWheelChangedWithEvent:];
-[UIKeyboardLayoutCursor _indexOfFirstKeyPassingTest:];
-[UIKeyboardLayoutCursor _isDirectionalHeading:];
-[UIKeyboardLayoutCursor _isKeyboardReverseOfAppLayoutDirection];
-[UIKeyboardLayoutCursor _keyplaneForKeyplaneProperties];
-[UIKeyboardLayoutCursor _logMajorToggleMissingCurrentKeyplane];
-[UIKeyboardLayoutCursor _menuTapShouldExitVariants];
-[UIKeyboardLayoutCursor _menuTapShouldStopDictation];
-[UIKeyboardLayoutCursor acceptRecentInputIfNecessary];
-[UIKeyboardLayoutCursor activeStateForKey:];
-[UIKeyboardLayoutCursor cacheTokenForKeyplane:];
-[UIKeyboardLayoutCursor clearVariantStateForKey:];
-[UIKeyboardLayoutCursor configureFloatingContentViewsIfNeeded];
-[UIKeyboardLayoutCursor cursorLocation];
-[UIKeyboardLayoutCursor deactivateKey:];
-[UIKeyboardLayoutCursor defaultCursorAdjustDistance];
-[UIKeyboardLayoutCursor defaultSelectedVariantIndexForKey:withActions:];
-[UIKeyboardLayoutCursor didSelectRecentInputString:];
-[UIKeyboardLayoutCursor downActionFlagsForKey:];
-[UIKeyboardLayoutCursor enabledStateForKey:];
-[UIKeyboardLayoutCursor endMultitapForKey:];
-[UIKeyboardLayoutCursor flushKeyCache:];
-[UIKeyboardLayoutCursor focusWindow];
-[UIKeyboardLayoutCursor getHandRestRecognizerState];
-[UIKeyboardLayoutCursor getNextKeyplaneIndex:];
-[UIKeyboardLayoutCursor getRomanAccentVariantsForString:inputMode:keyboardVariantIndludes:];
-[UIKeyboardLayoutCursor handleDidFinishDictation:];
-[UIKeyboardLayoutCursor handleLinearDirectionalInput:];
-[UIKeyboardLayoutCursor handleVariantDeleteIfNecessaryForKey:];
-[UIKeyboardLayoutCursor handleVisualDirectionalInput:];
-[UIKeyboardLayoutCursor ignoresShiftState];
-[UIKeyboardLayoutCursor isAppRightToLeft];
-[UIKeyboardLayoutCursor isKeyboardRightToLeft];
-[UIKeyboardLayoutCursor isKeyplaneDisabledWithName:];
-[UIKeyboardLayoutCursor isPossibleToTypeFast];
-[UIKeyboardLayoutCursor isSlimLinearKeyboardTV];
-[UIKeyboardLayoutCursor keyHitTestInSameRowAsCenter:size:];
-[UIKeyboardLayoutCursor keyplaneBeforeDictation];
-[UIKeyboardLayoutCursor lastSelectedKeyIndex];
-[UIKeyboardLayoutCursor overrideInitialKey];
-[UIKeyboardLayoutCursor recentInputsAlert];
-[UIKeyboardLayoutCursor refreshSelectedCellIfNecessaryForKey:];
-[UIKeyboardLayoutCursor refreshSelectedCellIfNecessaryForKey:animated:];
-[UIKeyboardLayoutCursor returnToKeyplaneAfterDictation];
-[UIKeyboardLayoutCursor runWithSuppressedActions:];
-[UIKeyboardLayoutCursor selectInitialKeyIfNecessary];
-[UIKeyboardLayoutCursor selectedKeyBeforeDictation];
-[UIKeyboardLayoutCursor selectionFrameForKeyIndex:];
-[UIKeyboardLayoutCursor setCursorLocation:];
-[UIKeyboardLayoutCursor setDisableTouchInput:];
-[UIKeyboardLayoutCursor setKeyboardName:appearance:];
-[UIKeyboardLayoutCursor setKeyplaneBeforeDictation:];
-[UIKeyboardLayoutCursor setLastSelectedKeyIndex:];
-[UIKeyboardLayoutCursor setOverrideInitialKey:];
-[UIKeyboardLayoutCursor setRecentInputs:];
-[UIKeyboardLayoutCursor setRecentInputsAlert:];
-[UIKeyboardLayoutCursor setSelectedKeyBeforeDictation:];
-[UIKeyboardLayoutCursor setSelectedKeyIndex:];
-[UIKeyboardLayoutCursor setShouldConfigureFloatingContentView:];
-[UIKeyboardLayoutCursor setShouldToggleLetterCaseNext:];
-[UIKeyboardLayoutCursor setSuppressOperations:];
-[UIKeyboardLayoutCursor shouldAllowCurrentKeyplaneReload];
-[UIKeyboardLayoutCursor shouldConfigureFloatingContentView];
-[UIKeyboardLayoutCursor shouldDeactivateWithoutWindow];
-[UIKeyboardLayoutCursor shouldMatchCaseForDomainKeys];
-[UIKeyboardLayoutCursor shouldPreventInputManagerHitTestingForKey:];
-[UIKeyboardLayoutCursor shouldRetestKey:slidOffKey:withKeyplane:];
-[UIKeyboardLayoutCursor shouldToggleKeyplaneWithName:];
-[UIKeyboardLayoutCursor shouldToggleLetterCaseNext];
-[UIKeyboardLayoutCursor showKeyboardWithInputTraits:screenTraits:splitTraits:];
-[UIKeyboardLayoutCursor showPopupKeyplaneSwitcher];
-[UIKeyboardLayoutCursor showRecentInputsAlert];
-[UIKeyboardLayoutCursor stateForCandidateListKey:];
-[UIKeyboardLayoutCursor stateForKeyplaneSwitchKey:];
-[UIKeyboardLayoutCursor supportsEmoji];
-[UIKeyboardLayoutCursor suppressOperations];
-[UIKeyboardLayoutCursor switchToDictationKeyplaneWithActivationIdentifier:];
-[UIKeyboardLayoutCursor takeKeyAction:];
-[UIKeyboardLayoutCursor targetEdgesForScreenGestureRecognition];
-[UIKeyboardLayoutCursor targetKeyIndexFromPoint:];
-[UIKeyboardLayoutCursor updateDictationHelpString];
-[UIKeyboardLayoutCursor updateKeyplaneSwitchEdgeBiases];
-[UIKeyboardLayoutCursor updateRecentInputsKeyIfNecessary];
-[UIKeyboardLayoutCursor variantCountForKey:];
```
