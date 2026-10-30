# `PKDrawingConcrete`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDrawing`
- 9 instance variables, 7 properties, 93 instance methods, 3 class methods

## Instance variables

```
@"NSUUID" _uuid;
@"NSMutableDictionary" _strokesIdentifierMap;
@"NSMutableArray" _allStrokes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __canvasBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __bounds;
@"NSUUID" _replicaUUID;
@"PKVectorTimestamp" _version;
{shared_ptr<PKProtobufUnknownFields>="__ptr_"^{PKProtobufUnknownFields}"__cntrl_"^{__shared_weak_count}} _unknownFields;
{_PKStrokeID="clock"I"replicaUUID"[16C]"subclock"I} _boundsVersion;
```

## Properties

```
@property (T{_PKStrokeID=I[16C]I},N,V_boundsVersion) boundsVersion;
@property (T{shared_ptr<PKProtobufUnknownFields>=^{PKProtobufUnknownFields}^{__shared_weak_count}},R,N,V_unknownFields) _unknownFields;
@property (T@"NSMutableArray",&,N,S_setAllStrokes:) _allStrokes;
@property (T@"PKVectorTimestamp",&,N,V_version) version;
@property (T@"NSUUID",R,N) nsuuid;
@property (T@"NSUUID",R,N,V_replicaUUID) replicaUUID;
@property (TB,R,N) _hasReplicaUUID;
```

## Class methods

```
+[PKDrawingConcrete newStrokeIDGreaterThan:forUUID:];
+[PKDrawingConcrete _defaultConversionQueue];
+[PKDrawingConcrete _orientationTransform:size:];
```

## Instance methods

```
-[PKDrawingConcrete dataRepresentation];
-[PKDrawingConcrete _addTestDataToUnknownFields];
-[PKDrawingConcrete uuid];
-[PKDrawingConcrete init];
-[PKDrawingConcrete didUpdate];
-[PKDrawingConcrete data];
-[PKDrawingConcrete dealloc];
-[PKDrawingConcrete _orientation];
-[PKDrawingConcrete initWithData:error:];
-[PKDrawingConcrete version];
-[PKDrawingConcrete _data];
-[PKDrawingConcrete serialize];
-[PKDrawingConcrete hash];
-[PKDrawingConcrete bounds];
-[PKDrawingConcrete setVersion:];
-[PKDrawingConcrete copyWithZone:];
-[PKDrawingConcrete isEqual:];
-[PKDrawingConcrete _dataInUnknownFields];
-[PKDrawingConcrete _setUUID:];
-[PKDrawingConcrete nsuuid];
-[PKDrawingConcrete initWithDrawing:];
-[PKDrawingConcrete replicaUUID];
-[PKDrawingConcrete _hasReplicaUUID];
-[PKDrawingConcrete _setAllStrokes:];
-[PKDrawingConcrete _allStrokes];
-[PKDrawingConcrete _canvasBounds];
-[PKDrawingConcrete _collectAllStrokesIn:into:];
-[PKDrawingConcrete _conversionScaleFactor];
-[PKDrawingConcrete _drawingStrokeInfoIsLegacyDrawing:];
-[PKDrawingConcrete _initWithUnzippedData:error:];
-[PKDrawingConcrete _initWithUnzippedData:loadNonInkingStrokes:error:];
-[PKDrawingConcrete _mergeStroke:];
-[PKDrawingConcrete _newStroke:withGroupID:];
-[PKDrawingConcrete _newStroke:withInk:];
-[PKDrawingConcrete _orientedDrawingSize];
-[PKDrawingConcrete _removeHiddenAndEraserStrokes];
-[PKDrawingConcrete _removeInvisibleStrokes];
-[PKDrawingConcrete _rootStrokes];
-[PKDrawingConcrete _stroke:transformed:concat:];
-[PKDrawingConcrete _strokeForIdentifier:];
-[PKDrawingConcrete _strokesIdentifierMap];
-[PKDrawingConcrete _transformForImageWithSize:];
-[PKDrawingConcrete _unknownFields];
-[PKDrawingConcrete _unscaledOrientedDrawingSize];
-[PKDrawingConcrete _updateStrokes:updateBlock:];
-[PKDrawingConcrete _upgradeLegacyPenInks];
-[PKDrawingConcrete _upgradeOnQueue:isLegacyDrawing:completionBlock:];
-[PKDrawingConcrete addNewStroke:];
-[PKDrawingConcrete boundsVersion];
-[PKDrawingConcrete copyWithoutInternalStrokes];
-[PKDrawingConcrete deleteStrokes:];
-[PKDrawingConcrete didMergeWithDrawing:];
-[PKDrawingConcrete initWithArchive:loadNonInkingStrokes:error:];
-[PKDrawingConcrete initWithData:loadNonInkingStrokes:error:];
-[PKDrawingConcrete initWithLegacyArchive:];
-[PKDrawingConcrete initWithLegacyData:];
-[PKDrawingConcrete initWithStrokes:fromDrawing:];
-[PKDrawingConcrete initWithUUID:strokes:version:canvasBounds:boundsVersion:unknownFields:];
-[PKDrawingConcrete initWithV1Archive:loadNonInkingStrokes:];
-[PKDrawingConcrete initWithV1Data:loadNonInkingStrokes:];
-[PKDrawingConcrete invalidateStrokeBounds];
-[PKDrawingConcrete invalidateVisibleStrokes];
-[PKDrawingConcrete mergeWithDrawing:];
-[PKDrawingConcrete newStroke];
-[PKDrawingConcrete newStrokeIDGreaterThan:];
-[PKDrawingConcrete normalizeUUIDsWithDrawing:];
-[PKDrawingConcrete saveToArchive:withPathData:];
-[PKDrawingConcrete saveToV1Archive:withPathData:];
-[PKDrawingConcrete serializeTransiently];
-[PKDrawingConcrete serializeWithVersion:];
-[PKDrawingConcrete setBoundsVersion:];
-[PKDrawingConcrete setStrokeSortIDForInsertion:];
-[PKDrawingConcrete setStrokes:groupID:];
-[PKDrawingConcrete setStrokes:hidden:];
-[PKDrawingConcrete setStrokes:inks:];
-[PKDrawingConcrete set_canvasBounds:];
-[PKDrawingConcrete set_orientation:];
-[PKDrawingConcrete strokeClass];
-[PKDrawingConcrete strokeSelectionClass];
-[PKDrawingConcrete transformStrokes:withTransform:concat:];
-[PKDrawingConcrete undoableAddNewStrokes:];
-[PKDrawingConcrete undoableAddNewStrokes:replacingOldStrokes:];
-[PKDrawingConcrete undoableDeleteStrokes:];
-[PKDrawingConcrete undoableSetStrokes:groupID:actionName:];
-[PKDrawingConcrete undoableSetStrokes:inks:];
-[PKDrawingConcrete undoableTransformStrokes:withTransform:concat:];
-[PKDrawingConcrete updateFromSlicedIntersectingIndexes:resultNewRoots:resultUpdatedStrokes:count:];
-[PKDrawingConcrete updateStroke:indexHint:];
-[PKDrawingConcrete updateStrokes:];
-[PKDrawingConcrete v1SerializeWithPathData:];
-[PKDrawingConcrete v1SerializeWithPathData:toVersion:];
-[PKDrawingConcrete visibleStrokeForInsertingStroke:];
-[PKDrawingConcrete willMergeWithDrawing:];
```
