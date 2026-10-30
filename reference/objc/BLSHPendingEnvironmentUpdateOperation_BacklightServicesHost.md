# `BLSHPendingEnvironmentUpdateOperation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 6 instance variables, 15 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _started;
B _completed;
B _updatedInitialState;
@"NSArray" _events;
@"BLSHPresentationDateSpecifier" _initialSpecifier;
q _targetDisplayMode;
```

## Properties

```
@property (T@"BLSBacklightChangeEvent",R) triggerEvent;
@property (T@"NSArray",R,V_events) events;
@property (T@"BLSHPresentationDateSpecifier",R,V_initialSpecifier) initialSpecifier;
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
-[BLSHPendingEnvironmentUpdateOperation triggerEvent];
-[BLSHPendingEnvironmentUpdateOperation setCompleted:];
-[BLSHPendingEnvironmentUpdateOperation initWithTriggerEvent:withInitialSpecifier:];
-[BLSHPendingEnvironmentUpdateOperation environmentUpdateOperation];
-[BLSHPendingEnvironmentUpdateOperation isStarted];
-[BLSHPendingEnvironmentUpdateOperation setStarted:];
-[BLSHPendingEnvironmentUpdateOperation targetDisplayMode];
-[BLSHPendingEnvironmentUpdateOperation didUpdateInitialState];
-[BLSHPendingEnvironmentUpdateOperation isCompleted];
-[BLSHPendingEnvironmentUpdateOperation events];
-[BLSHPendingEnvironmentUpdateOperation isBeforeDisplayBlankingChange];
-[BLSHPendingEnvironmentUpdateOperation initialSpecifier];
-[BLSHPendingEnvironmentUpdateOperation shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:];
-[BLSHPendingEnvironmentUpdateOperation type];
-[BLSHPendingEnvironmentUpdateOperation description];
-[BLSHPendingEnvironmentUpdateOperation flipbookOperation];
-[BLSHPendingEnvironmentUpdateOperation initWithEvents:withInitialSpecifier:targetDisplayMode:];
-[BLSHPendingEnvironmentUpdateOperation setUpdatedInitialState:];
```
