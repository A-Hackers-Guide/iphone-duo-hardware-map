# `PKAutoRefineTaskManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKAutoRefineTaskDelegate`
- 6 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _autoRefineQueue;
@"PKAutoRefineTask" _activeTask;
@"NSMutableArray" _tasksQueue;
@"<PKAutoRefineViewDelegate>" _autoRefineViewDelegate;
@"<CHStrokeProvider>" _latestStrokeProvider;
@"NSUUID" _currentDrawingUUID;
```

## Instance methods

```
-[PKAutoRefineTaskManager init];
-[PKAutoRefineTaskManager dealloc];
-[PKAutoRefineTaskManager autoRefineTask:isReadyToSynthesizeRefinedDrawingForStrokes:transcription:drawingUUID:];
```
