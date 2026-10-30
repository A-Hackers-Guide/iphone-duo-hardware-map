# `PKStrokeProvider`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHStrokeProvider`
- 8 instance variables, 10 properties, 25 instance methods, 2 class methods

## Instance variables

```
B _disabled;
@"NSMutableOrderedSet" _strokeSlices;
B _shouldProcessVisibleStrokes;
@"NSArray" _visibleOnscreenStrokes;
@"NSMutableDictionary" _strokeIdsByEncoding;
@"PKHandwritingTranscriptionCache" _transcriptionCache;
q groupingPriority;
@"PKDrawing" _drawing;
```

## Properties

```
@property (T@"PKDrawing",R,N,V_drawing) drawing;
@property (T@"<CHStrokeProviderVersion>",R) strokeProviderVersion;
@property (T@"NSArray",R,C) orderedStrokes;
@property (Tq,R,VgroupingPriority) groupingPriority;
@property (T{CGSize=dd},?,R) drawingCanvasSize;
@property (T@"NSOrderedSet",?,R,C) visibleStrokeEncodedIdentifiers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKStrokeProvider _identifiersForStrokes:];
+[PKStrokeProvider slicesForStrokes:];
```

## Instance methods

```
-[PKStrokeProvider drawing];
-[PKStrokeProvider slices];
-[PKStrokeProvider description];
-[PKStrokeProvider initWithDrawing:];
-[PKStrokeProvider visibleStrokeEncodedIdentifiers];
-[PKStrokeProvider cachedTranscriptionForStrokeGroup:];
-[PKStrokeProvider cachedTranscriptionsIntersectingStrokeGroup:];
-[PKStrokeProvider compareOrderOfStroke:toStroke:];
-[PKStrokeProvider compareOrderOfStrokeWithIdentifier:toStrokeWithIdentifier:];
-[PKStrokeProvider compareStyleOfStrokeWithIdentifier:toStrokeWithIdentifier:];
-[PKStrokeProvider drawingCanvasSize];
-[PKStrokeProvider encodedStrokeIdentifier:];
-[PKStrokeProvider groupingPriority];
-[PKStrokeProvider isStroke:versionOfStrokeWithIdentifier:];
-[PKStrokeProvider isValidStrokeIdentifier:];
-[PKStrokeProvider orderedStrokes];
-[PKStrokeProvider strokeForIdentifier:];
-[PKStrokeProvider strokeIdentifierFromData:];
-[PKStrokeProvider strokeProviderVersion];
-[PKStrokeProvider _cacheStrokeIdentifier:withEncodedStrokeIdentifier:];
-[PKStrokeProvider _cachedStrokeIdentifier:];
-[PKStrokeProvider enumerateChangesSinceVersion:usingBlock:];
-[PKStrokeProvider initWithDrawing:visibleOnscreenStrokes:shouldProcessVisibleStrokes:transcriptionCache:];
-[PKStrokeProvider sliceForIdentifier:];
-[PKStrokeProvider updateTranscriptionCache:];
```
