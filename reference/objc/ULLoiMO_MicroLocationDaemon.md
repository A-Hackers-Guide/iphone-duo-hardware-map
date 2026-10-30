# `ULLoiMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 19 properties, 2 instance methods, 3 class methods

## Properties

```
@property (Td,D,N) lastSeenTimeStamp;
@property (T@"NSNumber",&,D,N) loiCategory;
@property (TB,D,N) isSpareCategory;
@property (T@"NSString",&,D,N) loiGroupId;
@property (T@"NSString",&,D,N) loiId;
@property (T@"NSString",&,D,N) loiType;
@property (T@"NSSet",&,D,N) anchorAppearanceMap;
@property (T@"NSSet",&,D,N) associatedStates;
@property (T@"ULCustomLoiMO",&,D,N) customLOI;
@property (T@"NSSet",&,D,N) models;
@property (T@"NSSet",&,D,N) rapports;
@property (T@"NSSet",&,D,N) scanningEvents;
@property (T@"NSSet",&,D,N) wifiHistogram;
@property (T@"NSSet",&,D,N) odometryEntries;
@property (T@"NSSet",&,D,N) altitudeEntries;
@property (T@"NSSet",&,D,N) audioOdometryEntries;
@property (T@"NSSet",&,D,N) labels;
@property (T@"NSSet",&,D,N) poseEstimations;
@property (T@"NSSet",&,D,N) homeSlamLearningHistory;
```

## Class methods

```
+[ULLoiMO fetchRequest];
+[ULLoiMO createFromDO:inManagedObjectContext:];
+[ULLoiMO createWithLastSeenTimeStamp:loiId:loiGroupId:loiType:inManagedObjectContext:];
```

## Instance methods

```
-[ULLoiMO convertToDO];
-[ULLoiMO awakeFromInsert];
```
