# `BLSHPendingFlipbookVisualStateOperation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 7 instance variables, 16 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _started;
B _completed;
B _updatedInitialState;
B _isFlipbook;
@"BLSHPresentationDateSpecifier" _initialSpecifier;
@"NSArray" _events;
q _targetDisplayMode;
```

## Properties

```
@property (TB,R,V_isFlipbook) isFlipbook;
@property (T@"BLSHPresentationDateSpecifier",R,V_initialSpecifier) initialSpecifier;
@property (T@"NSArray",R,V_events) events;
@property (T@"BLSBacklightChangeEvent",R) triggerEvent;
@property (TB,GdidUpdateInitialState,V_updatedInitialState) updatedInitialState;
@property (TB,R,GisBeforeDisplayBlankingChange) beforeDisplayBlankingChange;
@property (Tq,R,V_targetDisplayMode) targetDisplayMode;
@property (Tq,R) type;
@property (TB,GisStarted,V_started) started;
@property (TB,GisCompleted,V_completed) completed;
@property (T@"BLSHPendingEnvironmentUpdateOperation",?,R) environmentUpdateOperation;
@property (T@"BLSHPendingFlipbookVisualStateOperation",?,R) flipbookOperation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHPendingFlipbookVisualStateOperation triggerEvent];
-[BLSHPendingFlipbookVisualStateOperation setCompleted:];
-[BLSHPendingFlipbookVisualStateOperation environmentUpdateOperation];
-[BLSHPendingFlipbookVisualStateOperation isStarted];
-[BLSHPendingFlipbookVisualStateOperation setStarted:];
-[BLSHPendingFlipbookVisualStateOperation targetDisplayMode];
-[BLSHPendingFlipbookVisualStateOperation isFlipbook];
-[BLSHPendingFlipbookVisualStateOperation didUpdateInitialState];
-[BLSHPendingFlipbookVisualStateOperation isCompleted];
-[BLSHPendingFlipbookVisualStateOperation events];
-[BLSHPendingFlipbookVisualStateOperation isBeforeDisplayBlankingChange];
-[BLSHPendingFlipbookVisualStateOperation initialSpecifier];
-[BLSHPendingFlipbookVisualStateOperation shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:];
-[BLSHPendingFlipbookVisualStateOperation type];
-[BLSHPendingFlipbookVisualStateOperation description];
-[BLSHPendingFlipbookVisualStateOperation flipbookOperation];
-[BLSHPendingFlipbookVisualStateOperation setUpdatedInitialState:];
-[BLSHPendingFlipbookVisualStateOperation initWithIsFlipbook:initialSpecifier:];
-[BLSHPendingFlipbookVisualStateOperation initWithIsFlipbook:initialSpecifier:events:targetDisplayMode:];
```
