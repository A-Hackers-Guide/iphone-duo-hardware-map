# `PKAutoRefineTaskCoordinator`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKAutoRefineViewDelegate`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"PKRecognitionController" _recognitionController;
@"<PKAutoRefineTaskCoordinatorDelegate>" _delegate;
{?="delegateSupportsTiledView"b1"delegateSupportsReplaceStrokes"b1"delegateSupportsRecentStrokes"b1} _delegateFlags;
d _userInteractionDelay;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:drawingUUID:completionBlock:];
-[PKAutoRefineTaskCoordinator clearRefinableStrokes];
-[PKAutoRefineTaskCoordinator enumerateRefinableStrokesWithOptions:usingBlock:];
-[PKAutoRefineTaskCoordinator hasRefinableStrokes];
-[PKAutoRefineTaskCoordinator isRefinableStroke:];
```
