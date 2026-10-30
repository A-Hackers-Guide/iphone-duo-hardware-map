# `PKTextInputLanguageSelectionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputLanguageSelectionTokenStore`
- 6 instance variables, 10 properties, 28 instance methods, 28 class methods

## Instance variables

```
@"UIMenu" _cachedLanguageMenu;
@"NSMutableDictionary" _observers;
@"NSTimer" _iconDisplayTimer;
@"NSHashTable" _languageSelectionControllerObservers;
@"NSArray" __cachedLanguageIdentifiers;
@"NSArray" __cachedLanguageIdentifiersForEmojiAlternatives;
```

## Properties

```
@property (T@"NSArray",C,N,V__cachedLanguageIdentifiers) _cachedLanguageIdentifiers;
@property (T@"NSArray",C,N,V__cachedLanguageIdentifiersForEmojiAlternatives) _cachedLanguageIdentifiersForEmojiAlternatives;
@property (T@"NSArray",R,C,N) currentLanguageIdentifiers;
@property (T@"NSArray",R,C,N) currentLanguageIdentifiersForEmojiAlternatives;
@property (T@"UIImage",R,N) languageIdentificationIcon;
@property (T@"UIMenu",R,N) languageSelectionMenu;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputLanguageSelectionController sharedInstance];
+[PKTextInputLanguageSelectionController activeInputModes];
+[PKTextInputLanguageSelectionController _additionalLocaleIdentifiersForIdentifier:excludingIdentifiers:];
+[PKTextInputLanguageSelectionController _getNormalizedLanguageIdentifier:dedupLanguageKey:forInputMode:];
+[PKTextInputLanguageSelectionController _preferencesLanguagesForTesting];
+[PKTextInputLanguageSelectionController _additionalLocaleRules];
+[PKTextInputLanguageSelectionController _currentLanguageIdentifiersForEmojiAlternatives];
+[PKTextInputLanguageSelectionController _englishFilteringRules];
+[PKTextInputLanguageSelectionController _enumerateSupportedAndEnabledLocaleIdentifiersWithBlock:];
+[PKTextInputLanguageSelectionController _filterEnglishWithLanguages:outRemapTarget:];
+[PKTextInputLanguageSelectionController _getNormalizedLanguageIdentifier:dedupLanguageKey:forInputMode:mappingYueToZh:];
+[PKTextInputLanguageSelectionController _getNormalizedLanguageIdentifier:dedupLanguageKey:forInputModeIdentifier:];
+[PKTextInputLanguageSelectionController _getNormalizedLanguageIdentifier:dedupLanguageKey:forInputModeIdentifier:mappingYueToZh:];
+[PKTextInputLanguageSelectionController _inputModesForTesting];
+[PKTextInputLanguageSelectionController _performOperations:withActiveInputModeIdentifiers:preferencesLanguages:preferredLanguages:];
+[PKTextInputLanguageSelectionController _performOperations:withActiveInputModes:preferencesLanguages:preferredLanguages:];
+[PKTextInputLanguageSelectionController _preferredLanguagesForTesting];
+[PKTextInputLanguageSelectionController _preferredRecognitionLocaleIdentifierFromIdentifiers:];
+[PKTextInputLanguageSelectionController _scriptQualifiedLocaleIdentifiers];
+[PKTextInputLanguageSelectionController _sortedStringsArray:withArray:];
+[PKTextInputLanguageSelectionController _transliterationInputModeRules];
+[PKTextInputLanguageSelectionController _unfilteredSupportedAndEnabledLocaleIdentifiers];
+[PKTextInputLanguageSelectionController filteredEnabledLocaleIdentifiers];
+[PKTextInputLanguageSelectionController hasSomeSupportedAndEnabledLocale];
+[PKTextInputLanguageSelectionController set_inputModesForTesting:];
+[PKTextInputLanguageSelectionController set_preferencesLanguagesForTesting:];
+[PKTextInputLanguageSelectionController set_preferredLanguagesForTesting:];
+[PKTextInputLanguageSelectionController supportedAndEnabledLocaleIdentifiers];
```

## Instance methods

```
-[PKTextInputLanguageSelectionController removeObserver:];
-[PKTextInputLanguageSelectionController init];
-[PKTextInputLanguageSelectionController dealloc];
-[PKTextInputLanguageSelectionController addObserver:];
-[PKTextInputLanguageSelectionController registerObserver:];
-[PKTextInputLanguageSelectionController _updateWithLanguageIdentifiers:];
-[PKTextInputLanguageSelectionController _cachedLanguageIdentifiers];
-[PKTextInputLanguageSelectionController _cachedLanguageIdentifiersForEmojiAlternatives];
-[PKTextInputLanguageSelectionController _clearCachesAndUpdateIconObservers];
-[PKTextInputLanguageSelectionController _currentKeyboardIdentifier];
-[PKTextInputLanguageSelectionController _enabledLanguagesByPreference];
-[PKTextInputLanguageSelectionController _handleKeyboardCurrentInputModeChanged:];
-[PKTextInputLanguageSelectionController _handleKeyboardPreferencesChanged:];
-[PKTextInputLanguageSelectionController _iconForLanguageIdentifier:];
-[PKTextInputLanguageSelectionController _notifyLanguageSelectionDidChange];
-[PKTextInputLanguageSelectionController _pencilPreferencesChangedCallback:];
-[PKTextInputLanguageSelectionController _switchToLanguageIfSupported:];
-[PKTextInputLanguageSelectionController _updateLanguageMenuIfNecessary];
-[PKTextInputLanguageSelectionController _updateSelectedLanguageInCachedMenu];
-[PKTextInputLanguageSelectionController currentLanguageIdentifiers];
-[PKTextInputLanguageSelectionController currentLanguageIdentifiersForEmojiAlternatives];
-[PKTextInputLanguageSelectionController ensureKeyboardLanguageConsistencyIfNeededWhileWriting:];
-[PKTextInputLanguageSelectionController languageIdentificationIcon];
-[PKTextInputLanguageSelectionController languageSelectionMenu];
-[PKTextInputLanguageSelectionController notifyLanguageDidChange];
-[PKTextInputLanguageSelectionController set_cachedLanguageIdentifiers:];
-[PKTextInputLanguageSelectionController set_cachedLanguageIdentifiersForEmojiAlternatives:];
-[PKTextInputLanguageSelectionController shouldIdentifyLanguages];
```
