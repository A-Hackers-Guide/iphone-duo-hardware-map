# `PKRecognitionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKRecognitionSessionManagerDelegate`
- 7 instance variables, 7 properties, 32 instance methods, 5 class methods

## Instance variables

```
@"_PKDataDetectorController" _dataDetectorController;
@"PKMathRecognitionController" _mathRecognitionController;
@"NSUUID" _listenerID;
@"NSMutableSet" _currentDrawingStrokeUUIDs;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _currentDrawingStrokeUUIDsLock;
@"<PKRecognitionControllerInternalDelegate>" _internalDelegate;
@"PKRecognitionSessionManager" _sessionManager;
```

## Properties

```
@property (T@"PKDrawing",C,N) drawing;
@property (T@"_PKDataDetectorController",R,N) dataDetectorController;
@property (T@"PKMathRecognitionController",R,N) mathRecognitionController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKRecognitionController currentDeviceSupportsAutoRefine];
+[PKRecognitionController changeStrokesUsingTransformations:strokeGroups:drawing:originalStrokes:];
+[PKRecognitionController newStrokesFromApplyingTransformations:strokeGroups:drawing:originalStrokes:];
+[PKRecognitionController recognitionVersion];
+[PKRecognitionController removeStrokesFromStyleInventory:];
```

## Instance methods

```
-[PKRecognitionController drawing];
-[PKRecognitionController dealloc];
-[PKRecognitionController setDrawing:];
-[PKRecognitionController initWithDrawing:];
-[PKRecognitionController canConvertTextToHandwriting:];
-[PKRecognitionController contextLookupResultsAtLocation:completion:];
-[PKRecognitionController contextLookupResultsForPath:completion:];
-[PKRecognitionController contextLookupResultsWithSelectedStrokes:completion:];
-[PKRecognitionController convertTextToHandwriting:bounds:inkColor:inputScale:suggestedHeight:suggestedDrawing:progress:completion:shouldCancel:];
-[PKRecognitionController dataDetectorController];
-[PKRecognitionController initWithDrawing:visibleOnscreenStrokes:];
-[PKRecognitionController initWithDrawing:visibleOnscreenStrokes:useSessionCache:];
-[PKRecognitionController initWithDrawing:visibleOnscreenStrokes:useSessionCache:sessionCacheIdentifier:];
-[PKRecognitionController initWithDrawing:visibleOnscreenStrokes:useSessionCache:sessionCacheIdentifier:preferredLocales:];
-[PKRecognitionController isAnyStrokeInMathGroup:];
-[PKRecognitionController mathRecognitionController];
-[PKRecognitionController recognitionSessionManager:foundDataDetectorItems:];
-[PKRecognitionController recognitionSessionManager:foundHashtagItems:];
-[PKRecognitionController recognitionSessionManager:foundMentionItems:];
-[PKRecognitionController recognitionSessionManager:foundProofreadingItems:];
-[PKRecognitionController recognitionSessionManager:foundStrokeGroupItems:];
-[PKRecognitionController refineStrokes:drawing:inputScale:completion:];
-[PKRecognitionController reflowableLinesInitialStrokes:atLocation:completion:];
-[PKRecognitionController replaceStrokes:withString:inBounds:inputScale:completion:];
-[PKRecognitionController setCalculateDocumentProvider:];
-[PKRecognitionController setCanvasAttachmentProvider:];
-[PKRecognitionController setDrawing:withVisibleOnscreenStrokes:];
-[PKRecognitionController setVisibleOnscreenStrokes:];
-[PKRecognitionController shouldCancelForAutoRefineCompletion];
-[PKRecognitionController straightenStrokes:drawing:completionBlockWithStrokeTransformInfo:];
-[PKRecognitionController tagAsActive];
-[PKRecognitionController tagAsIdle];
```
