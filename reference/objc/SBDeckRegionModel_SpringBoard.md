# `SBDeckRegionModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSFastEnumeration`
- 7 instance variables, 7 properties, 17 instance methods, 1 class methods

## Instance variables

```
Q _hash;
@"NSSet" _unorderedLeafAppLayouts;
@"NSArray" _orderedLeafAppLayouts;
@"NSMapTable" _appLayoutsToMaskedSpaceIndices;
@"NSArray" _spaceAppLayouts;
q _screenRegion;
@"NSArray" _spaces;
```

## Properties

```
@property (T@"NSArray",R,N) appLayoutsArray;
@property (Tq,R,N) region;
@property (T@"NSArray",R,C,N,V_spaces) spaces;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDeckRegionModel emptySwitcher];
```

## Instance methods

```
-[SBDeckRegionModel region];
-[SBDeckRegionModel debugDescription];
-[SBDeckRegionModel succinctDescription];
-[SBDeckRegionModel countByEnumeratingWithState:objects:count:];
-[SBDeckRegionModel hash];
-[SBDeckRegionModel description];
-[SBDeckRegionModel appendDescriptionToStream:];
-[SBDeckRegionModel copyWithZone:];
-[SBDeckRegionModel isEqual:];
-[SBDeckRegionModel _appLayoutsToMaskedSpaceIndices];
-[SBDeckRegionModel appLayoutsArray];
-[SBDeckRegionModel _orderedLeafAppLayouts];
-[SBDeckRegionModel _spaceAppLayouts];
-[SBDeckRegionModel _unorderedLeafAppLayouts];
-[SBDeckRegionModel _updateCachesIfNeeded];
-[SBDeckRegionModel initWithAppLayouts:region:];
-[SBDeckRegionModel spaces];
```
