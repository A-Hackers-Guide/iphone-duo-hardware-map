# `PKTextInputHandwritingShot`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputRecognitionManagerDataSource`, `PKTextInputDebugStateReporting`
- 22 instance variables, 27 properties, 71 instance methods, 2 class methods

## Instance variables

```
B _writingIsActiveAtStart;
B _cursorIsWeakAtStart;
B _cursorIsForcedStrongAtStart;
B _cancelled;
B __didRequestTextInputElements;
@"PKTextInputCanvasController" _canvasController;
@"PKTextInputElementsController" _elementsController;
@"<PKTextInputHandwritingShotDelegate>" _delegate;
@"PKDrawing" _inputDrawing;
@"PKStroke" _inputInProgressStroke;
@"NSNumber" _writingSessionIdentifier;
q _shotState;
@"PKTextInputStrokeProvider" _strokeProvider;
@"NSArray" _resultQueryItems;
d _recognitionDuration;
@"PKTextInputLanguageSpec" _languageSpec;
@"NSDictionary" __inputElementsByRecognitionID;
@"NSMutableDictionary" __inputElementsContentByRecognitionID;
@"NSMutableIndexSet" __potentiallyTargetedElementRecognitionIDs;
@"NSArray" __submittedTextInputTargets;
@"NSDictionary" __submittedTargetContentInfoByTargetID;
d __lastDrawingUpdateTimestamp;
```

## Properties

```
@property (Tq,N,S_setShotState:,V_shotState) shotState;
@property (T@"NSDictionary",C,N,S_setInputElementsByRecognitionID:,V__inputElementsByRecognitionID) _inputElementsByRecognitionID;
@property (T@"NSMutableDictionary",R,N,V__inputElementsContentByRecognitionID) _inputElementsContentByRecognitionID;
@property (T@"NSMutableIndexSet",&,N,V__potentiallyTargetedElementRecognitionIDs) _potentiallyTargetedElementRecognitionIDs;
@property (T@"NSArray",C,N,S_setResultQueryItems:,V_resultQueryItems) resultQueryItems;
@property (T@"PKTextInputStrokeProvider",&,N,V_strokeProvider) strokeProvider;
@property (T@"NSArray",C,N,V__submittedTextInputTargets) _submittedTextInputTargets;
@property (T@"NSDictionary",C,N,V__submittedTargetContentInfoByTargetID) _submittedTargetContentInfoByTargetID;
@property (Td,N,V__lastDrawingUpdateTimestamp) _lastDrawingUpdateTimestamp;
@property (Td,N,V_recognitionDuration) recognitionDuration;
@property (TB,N,S_setDidRequestTextInputElements:,V__didRequestTextInputElements) _didRequestTextInputElements;
@property (T@"PKTextInputCanvasController",R,N,V_canvasController) canvasController;
@property (T@"PKTextInputElementsController",R,N,V_elementsController) elementsController;
@property (T@"<PKTextInputHandwritingShotDelegate>",W,N,V_delegate) delegate;
@property (T@"PKDrawing",R,C,N,V_inputDrawing) inputDrawing;
@property (T@"PKStroke",R,C,N,V_inputInProgressStroke) inputInProgressStroke;
@property (TB,N,V_writingIsActiveAtStart) writingIsActiveAtStart;
@property (TB,N,V_cursorIsWeakAtStart) cursorIsWeakAtStart;
@property (TB,N,V_cursorIsForcedStrongAtStart) cursorIsForcedStrongAtStart;
@property (T@"NSNumber",C,N,V_writingSessionIdentifier) writingSessionIdentifier;
@property (T@"PKTextInputLanguageSpec",R,N,V_languageSpec) languageSpec;
@property (TB,N,GisCancelled,V_cancelled) cancelled;
@property (T@"NSArray",R,C,N) textInputTargets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputHandwritingShot _contentTypeFromKeyboardType:];
+[PKTextInputHandwritingShot _contentTypeFromTextContentType:];
```

## Instance methods

```
-[PKTextInputHandwritingShot setCancelled:];
-[PKTextInputHandwritingShot isCancelled];
-[PKTextInputHandwritingShot setDelegate:];
-[PKTextInputHandwritingShot delegate];
-[PKTextInputHandwritingShot description];
-[PKTextInputHandwritingShot _shouldTargetFirstResponderElement:strokeIdentifiers:];
-[PKTextInputHandwritingShot inputDrawing];
-[PKTextInputHandwritingShot setStrokeProvider:];
-[PKTextInputHandwritingShot strokeProvider];
-[PKTextInputHandwritingShot textInputTargets];
-[PKTextInputHandwritingShot recognitionManager:recognitionDidFinishWithQueryItems:duration:];
-[PKTextInputHandwritingShot setCursorIsForcedStrongAtStart:];
-[PKTextInputHandwritingShot set_lastDrawingUpdateTimestamp:];
-[PKTextInputHandwritingShot _autoCapitalizationModeForTextInputTraits:];
-[PKTextInputHandwritingShot _autoCorrectionModeForTextInputTraits:];
-[PKTextInputHandwritingShot _closestInputElementForStrokeIdentifiers:];
-[PKTextInputHandwritingShot _contentInfoFromElementContent:textInputTarget:strokeIdentifiers:];
-[PKTextInputHandwritingShot _contentTypeForElementContent:];
-[PKTextInputHandwritingShot _correctableTextRangeIntersectingStrokesWithIdentifiers:inInputTarget:elementContent:];
-[PKTextInputHandwritingShot _didRequestTextInputElements];
-[PKTextInputHandwritingShot _editingGestureCorrectableRangeForStrokeBounds:InInputTarget:elementContent:];
-[PKTextInputHandwritingShot _evaluateSubmissionReadyness];
-[PKTextInputHandwritingShot _fetchTextInputElementsIfNeededWithReferenceHitPoint:referenceSearchArea:referenceCoordSpace:];
-[PKTextInputHandwritingShot _inputElementsByRecognitionID];
-[PKTextInputHandwritingShot _inputElementsContentByRecognitionID];
-[PKTextInputHandwritingShot _lastDrawingUpdateTimestamp];
-[PKTextInputHandwritingShot _loadAndSaveContentFocusingIfNeededForElement:referenceCanvasPoint:strokesBounds:completion:];
-[PKTextInputHandwritingShot _potentiallyTargetedElementRecognitionIDs];
-[PKTextInputHandwritingShot _protectedCharacterIndexesInRange:forElementContent:];
-[PKTextInputHandwritingShot _saveSubmittedTargetContentInfo:];
-[PKTextInputHandwritingShot _selectedTextRangeForElementContent:textInputTarget:strokeSliceIdentifiers:];
-[PKTextInputHandwritingShot _setDidRequestTextInputElements:];
-[PKTextInputHandwritingShot _setInputElementsByRecognitionID:];
-[PKTextInputHandwritingShot _setResultQueryItems:];
-[PKTextInputHandwritingShot _setShotState:];
-[PKTextInputHandwritingShot _setupStrokeProvider];
-[PKTextInputHandwritingShot _submittedTargetContentInfoByTargetID];
-[PKTextInputHandwritingShot _submittedTextInputTargets];
-[PKTextInputHandwritingShot _substringReferenceRangeForStrokeCoveredRange:contentLength:selectedRange:];
-[PKTextInputHandwritingShot _textContentSubstringInRange:forElementContent:];
-[PKTextInputHandwritingShot beginRecognitionWithRecognitionManager:];
-[PKTextInputHandwritingShot canvasController];
-[PKTextInputHandwritingShot chWritingDirectionFrom:useDefault:];
-[PKTextInputHandwritingShot cursorIsForcedStrongAtStart];
-[PKTextInputHandwritingShot cursorIsWeakAtStart];
-[PKTextInputHandwritingShot elementsController];
-[PKTextInputHandwritingShot initWithCanvasController:elementsController:languageSpec:];
-[PKTextInputHandwritingShot inputInProgressStroke];
-[PKTextInputHandwritingShot isPotentiallyTargetingElement:];
-[PKTextInputHandwritingShot languageSpec];
-[PKTextInputHandwritingShot recognitionDuration];
-[PKTextInputHandwritingShot recognitionManager:fetchContentInfoForTextInputTarget:strokeIdentifiers:completion:];
-[PKTextInputHandwritingShot recognitionManager:textInputTargetForItemStableIdentifier:strokeIdentifiers:simultaneousItemStableIdentifiers:];
-[PKTextInputHandwritingShot recognitionManagerStrokeProvider:];
-[PKTextInputHandwritingShot recognitionManagerTextInputTargets:];
-[PKTextInputHandwritingShot reportDebugStateDescription:];
-[PKTextInputHandwritingShot resultQueryItems];
-[PKTextInputHandwritingShot setCursorIsWeakAtStart:];
-[PKTextInputHandwritingShot setInputDrawing:inputInProgressStroke:];
-[PKTextInputHandwritingShot setRecognitionDuration:];
-[PKTextInputHandwritingShot setWritingIsActiveAtStart:];
-[PKTextInputHandwritingShot setWritingSessionIdentifier:];
-[PKTextInputHandwritingShot set_potentiallyTargetedElementRecognitionIDs:];
-[PKTextInputHandwritingShot set_submittedTargetContentInfoByTargetID:];
-[PKTextInputHandwritingShot set_submittedTextInputTargets:];
-[PKTextInputHandwritingShot shotState];
-[PKTextInputHandwritingShot submittedTargetContentInfoForRecognitionIdentifier:];
-[PKTextInputHandwritingShot textInputElementContentForRecognitionIdentifier:];
-[PKTextInputHandwritingShot textInputElementForRecognitionIdentifier:];
-[PKTextInputHandwritingShot writingIsActiveAtStart];
-[PKTextInputHandwritingShot writingSessionIdentifier];
```
