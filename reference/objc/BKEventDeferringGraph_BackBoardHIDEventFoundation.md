# `BKEventDeferringGraph`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`
- 6 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _identityToGraph;
@"NSMutableDictionary" _pidToRules;
@"NSMutableDictionary" _pidToConstraints;
@"NSMutableDictionary" _pidToModalities;
@"NSMutableDictionary" _pidToGrants;
@"NSSet" _senderDisplays;
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
-[BKEventDeferringGraph init];
-[BKEventDeferringGraph appendDescriptionToFormatter:];
-[BKEventDeferringGraph description];
-[BKEventDeferringGraph describeDeliveryChains:identifier:];
-[BKEventDeferringGraph legend];
```
