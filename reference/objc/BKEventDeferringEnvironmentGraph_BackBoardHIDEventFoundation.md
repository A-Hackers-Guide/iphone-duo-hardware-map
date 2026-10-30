# `BKEventDeferringEnvironmentGraph`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 12 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _topLevelPredicateNodesByPID;
@"BKSEventDeferringChainIdentity" _graphIdentity;
q _generation;
@"NSMutableDictionary" _modalityAssertionsByClientPID;
@"NSMutableDictionary" _constraintAssertionsByClientPID;
@"NSMutableDictionary" _grantAssertionsByGrantorPID;
@"NSMutableOrderedSet" _allNodes;
@"NSMutableDictionary" _nodeByIdentity;
@"NSMutableDictionary" _nodeByDeferringTarget;
@"NSMutableDictionary" _predicateNodesByTarget;
@"NSMutableDictionary" _ruleNodesByDestinationTarget;
@"NSMutableDictionary" _selectionPathContainerByIdentifier;
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
-[BKEventDeferringEnvironmentGraph dealloc];
-[BKEventDeferringEnvironmentGraph hash];
-[BKEventDeferringEnvironmentGraph description];
-[BKEventDeferringEnvironmentGraph appendDescriptionToStream:];
-[BKEventDeferringEnvironmentGraph copyWithZone:];
-[BKEventDeferringEnvironmentGraph isEqual:];
-[BKEventDeferringEnvironmentGraph describeDeliveryChain:identifier:];
-[BKEventDeferringEnvironmentGraph graphDescriptionWithLabel:];
```
