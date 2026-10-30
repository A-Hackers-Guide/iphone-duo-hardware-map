# `PKGroupQuery`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKQuery`
- Protocols: `CHQueryDelegate`
- 7 instance variables, 6 properties, 35 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _intersectionQueue;
@"NSObject<OS_dispatch_queue>" _strokeGroupComputationQueue;
d _defaultUpdatesInterval;
@"NSArray" _strokeGroups;
@"NSSet" _handwritingStrokeUUIDs;
@"CHStrokeGroupQuery" _strokeGroupQuery;
@"PKDrawing" _drawing;
```

## Properties

```
@property (T@"CHStrokeGroupQuery",&,N,V_strokeGroupQuery) strokeGroupQuery;
@property (T@"PKDrawing",&,N,V_drawing) drawing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKGroupQuery _strokesInLine:inDrawing:];
```

## Instance methods

```
-[PKGroupQuery drawing];
-[PKGroupQuery pause];
-[PKGroupQuery dealloc];
-[PKGroupQuery start];
-[PKGroupQuery setDrawing:];
-[PKGroupQuery teardown];
-[PKGroupQuery queryDidUpdateResult:];
-[PKGroupQuery strokeGroups];
-[PKGroupQuery _closestLineToPoint:isTop:];
-[PKGroupQuery _firstLineIndexFromInitialStrokes:];
-[PKGroupQuery _lastLineIndexFromInitialStrokes:];
-[PKGroupQuery _lines:containingStrokes:];
-[PKGroupQuery _precalculateStrokeGroupProperties:];
-[PKGroupQuery _strokes:containsAnyStrokes:];
-[PKGroupQuery _strokesAtLineIndex:containingStrokes:];
-[PKGroupQuery _strokesForIdentifiers:inDrawing:];
-[PKGroupQuery _strokesInLine:leftOf:point:];
-[PKGroupQuery _tokenizationLevelForSelectionType:];
-[PKGroupQuery contentTypeForIntersectedStrokes:];
-[PKGroupQuery fetchCurrentHandwritingStrokeUUIDs];
-[PKGroupQuery fetchCurrentStrokeGroupItems:];
-[PKGroupQuery firstStrokesInStrokes:isRTL:];
-[PKGroupQuery handwritingStrokeUUIDs];
-[PKGroupQuery initWithRecognitionSessionManager:];
-[PKGroupQuery isAnyStrokeInMathGroup:];
-[PKGroupQuery lastStrokesInStrokes:isRTL:];
-[PKGroupQuery q_fetchStrokesAmbiguouslyBelowAndAboveInsertSpaceHandleWithStrokes:completion:];
-[PKGroupQuery q_fetchStrokesBetweenTopPoint:bottomPoint:isRTL:completion:];
-[PKGroupQuery q_fetchStrokesForPoint:selectionType:inputType:visibleOnscreenStrokes:completion:];
-[PKGroupQuery setHandwritingStrokeUUIDs:];
-[PKGroupQuery setMathPreferredUpdatesInterval:];
-[PKGroupQuery setStrokeGroupQuery:];
-[PKGroupQuery setStrokeGroups:];
-[PKGroupQuery strokeGroupQuery];
-[PKGroupQuery textStrokesCoveredByStroke:completion:];
```
