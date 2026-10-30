# `_PKStrokeConcrete`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKStroke`
- 18 instance variables, 5 properties, 95 instance methods, 2 class methods

## Instance variables

```
{shared_ptr<PKProtobufUnknownFields>="__ptr_"^{PKProtobufUnknownFields}"__cntrl_"^{__shared_weak_count}} _unknownFields;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedBounds;
@"PKInk" _ink;
{?=""(?=""{?="isHidden"b1"hiddenInherited"b1"inkInherited"b1"transformInherited"b1"isNewCopy"b1"randomSeed"b32"isRandomSeedSet"b1"isInProgressScribbleStroke"b1"combineWhenRendering_OBSOLETED"b1"isSynthesizedStroke"b1"shouldSolveMath"b1"safeForStyleInventory"b1"isPastedStroke"b1"isSharedStroke"b1}"allFlags"Q)} _flags;
@"NSUUID" _strokeUUID;
@"PKStrokePath" _strokeData;
{_PKStrokeID="clock"I"replicaUUID"[16C]"subclock"I} _substrokesVersion;
@"NSArray" _substrokes;
@"_PKStrokeClipPlane" _clipPlane;
@"PKStrokeMask" _strokeMask;
@"NSUUID" _groupID;
@"NSUUID" _renderGroupID;
q _shapeType;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _inkTransform;
@"PKStrokeRenderState" _renderState;
{_PKStrokeID="clock"I"replicaUUID"[16C]"subclock"I} _sortID;
{_PKStrokeID="clock"I"replicaUUID"[16C]"subclock"I} _version;
```

## Properties

```
@property (T@"NSArray",&,N,V_substrokes) _substrokes;
@property (T{_PKStrokeID=I[16C]I},N,V_sortID) _sortID;
@property (T{_PKStrokeID=I[16C]I},N,V_version) _version;
@property (T{_PKStrokeID=I[16C]I},N,V_substrokesVersion) _substrokesVersion;
@property (TB,R,N) _isFullyHidden;
```

## Class methods

```
+[_PKStrokeConcrete decodeRenameableUUIDFromData:transientArchiveDictionary:];
+[_PKStrokeConcrete encodeUUID:toData:];
```

## Instance methods

```
-[_PKStrokeConcrete _shapeType];
-[_PKStrokeConcrete _setBounds:];
-[_PKStrokeConcrete _transform];
-[_PKStrokeConcrete dataRepresentation];
-[_PKStrokeConcrete _addTestDataToUnknownFields];
-[_PKStrokeConcrete _groupID];
-[_PKStrokeConcrete copyWithStrokeID:];
-[_PKStrokeConcrete saveInksTo:];
-[_PKStrokeConcrete initWithStroke:hidden:version:ink:transform:];
-[_PKStrokeConcrete _copyWithNewTransform:];
-[_PKStrokeConcrete mutableCopyWithZone:];
-[_PKStrokeConcrete saveToV1Archive:sortedUUIDs:inks:withPathData:transient:];
-[_PKStrokeConcrete initWithLegacyArchive:sortedUUIDs:];
-[_PKStrokeConcrete _substrokesInDrawing:];
-[_PKStrokeConcrete initWithData:id:sortID:flags:version:ink:transform:substrokes:substrokesVersion:];
-[_PKStrokeConcrete initWithInk:strokePath:transform:mask:randomSeed:];
-[_PKStrokeConcrete _setFlags:];
-[_PKStrokeConcrete init];
-[_PKStrokeConcrete didUpdateSubstrokesInDrawing:];
-[_PKStrokeConcrete _invalidateBounds];
-[_PKStrokeConcrete saveStrokeID:toArchive:withSortedUUIDs:];
-[_PKStrokeConcrete set_substrokes:];
-[_PKStrokeConcrete _substrokes];
-[_PKStrokeConcrete _copyWithNewParticleOffset:secondaryParticleOffset:];
-[_PKStrokeConcrete _sortID];
-[_PKStrokeConcrete _strokeWithUUID:dataUUID:];
-[_PKStrokeConcrete copyForSubstroke];
-[_PKStrokeConcrete _anchorPointForTexture];
-[_PKStrokeConcrete _newStrokeWithSubstrokes:inDrawing:];
-[_PKStrokeConcrete initWithData:error:];
-[_PKStrokeConcrete _mergeUnparentedWithStroke:inDrawing:];
-[_PKStrokeConcrete renderBounds];
-[_PKStrokeConcrete _updateStroke:inDrawing:];
-[_PKStrokeConcrete readPointFromLegacyArchive:deltaFrom:];
-[_PKStrokeConcrete deltaTo:];
-[_PKStrokeConcrete _setGroupID:];
-[_PKStrokeConcrete initWithArchive:error:];
-[_PKStrokeConcrete initWithInk:strokePath:transform:mask:randomSeed:strokeID:];
-[_PKStrokeConcrete mergeArrayOfStrokes:with:inDrawing:];
-[_PKStrokeConcrete _isFullyHidden];
-[_PKStrokeConcrete _particleOffset];
-[_PKStrokeConcrete _setInkTransform:];
-[_PKStrokeConcrete _setStrokeMask:];
-[_PKStrokeConcrete _clipPlane];
-[_PKStrokeConcrete didUpdateInDrawing:];
-[_PKStrokeConcrete initWithArchive:sortedUUIDs:inks:parent:isHidden:transientArchiveDictionary:];
-[_PKStrokeConcrete initWithInk:strokePath:transform:mask:randomSeed:strokeID:renderGroupID:renderState:];
-[_PKStrokeConcrete saveToArchive:sortedUUIDs:inks:withPathData:parent:transient:];
-[_PKStrokeConcrete copyWithNewAnchorPointForTexture:];
-[_PKStrokeConcrete initWithV1Archive:sortedUUIDs:inks:];
-[_PKStrokeConcrete ink];
-[_PKStrokeConcrete _strokeByAppendingTransform:];
-[_PKStrokeConcrete hasSubstrokes];
-[_PKStrokeConcrete _renderState];
-[_PKStrokeConcrete _substrokesVersion];
-[_PKStrokeConcrete _strokeMask];
-[_PKStrokeConcrete _setRenderState:];
-[_PKStrokeConcrete saveToArchive:];
-[_PKStrokeConcrete _version];
-[_PKStrokeConcrete compareToStroke:];
-[_PKStrokeConcrete initWithArchive:sortedUUIDs:inks:transientArchiveDictionary:];
-[_PKStrokeConcrete _updateWithParent:inDrawing:];
-[_PKStrokeConcrete set_sortID:];
-[_PKStrokeConcrete _strokeUUID];
-[_PKStrokeConcrete readV1StrokeIDFromArchive:withSortedUUIDs:];
-[_PKStrokeConcrete _setTransform:];
-[_PKStrokeConcrete _hasPopulatedRenderBoundsCache];
-[_PKStrokeConcrete _secondaryParticleOffset];
-[_PKStrokeConcrete setPath:];
-[_PKStrokeConcrete _setRenderGroupID:];
-[_PKStrokeConcrete saveToArchive:sortedUUIDs:inks:withPathData:transient:];
-[_PKStrokeConcrete setInk:];
-[_PKStrokeConcrete saveUUIDsTo:];
-[_PKStrokeConcrete _inkTransform];
-[_PKStrokeConcrete _setClipPlane:];
-[_PKStrokeConcrete parentStrokeForInsertionInDrawing:];
-[_PKStrokeConcrete _setSubstrokes:];
-[_PKStrokeConcrete _mergeWithStroke:inDrawing:];
-[_PKStrokeConcrete copyForMutation];
-[_PKStrokeConcrete isEqual:];
-[_PKStrokeConcrete sliceIdentifierForTStart:tEnd:];
-[_PKStrokeConcrete _flags];
-[_PKStrokeConcrete set_substrokesVersion:];
-[_PKStrokeConcrete _setShapeType:];
-[_PKStrokeConcrete readPointFromArchive:];
-[_PKStrokeConcrete _renderGroupID];
-[_PKStrokeConcrete _dataInUnknownFields];
-[_PKStrokeConcrete initWithData:id:flags:ink:transform:substrokes:];
-[_PKStrokeConcrete _setStrokeUUID:];
-[_PKStrokeConcrete copyWithTransform:];
-[_PKStrokeConcrete readStrokeIDFromArchive:withSortedUUIDs:];
-[_PKStrokeConcrete set_version:];
-[_PKStrokeConcrete strokeApplying:];
-[_PKStrokeConcrete saveV1StrokeID:toArchive:withSortedUUIDs:];
-[_PKStrokeConcrete path];
```
