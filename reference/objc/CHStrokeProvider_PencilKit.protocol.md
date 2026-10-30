# `CHStrokeProvider` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"<CHStrokeProviderVersion>",R) strokeProviderVersion;
@property (T@"NSArray",R,C) orderedStrokes;
@property (Tq,R) groupingPriority;
@property (T{CGSize=dd},?,R) drawingCanvasSize;
@property (T@"NSOrderedSet",?,R,C) visibleStrokeEncodedIdentifiers;
```

## Instance methods

```
-[CHStrokeProvider compareOrderOfStrokeWithIdentifier:toStrokeWithIdentifier:];
-[CHStrokeProvider compareStyleOfStrokeWithIdentifier:toStrokeWithIdentifier:];
-[CHStrokeProvider encodedStrokeIdentifier:];
-[CHStrokeProvider groupingPriority];
-[CHStrokeProvider orderedStrokes];
-[CHStrokeProvider strokeForIdentifier:];
-[CHStrokeProvider strokeIdentifierFromData:];
-[CHStrokeProvider strokeProviderVersion];
-[CHStrokeProvider visibleStrokeEncodedIdentifiers];
-[CHStrokeProvider cachedTranscriptionForStrokeGroup:];
-[CHStrokeProvider cachedTranscriptionsIntersectingStrokeGroup:];
-[CHStrokeProvider compareOrderOfStroke:toStroke:];
-[CHStrokeProvider drawingCanvasSize];
-[CHStrokeProvider isStroke:versionOfStrokeWithIdentifier:];
-[CHStrokeProvider isValidStrokeIdentifier:];
```
