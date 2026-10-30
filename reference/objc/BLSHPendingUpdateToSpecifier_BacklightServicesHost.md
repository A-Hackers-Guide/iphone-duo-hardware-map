# `BLSHPendingUpdateToSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 3 instance variables, 12 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _started;
B _completed;
@"BLSHPresentationDateSpecifier" _specifier;
```

## Properties

```
@property (T@"BLSHPresentationDateSpecifier",R,V_specifier) specifier;
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
-[BLSHPendingUpdateToSpecifier setCompleted:];
-[BLSHPendingUpdateToSpecifier isStarted];
-[BLSHPendingUpdateToSpecifier setStarted:];
-[BLSHPendingUpdateToSpecifier isCompleted];
-[BLSHPendingUpdateToSpecifier specifier];
-[BLSHPendingUpdateToSpecifier type];
-[BLSHPendingUpdateToSpecifier description];
-[BLSHPendingUpdateToSpecifier initWithSpecifier:];
```
