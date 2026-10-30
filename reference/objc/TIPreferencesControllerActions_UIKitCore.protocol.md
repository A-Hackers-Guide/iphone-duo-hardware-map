# `TIPreferencesControllerActions` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 42 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",C,N) inputModeSelectionSequence;
@property (TB,N) predictionEnabled;
@property (TB,N) autocorrectionEnabled;
@property (TB,N) automaticMinimizationEnabled;
@property (TB,R,N) alwaysShowOnscreenKeyboardEnabled;
@property (TB,N) keyboardShownByTouch;
@property (T{CGPoint=dd},N) keyboardPosition;
@property (T{CGPoint=dd},N) floatingKeyboardPosition;
@property (TQ,N) floatingKeyboardDockedEdge;
@property (TB,N) shouldSplitInSplitPreferringContext;
@property (TB,N) shouldSplitInDefaultContext;
```

## Instance methods

```
-[TIPreferencesControllerActions autocorrectionEnabled];
-[TIPreferencesControllerActions updateDidPerformFirstReachableKeyboardInteraction];
-[TIPreferencesControllerActions setKeyboardPosition:];
-[TIPreferencesControllerActions updateVisceral:];
-[TIPreferencesControllerActions updateDictationTipDisplayCount:dictationTipKey:];
-[TIPreferencesControllerActions predictionEnabled];
-[TIPreferencesControllerActions keyboardPosition];
-[TIPreferencesControllerActions shouldSplitInDefaultContext];
-[TIPreferencesControllerActions setAutomaticMinimizationEnabled:];
-[TIPreferencesControllerActions setPredictionEnabled:];
-[TIPreferencesControllerActions didTriggerOneTimeAction:];
-[TIPreferencesControllerActions updateKeyboardIsSplit:locked:];
-[TIPreferencesControllerActions updateLastUsedDictationLanguages:];
-[TIPreferencesControllerActions updateLastUsedKeyboards:];
-[TIPreferencesControllerActions updateDictationTipLastShownDate:];
-[TIPreferencesControllerActions keyboardShownByTouch];
-[TIPreferencesControllerActions automaticMinimizationEnabled];
-[TIPreferencesControllerActions floatingKeyboardDockedEdge];
-[TIPreferencesControllerActions inputModeSelectionSequence];
-[TIPreferencesControllerActions floatingKeyboardPosition];
-[TIPreferencesControllerActions resetDictationTipsToDefaultSettings];
-[TIPreferencesControllerActions setKeyboardShownByTouch:];
-[TIPreferencesControllerActions setShouldSplitInSplitPreferringContext:];
-[TIPreferencesControllerActions updateKeyboardIsFloating:];
-[TIPreferencesControllerActions updateLastUsedLayout:];
-[TIPreferencesControllerActions setInputModeSelectionSequence:];
-[TIPreferencesControllerActions updateDictationAutoPunctuation:];
-[TIPreferencesControllerActions alwaysShowOnscreenKeyboardEnabled];
-[TIPreferencesControllerActions updateLastUsedInputMode:];
-[TIPreferencesControllerActions setFloatingKeyboardDockedEdge:];
-[TIPreferencesControllerActions updateEnableProKeyboard:];
-[TIPreferencesControllerActions setFloatingKeyboardPosition:];
-[TIPreferencesControllerActions updateIndicatorLastShownDate:];
-[TIPreferencesControllerActions updateEnabledDictationLanguages:];
-[TIPreferencesControllerActions shouldSplitInSplitPreferringContext];
-[TIPreferencesControllerActions oneTimeActionCompleted:];
-[TIPreferencesControllerActions updateKeyboardHandBias:];
-[TIPreferencesControllerActions updateLastUsedDictionaryLanguageInMultilingualKeyboard:activeDictationlanguage:];
-[TIPreferencesControllerActions updateCompactAssistantBarPersistentLocation:];
-[TIPreferencesControllerActions updateDictationAsPrimaryInputMode:];
-[TIPreferencesControllerActions setShouldSplitInDefaultContext:];
-[TIPreferencesControllerActions setAutocorrectionEnabled:];
```
