# `BLSHPendingOperation` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 10 instance methods, 0 class methods

## Properties

```
@property (Tq,R) type;
@property (TB,GisStarted) started;
@property (TB,GisCompleted) completed;
@property (TB,?,R,GisBeforeDisplayBlankingChange) beforeDisplayBlankingChange;
@property (Tq,?,R) targetDisplayMode;
@property (T@"BLSHPendingEnvironmentUpdateOperation",?,R) environmentUpdateOperation;
@property (T@"BLSHPendingFlipbookVisualStateOperation",?,R) flipbookOperation;
```

## Instance methods

```
-[BLSHPendingOperation setCompleted:];
-[BLSHPendingOperation isStarted];
-[BLSHPendingOperation setStarted:];
-[BLSHPendingOperation isCompleted];
-[BLSHPendingOperation type];
-[BLSHPendingOperation environmentUpdateOperation];
-[BLSHPendingOperation targetDisplayMode];
-[BLSHPendingOperation isBeforeDisplayBlankingChange];
-[BLSHPendingOperation shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:];
-[BLSHPendingOperation flipbookOperation];
```
