# `PKTextInputDebugLogEntry`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 16 properties, 37 instance methods, 5 class methods

## Instance variables

```
@"PKDrawing" _inputDrawing;
B _inputContainsInProgressStroke;
@"NSDate" _entryDate;
@"NSArray" _recognitionLocaleIdentifiers;
@"NSArray" _inputTargets;
@"CHTextInputTargetContentInfo" _inputTargetContentInfo;
@"NSString" _inputTargetElementType;
@"CHTokenizedTextResult" _tokenizedTextResult;
@"NSString" _resultCommittedText;
@"NSString" _resultTopTranscription;
q _resultCommittedTokenColumnCount;
@"NSString" _resultTypeDescription;
@"NSString" _resultCommitReason;
d _resultRecognitionDuration;
{_NSRange="location"Q"length"Q} _resultAffectedRange;
```

## Properties

```
@property (T@"NSDate",&,N,V_entryDate) entryDate;
@property (T@"NSArray",C,N,V_recognitionLocaleIdentifiers) recognitionLocaleIdentifiers;
@property (T@"PKDrawing",&,N,V_inputDrawing) inputDrawing;
@property (TB,N,V_inputContainsInProgressStroke) inputContainsInProgressStroke;
@property (T@"NSArray",C,N,V_inputTargets) inputTargets;
@property (T@"CHTextInputTargetContentInfo",&,N,V_inputTargetContentInfo) inputTargetContentInfo;
@property (T@"NSString",C,N,V_inputTargetElementType) inputTargetElementType;
@property (T@"CHTokenizedTextResult",&,N,V_tokenizedTextResult) tokenizedTextResult;
@property (T@"NSString",C,N,V_resultCommittedText) resultCommittedText;
@property (T@"NSString",C,N,V_resultTopTranscription) resultTopTranscription;
@property (Tq,N,V_resultCommittedTokenColumnCount) resultCommittedTokenColumnCount;
@property (T{_NSRange=QQ},N,V_resultAffectedRange) resultAffectedRange;
@property (T@"NSString",C,N,V_resultTypeDescription) resultTypeDescription;
@property (T@"NSString",C,N,V_resultCommitReason) resultCommitReason;
@property (Td,N,V_resultRecognitionDuration) resultRecognitionDuration;
@property (Tq,R,N) resultType;
```

## Class methods

```
+[PKTextInputDebugLogEntry _mutableDictionaryRepresentationForResultQueryItem:detailLevel:];
+[PKTextInputDebugLogEntry _minimalReferenceString:rangeOfInterest:tokenSearchDistance:localeIdentifier:];
+[PKTextInputDebugLogEntry _referenceSubstringForTargetContentInfo:resultAffectedRange:targetContentLevel:localeIdentifier:];
+[PKTextInputDebugLogEntry loggedDateFormatter];
+[PKTextInputDebugLogEntry mediumDescriptionForResultQueryItem:];
```

## Instance methods

```
-[PKTextInputDebugLogEntry resultType];
-[PKTextInputDebugLogEntry minimalDescription];
-[PKTextInputDebugLogEntry entryDate];
-[PKTextInputDebugLogEntry setEntryDate:];
-[PKTextInputDebugLogEntry description];
-[PKTextInputDebugLogEntry inputDrawing];
-[PKTextInputDebugLogEntry setInputDrawing:];
-[PKTextInputDebugLogEntry resultCommittedTokenColumnCount];
-[PKTextInputDebugLogEntry dictionaryRepresentationWithDetailLevel:targetContentLevel:];
-[PKTextInputDebugLogEntry dictionaryRepresentationWithTargetContentLevel:];
-[PKTextInputDebugLogEntry inputContainsInProgressStroke];
-[PKTextInputDebugLogEntry inputTargetContentInfo];
-[PKTextInputDebugLogEntry inputTargetElementType];
-[PKTextInputDebugLogEntry inputTargets];
-[PKTextInputDebugLogEntry mediumDescription];
-[PKTextInputDebugLogEntry recognitionLocaleIdentifiers];
-[PKTextInputDebugLogEntry referenceSubstringWithTargetContentLevel:];
-[PKTextInputDebugLogEntry resultAffectedRange];
-[PKTextInputDebugLogEntry resultCommitReason];
-[PKTextInputDebugLogEntry resultCommittedText];
-[PKTextInputDebugLogEntry resultRecognitionDuration];
-[PKTextInputDebugLogEntry resultTopTranscription];
-[PKTextInputDebugLogEntry resultTypeDescription];
-[PKTextInputDebugLogEntry setInputContainsInProgressStroke:];
-[PKTextInputDebugLogEntry setInputTargetContentInfo:];
-[PKTextInputDebugLogEntry setInputTargetElementType:];
-[PKTextInputDebugLogEntry setInputTargets:];
-[PKTextInputDebugLogEntry setRecognitionLocaleIdentifiers:];
-[PKTextInputDebugLogEntry setResultAffectedRange:];
-[PKTextInputDebugLogEntry setResultCommitReason:];
-[PKTextInputDebugLogEntry setResultCommittedText:];
-[PKTextInputDebugLogEntry setResultCommittedTokenColumnCount:];
-[PKTextInputDebugLogEntry setResultRecognitionDuration:];
-[PKTextInputDebugLogEntry setResultTopTranscription:];
-[PKTextInputDebugLogEntry setResultTypeDescription:];
-[PKTextInputDebugLogEntry setTokenizedTextResult:];
-[PKTextInputDebugLogEntry tokenizedTextResult];
```
