# `BKEventDeferringSelectionPathContainer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDeferringSelectionPathIdentifier" _pathIdentifier;
@"NSMutableSet" _selectedDestinations;
@"NSMutableDictionary" _subtargetSelectionHistoryByTarget;
@"NSDictionary" _constraintAssertionsByTarget;
@"NSDictionary" _constraintAssertionsBySourcePID;
@"NSDictionary" _modalityAssertionsByTarget;
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
-[BKEventDeferringSelectionPathContainer copy];
-[BKEventDeferringSelectionPathContainer hash];
-[BKEventDeferringSelectionPathContainer description];
-[BKEventDeferringSelectionPathContainer appendDescriptionToStream:];
-[BKEventDeferringSelectionPathContainer copyWithZone:];
-[BKEventDeferringSelectionPathContainer isEqual:];
-[BKEventDeferringSelectionPathContainer _addTarget:parentTarget:];
-[BKEventDeferringSelectionPathContainer _addTarget:parentTarget:recordInHistory:];
-[BKEventDeferringSelectionPathContainer _keyForTarget:];
```
