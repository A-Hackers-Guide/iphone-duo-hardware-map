# `BLSHPendingEnvironmentUpdate`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 5 instance variables, 12 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _flipbookFirst;
B _started;
B _completed;
@"BLSHPendingFlipbookVisualStateOperation" _flipbookOperation;
@"BLSHPendingEnvironmentUpdateOperation" _environmentUpdateOperation;
```

## Properties

```
@property (T@"BLSHPendingFlipbookVisualStateOperation",R,V_flipbookOperation) flipbookOperation;
@property (T@"BLSHPendingEnvironmentUpdateOperation",R,V_environmentUpdateOperation) environmentUpdateOperation;
@property (T@"<BLSHPendingOperation>",R) currentOperation;
@property (TB,R,GisBeforeDisplayBlankingChange) beforeDisplayBlankingChange;
@property (Tq,R) targetDisplayMode;
@property (Tq,R) type;
@property (TB,GisStarted,V_started) started;
@property (TB,GisCompleted,V_completed) completed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHPendingEnvironmentUpdate setCompleted:];
-[BLSHPendingEnvironmentUpdate environmentUpdateOperation];
-[BLSHPendingEnvironmentUpdate isStarted];
-[BLSHPendingEnvironmentUpdate setStarted:];
-[BLSHPendingEnvironmentUpdate targetDisplayMode];
-[BLSHPendingEnvironmentUpdate isCompleted];
-[BLSHPendingEnvironmentUpdate isBeforeDisplayBlankingChange];
-[BLSHPendingEnvironmentUpdate shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:];
-[BLSHPendingEnvironmentUpdate type];
-[BLSHPendingEnvironmentUpdate description];
-[BLSHPendingEnvironmentUpdate flipbookOperation];
-[BLSHPendingEnvironmentUpdate currentOperation];
-[BLSHPendingEnvironmentUpdate initWithFlipbookOperation:environmentUpdateOperation:flipbookFirst:];
```
