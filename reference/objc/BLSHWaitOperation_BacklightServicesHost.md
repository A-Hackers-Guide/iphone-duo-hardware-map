# `BLSHWaitOperation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 2 instance variables, 11 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _started;
B _completed;
```

## Properties

```
@property (Tq,R) type;
@property (TB,GisStarted,V_started) started;
@property (TB,GisCompleted,V_completed) completed;
@property (TB,?,R,GisBeforeDisplayBlankingChange) beforeDisplayBlankingChange;
@property (Tq,?,R) targetDisplayMode;
@property (T@"BLSHPendingEnvironmentUpdateOperation",?,R) environmentUpdateOperation;
@property (T@"BLSHPendingFlipbookVisualStateOperation",?,R) flipbookOperation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHWaitOperation setCompleted:];
-[BLSHWaitOperation isStarted];
-[BLSHWaitOperation setStarted:];
-[BLSHWaitOperation isCompleted];
-[BLSHWaitOperation type];
```
