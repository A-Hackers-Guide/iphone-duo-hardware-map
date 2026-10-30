# `UITextChecker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 50 instance methods, 31 class methods

## Instance variables

```
q _usdt;
@"NSString" _checkerWarmingLanguage;
```

## Properties

```
@property (T@"NSArray",&,N) ignoredWords;
```

## Class methods

```
+[UITextChecker handleGrammarCorrectionEntries:];
+[UITextChecker grammarAutocorrectionForWord:];
+[UITextChecker _isWord:inDictionary:];
+[UITextChecker _setDictionaryEntry:forName:];
+[UITextChecker noteWordTerminator:replacement:];
+[UITextChecker createDictHashTable:];
+[UITextChecker bestLanguageForString:fromAlternatives:currentLanguage:insertionPointIndex:scriptForBestLanguage:];
+[UITextChecker bestLanguageForString:fromAlternatives:currentLanguage:];
+[UITextChecker proofreadingSuggestionForTextAlternatives:client:range:detail:];
+[UITextChecker grammarCheckingEnabled];
+[UITextChecker openUserDictionary:];
+[UITextChecker hasLearnedWord:];
+[UITextChecker unlearnWord:];
+[UITextChecker proofreadingSuggestionsEnabled];
+[UITextChecker noteTextReplacement:];
+[UITextChecker _setWords:inDictionary:];
+[UITextChecker uniqueSpellDocumentTag];
+[UITextChecker keyboardLanguages];
+[UITextChecker setProofreadingSuggestionForRange:originalString:replacementString:category:userDescription:detail:textAlternatives:];
+[UITextChecker setString:isExemptFromChecker:];
+[UITextChecker learnWord:];
+[UITextChecker _forgetWord:inDictionary:];
+[UITextChecker suggestionForRange:originalString:detail:];
+[UITextChecker _wordsInDictionary:];
+[UITextChecker performFinalGrammarChecking];
+[UITextChecker _learnWord:inDictionary:];
+[UITextChecker _dictionaryEntryForName:];
+[UITextChecker availableLanguages];
+[UITextChecker dictionaryInfo:];
+[UITextChecker postEditor];
+[UITextChecker grammarCheckingEnabledForLanguage:];
```

## Instance methods

```
-[UITextChecker nonIgnoredGrammarCheckingResultForResult:string:];
-[UITextChecker requestGrammarCheckingOfString:range:waitForAllResults:completionHandler:];
-[UITextChecker _setDocumentDictionaryName:];
-[UITextChecker rangeOfMisspelledWordInString:range:startingAt:wrap:languages:];
-[UITextChecker checkSpellingOfString:startingAt:language:wrap:correction:];
-[UITextChecker _filteredGrammarCheckingResultsForResults:string:];
-[UITextChecker correctionForWordRange:inString:language:];
-[UITextChecker releaseAllLexicons];
-[UITextChecker init];
-[UITextChecker adjustOffsetToNextWordBoundaryInString:startingAt:];
-[UITextChecker _doneLoading];
-[UITextChecker ignoredWords];
-[UITextChecker dealloc];
-[UITextChecker requestProofreadingReviewOfString:range:language:options:completionHandler:];
-[UITextChecker checkGrammarOfString:startingAt:language:wrap:details:];
-[UITextChecker recordResponse:toGrammarDetail:language:];
-[UITextChecker requestResultOptionsForDetail:completionHandler:];
-[UITextChecker alternativesForPinyinInputString:];
-[UITextChecker initUserDictionaries];
-[UITextChecker extendedGrammarAlternativesForString:context:rangeInContext:];
-[UITextChecker initGlobalsWithAsynchronousLoading:];
-[UITextChecker setIgnoredWords:];
-[UITextChecker suggestWordInLanguage:];
-[UITextChecker initPostEditingWithAsynchronousLoading:];
-[UITextChecker _setLanguageDictionaryName:];
-[UITextChecker ignoreGrammarCheckingResultsForWord:grammarString:detail:];
-[UITextChecker requestGrammarCheckingOfString:range:language:options:completionHandler:];
-[UITextChecker isWordInUserDictionaries:caseSensitive:];
-[UITextChecker ignoreGrammarRange:inSentence:];
-[UITextChecker guessesForWordRange:inString:language:];
-[UITextChecker _nameOfDictionaryForDocumentTag:];
-[UITextChecker _chunkAndCheckGrammarInString:language:usingChecker:details:];
-[UITextChecker checkString:range:types:languages:options:];
-[UITextChecker checkSpellingOfString:startingAt:languages:wrap:correction:];
-[UITextChecker grammarGuessesForRange:inString:language:];
-[UITextChecker stringForInputString:language:];
-[UITextChecker completionsForPartialWordRange:inString:language:];
-[UITextChecker grammarAlternativesForString:];
-[UITextChecker canChangeCaseOfFirstLetterInString:toUpperCase:language:];
-[UITextChecker finalResultsFromCheckingString:range:language:options:];
-[UITextChecker ignoreWord:];
-[UITextChecker resetAllLanguageModels];
-[UITextChecker postEditor];
-[UITextChecker _checker];
-[UITextChecker proofreadingGuessForString:];
-[UITextChecker recordResponse:toGrammarDetailInAnnotatedString:range:];
-[UITextChecker _initWithAsynchronousLoading:];
-[UITextChecker _chunkAndFindMisspelledWordInString:languages:learnedDictionaries:wordCount:correction:usingChecker:];
-[UITextChecker _grammarAlternativesForString:allowExtended:context:rangeInContext:];
-[UITextChecker rangeOfMisspelledWordInString:range:startingAt:wrap:language:];
```
