# `BLSHPendingUpdatePresentation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 4 instance variables, 13 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _started;
B _completed;
@"BLSHBacklightEnvironmentPresentation" _presentation;
q _targetBacklightState;
```

## Properties

```
@property (T@"BLSHBacklightEnvironmentPresentation",R,V_presentation) presentation;
@property (Tq,V_targetBacklightState) targetBacklightState;
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
-[BLSHPendingUpdatePresentation setCompleted:];
-[BLSHPendingUpdatePresentation presentation];
-[BLSHPendingUpdatePresentation isStarted];
-[BLSHPendingUpdatePresentation setStarted:];
-[BLSHPendingUpdatePresentation isCompleted];
-[BLSHPendingUpdatePresentation initWithPresentation:];
-[BLSHPendingUpdatePresentation type];
-[BLSHPendingUpdatePresentation description];
-[BLSHPendingUpdatePresentation setTargetBacklightState:];
-[BLSHPendingUpdatePresentation targetBacklightState];
```
