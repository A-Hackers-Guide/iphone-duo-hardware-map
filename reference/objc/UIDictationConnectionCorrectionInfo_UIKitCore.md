# `UIDictationConnectionCorrectionInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _alternativeSelectionCount;
i _characterModificationCount;
i _characterInsertionCount;
i _characterDeletionCount;
i _characterSubstitutionCount;
@"NSString" _correctedText;
@"NSDictionary" _recognizedTextInfo;
@"NSDictionary" _userEditedTextInfo;
@"NSArray" _selectedAlternativesInfo;
```

## Properties

```
@property (Ti,N,V_alternativeSelectionCount) alternativeSelectionCount;
@property (Ti,N,V_characterModificationCount) characterModificationCount;
@property (Ti,N,V_characterInsertionCount) characterInsertionCount;
@property (Ti,N,V_characterDeletionCount) characterDeletionCount;
@property (Ti,N,V_characterSubstitutionCount) characterSubstitutionCount;
@property (T@"NSString",C,N,V_correctedText) correctedText;
@property (T@"NSDictionary",C,N,V_recognizedTextInfo) recognizedTextInfo;
@property (T@"NSDictionary",C,N,V_userEditedTextInfo) userEditedTextInfo;
@property (T@"NSArray",C,N,V_selectedAlternativesInfo) selectedAlternativesInfo;
```

## Instance methods

```
-[UIDictationConnectionCorrectionInfo alternativeSelectionCount];
-[UIDictationConnectionCorrectionInfo characterDeletionCount];
-[UIDictationConnectionCorrectionInfo characterInsertionCount];
-[UIDictationConnectionCorrectionInfo characterModificationCount];
-[UIDictationConnectionCorrectionInfo characterSubstitutionCount];
-[UIDictationConnectionCorrectionInfo correctedText];
-[UIDictationConnectionCorrectionInfo recognizedTextInfo];
-[UIDictationConnectionCorrectionInfo selectedAlternativesInfo];
-[UIDictationConnectionCorrectionInfo setAlternativeSelectionCount:];
-[UIDictationConnectionCorrectionInfo setCharacterDeletionCount:];
-[UIDictationConnectionCorrectionInfo setCharacterInsertionCount:];
-[UIDictationConnectionCorrectionInfo setCharacterModificationCount:];
-[UIDictationConnectionCorrectionInfo setCharacterSubstitutionCount:];
-[UIDictationConnectionCorrectionInfo setCorrectedText:];
-[UIDictationConnectionCorrectionInfo setRecognizedTextInfo:];
-[UIDictationConnectionCorrectionInfo setSelectedAlternativesInfo:];
-[UIDictationConnectionCorrectionInfo setUserEditedTextInfo:];
-[UIDictationConnectionCorrectionInfo userEditedTextInfo];
```
