# `UIDictationUtilities`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 56 class methods

## Class methods

```
+[UIDictationUtilities maxLoggableLengthOfInsertionWithoutDeletion:];
+[UIDictationUtilities _remapDictationLocaleFromLanguage:];
+[UIDictationUtilities _isDictationAssetAvailableForCurrentInputModeDictationLanguage];
+[UIDictationUtilities needsLeadingSpaceForText:secureInput:];
+[UIDictationUtilities activeMultilingualKeyboardDictationMappings];
+[UIDictationUtilities needsTrailingSpaceForText:secureInput:];
+[UIDictationUtilities attributedStringForDictationResult:andCorrectionIdentifier:capturePrefixAndPostfixWordCount:];
+[UIDictationUtilities phraseFromAFPhrase:];
+[UIDictationUtilities dictationPhrasesFromPhraseArray:];
+[UIDictationUtilities updateCharacterDeletionCount:delta:];
+[UIDictationUtilities logSpeechAlternativeReplacement:originalText:replacementText:index:];
+[UIDictationUtilities interpretationFromAFInterpretation:];
+[UIDictationUtilities trackSubstitution:originalText:originalTextRange:replacementText:replacementTextRange:];
+[UIDictationUtilities shouldAddDeleteMenuElement];
+[UIDictationUtilities trackingPunctuations];
+[UIDictationUtilities rangesForSearchStringWithWordBoundariesValidation:substring:reverse:];
+[UIDictationUtilities utilizeInputContextHistory];
+[UIDictationUtilities searchStringWithWordBoundariesValidation:substring:reverse:];
+[UIDictationUtilities updateCharacterModificationCount:delta:];
+[UIDictationUtilities maxLoggableLengthOfInsertionWithDeletion:];
+[UIDictationUtilities updateCharacterInsertionCount:delta:];
+[UIDictationUtilities metadataDictionaryForCorrectionIdentifier:];
+[UIDictationUtilities characterDeletionCount:];
+[UIDictationUtilities _isDictationAssetAvailableForLocale:];
+[UIDictationUtilities _isAutomaticKeyboardDownDictationDisabled];
+[UIDictationUtilities needsLeadingSpaceForPhrases:secureInput:];
+[UIDictationUtilities capitalizeFirstWord:];
+[UIDictationUtilities _properNameForString:];
+[UIDictationUtilities supportsDictationVoiceEditingUIForBundleIdentifier:];
+[UIDictationUtilities dictationPhrasesFromTokenMatrix:];
+[UIDictationUtilities interpretationFromAFTokens:];
+[UIDictationUtilities _unsupportedAppsForVoiceEditing];
+[UIDictationUtilities bestInterpretationForDictationResult:];
+[UIDictationUtilities trackDeletion:text:range:];
+[UIDictationUtilities searchString:contextBefore:contextAfter:completionHandler:];
+[UIDictationUtilities setActiveMultilingualKeyboardDictationMappings:activeDictationlanguage:];
+[UIDictationUtilities updateCharacterSubstitutionCount:delta:];
+[UIDictationUtilities tokenFromAFToken:];
+[UIDictationUtilities _normalizeToSpeechString:];
+[UIDictationUtilities selectionStartInfoWithBlock:];
+[UIDictationUtilities bestInterpretationForPhrases:];
+[UIDictationUtilities voiceCommandParameterFromAFVoiceCommandGrammarParamMatch:];
+[UIDictationUtilities shouldLogCorrectionInfoForCurrentBundleId];
+[UIDictationUtilities trackInsertion:text:range:];
+[UIDictationUtilities shouldInsertSpaceBetweenStringA:andStringB:];
+[UIDictationUtilities characterInsertionCount:];
+[UIDictationUtilities isSendRelatedKeyboardShortcut:];
+[UIDictationUtilities needsLeadingSpaceForText:secureInput:previousCharacter:selectionStartIsStartOfParagraph:];
+[UIDictationUtilities applySmartPunctuationToString:];
+[UIDictationUtilities needsTrailingSpaceForPhrases:secureInput:];
+[UIDictationUtilities attributedString:withIdentifiersBlock:];
+[UIDictationUtilities maxLoggableLengthOfInsertionBySubstitution:];
+[UIDictationUtilities dictationVoiceCommandParametersFromAFVoiceCommandGrammarParseCandidate:];
+[UIDictationUtilities characterSubstitutionCount:];
+[UIDictationUtilities _isUsingLargeFormatDictationUI];
+[UIDictationUtilities localizedDictationHelpMessageStringForKeyboardType:isSpelling:dictationLanguage:interfaceLanguage:enabledDictationLanguagesCount:];
```
