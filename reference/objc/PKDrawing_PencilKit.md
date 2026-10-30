# `PKDrawing`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHQueryDelegate`, `NSCopying`, `NSSecureCoding`
- 8 instance variables, 14 properties, 154 instance methods, 16 class methods

## Instance variables

```
B _recognitionEnabled;
@"NSArray" _forcedRecognitionLocales;
@"NSUUID" _listenerID;
@"NSMutableArray" _cachedVisibleStrokes;
@"PKRecognitionSessionManager" _recognitionManager;
@"CHRecognitionSession" _recognitionSession;
@"NSMapTable" _ongoingQueries;
@"PKVisualizationManager" _visualizationManager;
```

## Properties

```
@property (Tq,N) _orientation;
@property (T@"PKRecognitionSessionManager",&,N,V_recognitionManager) recognitionManager;
@property (T@"NSUUID",&,N,S_setUUID:) uuid;
@property (T@"CHRecognitionSession",&,N,V_recognitionSession) recognitionSession;
@property (T@"NSMapTable",&,N,V_ongoingQueries) ongoingQueries;
@property (T@"PKVisualizationManager",&,N,V_visualizationManager) visualizationManager;
@property (T@"NSMutableArray",&,N,V_cachedVisibleStrokes) _cachedVisibleStrokes;
@property (T@"NSArray",R,N) strokes;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (Tq,R,N) requiredContentVersion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKDrawing allocWithZone:];
+[PKDrawing supportsSecureCoding];
+[PKDrawing fileType];
+[PKDrawing _boundingBoxForStrokeArray:];
+[PKDrawing _boundingBoxForStrokes:];
+[PKDrawing _currentSerializationVersion];
+[PKDrawing _findLeftmostStrokes:];
+[PKDrawing _findRightmostStrokes:];
+[PKDrawing _otherStrokesCloseToLeft:forStrokes:withClosestStroke:];
+[PKDrawing _upgradeDrawingData:queue:completionBlock:];
+[PKDrawing _uuidDescriptionForStrokes:];
+[PKDrawing drawingClassForPaper];
+[PKDrawing drawingStrokesFromStrokes:inDrawing:];
+[PKDrawing drawingWithData:];
+[PKDrawing sortStrokes:];
+[PKDrawing visibleStrokesFromStrokes:inDrawing:];
```

## Instance methods

```
-[PKDrawing dataRepresentation];
-[PKDrawing uuid];
-[PKDrawing init];
-[PKDrawing debugQuickLookObject];
-[PKDrawing classForCoder];
-[PKDrawing didUpdate];
-[PKDrawing data];
-[PKDrawing dealloc];
-[PKDrawing _orientation];
-[PKDrawing initWithData:error:];
-[PKDrawing version];
-[PKDrawing requiredContentVersion];
-[PKDrawing _isEmpty];
-[PKDrawing encodeWithCoder:];
-[PKDrawing hash];
-[PKDrawing bounds];
-[PKDrawing description];
-[PKDrawing initWithCoder:];
-[PKDrawing copyWithZone:];
-[PKDrawing isEqual:];
-[PKDrawing _setUUID:];
-[PKDrawing strokes];
-[PKDrawing initWithDrawing:];
-[PKDrawing _bounds];
-[PKDrawing indexableContent];
-[PKDrawing queryDidUpdateResult:];
-[PKDrawing recognitionSession];
-[PKDrawing setNeedsRecognitionUpdate];
-[PKDrawing CHDrawing];
-[PKDrawing _setAllStrokes:];
-[PKDrawing _visibleStrokes];
-[PKDrawing firstIntersectedStrokeAtPoint:inputType:visibleOnscreenStrokes:];
-[PKDrawing intersectedStrokesFromRect:visibleOnscreenStrokes:pathStepSize:];
-[PKDrawing _addStroke:];
-[PKDrawing _allStrokes];
-[PKDrawing _ascii];
-[PKDrawing _cachedVisibleStrokes];
-[PKDrawing _canvasBounds];
-[PKDrawing _clipAgainstLegacyCanvas:];
-[PKDrawing _clipMaskedStrokes];
-[PKDrawing _clipStroke:againstPaths:];
-[PKDrawing _clipStroke:newRootStroke:];
-[PKDrawing _copyAndAddStroke:transform:];
-[PKDrawing _copyAndAddStroke:transform:ink:newParent:];
-[PKDrawing _copyAndAddStroke:transform:inkTransform:ink:newParent:forceNewUUID:];
-[PKDrawing _copyAndAddStroke:transform:inkTransform:ink:newParent:forceNewUUID:existingStrokesUUIDs:];
-[PKDrawing _copyAndAddStrokes:transform:];
-[PKDrawing _copyAndAddStrokes:transform:forceNewUUID:];
-[PKDrawing _copyAndAddStrokes:transform:inkTransform:];
-[PKDrawing _copyAndAddStrokes:transform:inkTransform:forceNewUUID:];
-[PKDrawing _eraseWithEraserStroke:];
-[PKDrawing _eraserStrokeBounds];
-[PKDrawing _hasAnyHDRStrokes];
-[PKDrawing _imageInRect:scale:completionHandler:];
-[PKDrawing _minimumSerializationVersion];
-[PKDrawing _newAsciiBitfield];
-[PKDrawing _orientedDrawingSize];
-[PKDrawing _originalDataUUIDToTransformedStrokeDictFromStrokes:pathDict:maskDict:shouldUseStrokeDataUUID:];
-[PKDrawing _originalStrokeDataUUIDToTransformedStrokeDictFromStrokes:pathDict:maskDict:];
-[PKDrawing _originalStrokeUUIDToTransformedStrokeDictFromStrokes:pathDict:maskDict:];
-[PKDrawing _removeStroke:];
-[PKDrawing _rootStrokes];
-[PKDrawing _rootStrokesCount];
-[PKDrawing _strokeForIdentifier:];
-[PKDrawing _strokes];
-[PKDrawing _strokesIntersectedByPoint:prevPoint:transform:];
-[PKDrawing _teardownRecognitionObjects];
-[PKDrawing _transformAllStrokes:];
-[PKDrawing _transformForImageWithSize:];
-[PKDrawing _unclippedStroke:];
-[PKDrawing _updateRecognitionSession];
-[PKDrawing _upgradeLegacyPenInks];
-[PKDrawing _visibleStrokeForIdentifier:];
-[PKDrawing addNewStroke:];
-[PKDrawing cachedVisibleStrokes];
-[PKDrawing calculateStrokeBounds];
-[PKDrawing cancelOngoingRecognitionRequests];
-[PKDrawing clipStroke:onPlane:renderMask:];
-[PKDrawing clipStrokesIfNeededOnQueue:completion:];
-[PKDrawing containsInternalStrokes];
-[PKDrawing copyAndAddStroke:transform:];
-[PKDrawing copyCachedStrokesFrom:];
-[PKDrawing copyWithoutInternalStrokes];
-[PKDrawing deleteStrokes:];
-[PKDrawing drawingByAppendingDrawing:];
-[PKDrawing drawingByAppendingStrokes:];
-[PKDrawing drawingByApplyingTransform:];
-[PKDrawing drawingByApplyingTransform:transformInk:];
-[PKDrawing drawingByApplyingTransform:transformInk:forceNewUUID:];
-[PKDrawing drawingByErasingStrokePath:mask:transform:];
-[PKDrawing fetchIntersectedStrokesBetweenPoint:otherPoint:visibleOnscreenStrokes:completion:];
-[PKDrawing forcedRecognitionLocales];
-[PKDrawing imageFromRect:scale:];
-[PKDrawing initWithData:loadNonInkingStrokes:error:];
-[PKDrawing initWithStrokes:];
-[PKDrawing initWithStrokes:fromDrawing:];
-[PKDrawing insertNewTestStroke];
-[PKDrawing intersectedStrokesAtPoint:selectionType:inputType:visibleOnscreenStrokes:];
-[PKDrawing intersectedStrokesFromRect:visibleOnscreenStrokes:];
-[PKDrawing intersectedStrokesFromStroke:visibleOnscreenStrokes:];
-[PKDrawing intersectedStrokesTest:inBounds:visibleOnscreenStrokes:];
-[PKDrawing invalidateVisibleStrokes];
-[PKDrawing mergeWithDrawing:];
-[PKDrawing newStroke];
-[PKDrawing ongoingQueries];
-[PKDrawing performSearchQuery:fullWordsOnly:caseMatchingOnly:withBlock:];
-[PKDrawing performSearchQuery:withBlock:];
-[PKDrawing recognitionEnabled];
-[PKDrawing recognitionManager];
-[PKDrawing replaceStrokes:withNewStrokes:actionName:];
-[PKDrawing setForcedRecognitionLocales:];
-[PKDrawing setOngoingQueries:];
-[PKDrawing setRecognitionEnabled:];
-[PKDrawing setRecognitionManager:];
-[PKDrawing setRecognitionSession:];
-[PKDrawing setStroke:hidden:];
-[PKDrawing setStroke:ink:];
-[PKDrawing setStroke:transform:concat:];
-[PKDrawing setStrokeSubstrokes:];
-[PKDrawing setStrokes:groupID:];
-[PKDrawing setStrokes:hidden:];
-[PKDrawing setStrokes:inks:];
-[PKDrawing setStrokes:transform:concat:];
-[PKDrawing setVisualizationManager:];
-[PKDrawing set_cachedVisibleStrokes:];
-[PKDrawing set_canvasBounds:];
-[PKDrawing set_orientation:];
-[PKDrawing shouldClearSelectionAfterStraightening];
-[PKDrawing sliceWithEraseStroke:];
-[PKDrawing sliceWithEraseStroke:honoringErasable:];
-[PKDrawing strokeBounds];
-[PKDrawing strokeClass];
-[PKDrawing strokeSelectionClass];
-[PKDrawing strokesForCHStrokeIdentifiers:];
-[PKDrawing strokesForCHStrokeIdentifiers:didFindAllStrokes:];
-[PKDrawing strokesIntersectedByPoint:prevPoint:minThreshold:transform:onscreenVisibleStrokes:];
-[PKDrawing strokesIntersectedByPoint:prevPoint:onscreenVisibleStrokes:];
-[PKDrawing transformStrokes:paths:masks:];
-[PKDrawing transformStrokes:withTransform:concat:];
-[PKDrawing transformStrokes:withTransforms:concat:];
-[PKDrawing undoableAddNewStrokes:];
-[PKDrawing undoableAddNewStrokes:replacingOldStrokes:];
-[PKDrawing undoableDeleteStrokes:];
-[PKDrawing undoableMergeWithDrawing:];
-[PKDrawing undoableSetStrokes:groupID:actionName:];
-[PKDrawing undoableSetStrokes:inks:];
-[PKDrawing undoableTransformStrokes:withTransform:concat:];
-[PKDrawing updateFromSlicedIntersectingIndexes:resultNewRoots:resultUpdatedStrokes:count:];
-[PKDrawing updateStroke:indexHint:];
-[PKDrawing updateStroke:updater:];
-[PKDrawing updateStrokes:];
-[PKDrawing visibleStrokeForInsertingStroke:];
-[PKDrawing visibleStrokes];
-[PKDrawing visualizationManager];
```
