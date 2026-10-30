# `UIKeyboardInputMode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInputMode`
- Protocols: `NSCopying`
- 15 instance variables, 44 properties, 92 instance methods, 10 class methods

## Instance variables

```
B isDisplayed;
B _extensionInputModeHasDictation;
B _isActiveDictationInputInMultilingualKeyboard;
@"NSString" _primaryLanguage;
@"NSString" _languageWithRegion;
@"NSString" identifier;
@"NSString" normalizedIdentifier;
@"NSString" softwareLayout;
@"NSString" hardwareLayout;
@"NSArray" _multilingualLanguages;
@"NSString" _variant;
@"NSString" _defaultDictationLanguage;
@"UIImage" _cachedIcon;
Q _cachedIconKey;
@"NSString" _cachedSizeCategory;
```

## Properties

```
@property (T@"NSString",&,N,Videntifier) identifier;
@property (T@"NSString",&,N,VnormalizedIdentifier) normalizedIdentifier;
@property (T@"NSString",&,N,V_languageWithRegion) languageWithRegion;
@property (T@"NSString",&,N,V_variant) variant;
@property (T@"NSString",&,N,VsoftwareLayout) softwareLayout;
@property (T@"NSString",&,N,VhardwareLayout) hardwareLayout;
@property (T@"NSArray",&,N,V_multilingualLanguages) multilingualLanguages;
@property (T@"UIImage",&,N,V_cachedIcon) cachedIcon;
@property (TQ,N,V_cachedIconKey) cachedIconKey;
@property (T@"NSString",&,N,V_cachedSizeCategory) cachedSizeCategory;
@property (T@"NSString",R,N) identifierWithLayouts;
@property (T@"NSString",&,N,V_primaryLanguage) primaryLanguage;
@property (T@"NSString",R,N) automaticHardwareLayout;
@property (TB,R,N) showSWLayoutWithHWKeyboard;
@property (T@"NSArray",R,N) normalizedIdentifierLevels;
@property (T@"NSString",R,N) displayName;
@property (T@"NSString",R,N) extendedDisplayName;
@property (TB,R,N) isDefaultRightToLeft;
@property (TB,R,N) defaultLayoutIsASCIICapable;
@property (TB,R,N) isExtensionInputMode;
@property (TB,R,N) isStalledExtensionInputMode;
@property (TB,N,V_extensionInputModeHasDictation) extensionInputModeHasDictation;
@property (T@"NSExtension",R,N) extension;
@property (T@"NSBundle",R,N) containingBundle;
@property (T@"NSString",R,N) containingBundleDisplayName;
@property (TB,N,VisDisplayed) isDisplayed;
@property (TB,R,N) isSpecializedInputMode;
@property (TB,R,N) isEmojiInputMode;
@property (TB,R,N) isHandwritingInputMode;
@property (TB,R,N) supportsEmojiSearch;
@property (T@"NSString",&,N) dictationLanguage;
@property (T@"NSString",R,N) dictationDisplayName;
@property (T@"NSString",&,N,V_defaultDictationLanguage) defaultDictationLanguage;
@property (T@"NSString",R,N) monolingualDisplayName;
@property (T@"NSLocale",R,N) locale;
@property (TB,R,N,GisMultilingual) multilingual;
@property (TB,R,N,GisMultiscript) multiscript;
@property (T@"NSArray",R,N) multilingualSet;
@property (T@"NSArray",R,N) multiscriptSet;
@property (TQ,R,N) multilingualIndex;
@property (TQ,R,N) multiscriptIndex;
@property (TB,R,N,GisMultilingualOnly) multilingualOnly;
@property (TB,R,N) showsTransliterationCandidates;
@property (TB,N,V_isActiveDictationInputInMultilingualKeyboard) isActiveDictationInputInMultilingualKeyboard;
```

## Class methods

```
+[UIKeyboardInputMode supportsSecureCoding];
+[UIKeyboardInputMode autofillSignupInputMode];
+[UIKeyboardInputMode canonicalLanguageIdentifierFromIdentifier:];
+[UIKeyboardInputMode multilingualSetsFromInputModeIdentifiers:];
+[UIKeyboardInputMode keyboardInputModeWithIdentifier:];
+[UIKeyboardInputMode intlInputMode];
+[UIKeyboardInputMode dictationInputMode];
+[UIKeyboardInputMode softwareLayoutFromIdentifier:];
+[UIKeyboardInputMode hardwareLayoutFromIdentifier:];
+[UIKeyboardInputMode _displayNameForMultilingualSet:forDisplayInLists:usingDeviceLanguage:context:];
```

## Instance methods

```
-[UIKeyboardInputMode preferencesControllerChanged:];
-[UIKeyboardInputMode setVariant:];
-[UIKeyboardInputMode primaryLanguage];
-[UIKeyboardInputMode identifier];
-[UIKeyboardInputMode hardwareLayout];
-[UIKeyboardInputMode displayName];
-[UIKeyboardInputMode dealloc];
-[UIKeyboardInputMode includeBarHeight];
-[UIKeyboardInputMode softwareLayout];
-[UIKeyboardInputMode languageWithRegion];
-[UIKeyboardInputMode isMultilingual];
-[UIKeyboardInputMode showSWLayoutWithHWKeyboard];
-[UIKeyboardInputMode setIdentifier:];
-[UIKeyboardInputMode locale];
-[UIKeyboardInputMode multilingualLanguages];
-[UIKeyboardInputMode encodeWithCoder:];
-[UIKeyboardInputMode normalizedIdentifier];
-[UIKeyboardInputMode initWithCoder:];
-[UIKeyboardInputMode extension];
-[UIKeyboardInputMode setMultilingualLanguages:];
-[UIKeyboardInputMode setPrimaryLanguage:];
-[UIKeyboardInputMode copyWithZone:];
-[UIKeyboardInputMode isEqual:];
-[UIKeyboardInputMode initWithIdentifier:];
-[UIKeyboardInputMode variant];
-[UIKeyboardInputMode multilingualSet];
-[UIKeyboardInputMode multiscriptInputModeIdentifiers];
-[UIKeyboardInputMode setIsDisplayed:];
-[UIKeyboardInputMode _fallbackIconLabel];
-[UIKeyboardInputMode _getIconLabel:secondaryIconLabel:];
-[UIKeyboardInputMode _getIconLabel:secondaryIconLabel:artwork:];
-[UIKeyboardInputMode _getIconLabel:secondaryIconLabel:artwork:inputModes:];
-[UIKeyboardInputMode _iconLabelComponentsForMultilingualSet];
-[UIKeyboardInputMode _iconLabelForMultilingualSet];
-[UIKeyboardInputMode _iconLabelWithinMultiscriptSet];
-[UIKeyboardInputMode _indicatorIconWithConfiguration:];
-[UIKeyboardInputMode automaticHardwareLayout];
-[UIKeyboardInputMode cachedIcon];
-[UIKeyboardInputMode cachedIconKey];
-[UIKeyboardInputMode cachedSizeCategory];
-[UIKeyboardInputMode containingBundle];
-[UIKeyboardInputMode containingBundleDisplayName];
-[UIKeyboardInputMode cursorAccessoryIcon];
-[UIKeyboardInputMode defaultDictationLanguage];
-[UIKeyboardInputMode defaultLayoutIsASCIICapable];
-[UIKeyboardInputMode dictationDisplayName];
-[UIKeyboardInputMode dictationLanguage];
-[UIKeyboardInputMode drawStringInRect:inRect:useSmallFont:useCondensedFont:scale:];
-[UIKeyboardInputMode extendedDisplayName];
-[UIKeyboardInputMode extensionInputModeHasDictation];
-[UIKeyboardInputMode identifierWithLayouts];
-[UIKeyboardInputMode imageForInputModeLabel:secondaryIconLabel:artwork:withConfiguration:];
-[UIKeyboardInputMode indicatorIcon];
-[UIKeyboardInputMode indicatorIconForSoftwareLayout];
-[UIKeyboardInputMode indicatorTextIcon];
-[UIKeyboardInputMode isActiveDictationInputInMultilingualKeyboard];
-[UIKeyboardInputMode isAllowedForTraits:];
-[UIKeyboardInputMode isDefaultRightToLeft];
-[UIKeyboardInputMode isDesiredForTraits:];
-[UIKeyboardInputMode isDesiredForTraits:withExtended:];
-[UIKeyboardInputMode isDisplayed];
-[UIKeyboardInputMode isEmojiInputMode];
-[UIKeyboardInputMode isExtensionInputMode];
-[UIKeyboardInputMode isHandwritingInputMode];
-[UIKeyboardInputMode isMultilingualOnly];
-[UIKeyboardInputMode isMultiscript];
-[UIKeyboardInputMode isSpecializedInputMode];
-[UIKeyboardInputMode isStalledExtensionInputMode];
-[UIKeyboardInputMode languageIndicatorScale];
-[UIKeyboardInputMode largeCursorAccessoryIcon];
-[UIKeyboardInputMode monolingualDisplayName];
-[UIKeyboardInputMode multilingualIndex];
-[UIKeyboardInputMode multilingualInputModeIdentifiers];
-[UIKeyboardInputMode multilingualSetFromInputModeIdentifiers:];
-[UIKeyboardInputMode multiscriptIndex];
-[UIKeyboardInputMode multiscriptSet];
-[UIKeyboardInputMode normalizedIdentifierLevels];
-[UIKeyboardInputMode setCachedIcon:];
-[UIKeyboardInputMode setCachedIconKey:];
-[UIKeyboardInputMode setCachedSizeCategory:];
-[UIKeyboardInputMode setCurrentInputModeToActiveInputModeForMultilingualKeyboardForDictation];
-[UIKeyboardInputMode setDefaultDictationLanguage:];
-[UIKeyboardInputMode setDictationLanguage:];
-[UIKeyboardInputMode setExtensionInputModeHasDictation:];
-[UIKeyboardInputMode setHardwareLayout:];
-[UIKeyboardInputMode setIsActiveDictationInputInMultilingualKeyboard:];
-[UIKeyboardInputMode setLanguageWithRegion:];
-[UIKeyboardInputMode setLastUsedDictationLanguage];
-[UIKeyboardInputMode setNormalizedIdentifier:];
-[UIKeyboardInputMode setSoftwareLayout:];
-[UIKeyboardInputMode showsTransliterationCandidates];
-[UIKeyboardInputMode supportsEmojiSearch];
```
