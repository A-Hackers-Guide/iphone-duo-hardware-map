# `UIKeyboardPreferencesController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 7 properties, 57 instance methods, 1 class methods

## Properties

```
@property (TB,R,N) _shouldUseModifiedHitArea;
@property (TB,R,N) _shouldShowDebugHitArea;
@property (T@"UIKeyboardPreferencesController<TIPreferencesControllerActions>",R,N) preferencesActions;
@property (Tq) handBias;
@property (Tq) compactAssistantBarPersistentLocation;
@property (Tq) visceral;
@property (TB) enableProKeyboard;
```

## Class methods

```
+[UIKeyboardPreferencesController sharedPreferencesController];
```

## Instance methods

```
-[UIKeyboardPreferencesController handBias];
-[UIKeyboardPreferencesController isPreferenceKeyLockedDown:];
-[UIKeyboardPreferencesController _configurePreferences];
-[UIKeyboardPreferencesController isDictationAsPrimaryInputMode];
-[UIKeyboardPreferencesController synchronizePreferences];
-[UIKeyboardPreferencesController crescendoEnabled];
-[UIKeyboardPreferencesController setHandBias:];
-[UIKeyboardPreferencesController boolForPreferenceKey:];
-[UIKeyboardPreferencesController currentInputModeSupportsCrescendo];
-[UIKeyboardPreferencesController isPasswordAutoFillAllowed];
-[UIKeyboardPreferencesController valueForPreferenceKey:];
-[UIKeyboardPreferencesController touchSynchronizePreferencesTimer];
-[UIKeyboardPreferencesController setValue:forPreferenceKey:];
-[UIKeyboardPreferencesController valueForPreferenceKey:forceUpdate:];
-[UIKeyboardPreferencesController preferencesControllerChanged:];
-[UIKeyboardPreferencesController boolForKey:];
-[UIKeyboardPreferencesController allEnabledInputModesAreValid];
-[UIKeyboardPreferencesController setVisceral:];
-[UIKeyboardPreferencesController inputModeUpdateTime];
-[UIKeyboardPreferencesController useHardwareGlobeKeyAsEmojiKey];
-[UIKeyboardPreferencesController init];
-[UIKeyboardPreferencesController useDynamicEmojiKeyplaneEnabled];
-[UIKeyboardPreferencesController spaceConfirmationEnabled];
-[UIKeyboardPreferencesController compactAssistantBarPersistentLocation];
-[UIKeyboardPreferencesController inputModeSupportsCrescendo:];
-[UIKeyboardPreferencesController dealloc];
-[UIKeyboardPreferencesController _shouldUseModifiedHitArea];
-[UIKeyboardPreferencesController setLastUsedDictationLanguages:];
-[UIKeyboardPreferencesController colorAdaptiveKeyboardBackdropEnabled];
-[UIKeyboardPreferencesController setValue:forKey:];
-[UIKeyboardPreferencesController setCompactAssistantBarPersistentLocation:];
-[UIKeyboardPreferencesController colorAdaptiveKeyboardEnabled];
-[UIKeyboardPreferencesController _shouldShowDebugHitArea];
-[UIKeyboardPreferencesController valueForKey:];
-[UIKeyboardPreferencesController showSensitiveUI];
-[UIKeyboardPreferencesController keyboardLanguageIndicatorEnabled];
-[UIKeyboardPreferencesController setEnabledDictationLanguages:];
-[UIKeyboardPreferencesController setEnableProKeyboard:];
-[UIKeyboardPreferencesController inputModeSupportsCrescendo:screenTraits:];
-[UIKeyboardPreferencesController preferencesActions];
-[UIKeyboardPreferencesController crescendo50OnLayoutsEnabled];
-[UIKeyboardPreferencesController rivenSizeFactor:];
-[UIKeyboardPreferencesController setLanguageAwareInputModeLastUsed:];
-[UIKeyboardPreferencesController methodSignatureForSelector:];
-[UIKeyboardPreferencesController inputModeSupportsCrescendo:screenTraits:keyboardType:];
-[UIKeyboardPreferencesController numPadNameForInputMode:keyboardType:];
-[UIKeyboardPreferencesController isFirstReachableKeyboardInteraction];
-[UIKeyboardPreferencesController sb_defaults];
-[UIKeyboardPreferencesController performedFirstReachableKeyboardInteraction];
-[UIKeyboardPreferencesController defaultGlobeAsEmojiKeySetting];
-[UIKeyboardPreferencesController respondsToSelector:];
-[UIKeyboardPreferencesController setDictationAutoPunctuation:];
-[UIKeyboardPreferencesController setDictationAsPrimaryInputMode:];
-[UIKeyboardPreferencesController forwardInvocation:];
-[UIKeyboardPreferencesController enableProKeyboard];
-[UIKeyboardPreferencesController saveInputModes:];
-[UIKeyboardPreferencesController visceral];
```
