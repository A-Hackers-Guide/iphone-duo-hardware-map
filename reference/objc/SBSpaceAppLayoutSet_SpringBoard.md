# `SBSpaceAppLayoutSet`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionStreaming`
- 2 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _leafAppLayoutsToSpaceAppLayouts;
@"NSSet" _computedSetRepresentation;
```

## Properties

```
@property (T@"NSSet",R,C,N) setRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSpaceAppLayoutSet debugDescription];
-[SBSpaceAppLayoutSet succinctDescription];
-[SBSpaceAppLayoutSet hash];
-[SBSpaceAppLayoutSet description];
-[SBSpaceAppLayoutSet appendDescriptionToStream:];
-[SBSpaceAppLayoutSet copyWithZone:];
-[SBSpaceAppLayoutSet isEqual:];
-[SBSpaceAppLayoutSet setRepresentation];
-[SBSpaceAppLayoutSet _addSpaceAppLayout:];
-[SBSpaceAppLayoutSet _initWithLeafAppLayoutsToSpaceAppLayouts:];
-[SBSpaceAppLayoutSet initWithSpaceAppLayouts:];
-[SBSpaceAppLayoutSet spaceAppLayoutSetByAddingSpaceAppLayout:];
```
