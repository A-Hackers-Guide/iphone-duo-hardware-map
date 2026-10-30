# `SBAppLayout`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`, `SBSwitcherLayoutElementProviding`
- 14 instance variables, 14 properties, 74 instance methods, 4 class methods

## Instance variables

```
q _cachedAppLayoutType;
Q _cachedHash;
@"NSString" _continuousExposeIdentifier;
B _hidden;
B _isFlexibleWindowingEnabled;
@"NSString" _cached_uniqueIdentifier;
q _environment;
q _centerConfiguration;
@"SBDisplayItem" _centerItem;
q _preferredDisplayOrdinal;
@"SBFlexibleWindowingAutoLayoutSpace" _cachedLastFlexibleWindowingAutoLayoutSpace;
@"SBAppLayoutAutoLayoutSpaceCacheKey" _cachedLastOverlappingModelKey;
@"NSArray" _items;
@"NSArray" _itemsWithoutCenterItem;
```

## Properties

```
@property (Tq,R,N) type;
@property (Tq,R,N,V_environment) environment;
@property (TB,R,N,GisHidden,V_hidden) hidden;
@property (Tq,R,N,V_centerConfiguration) centerConfiguration;
@property (T@"SBDisplayItem",R,N,V_centerItem) centerItem;
@property (Tq,R,N,V_preferredDisplayOrdinal) preferredDisplayOrdinal;
@property (T@"NSString",R,C,N) continuousExposeIdentifier;
@property (T@"NSString",R,N,V_cached_uniqueIdentifier) uniqueIdentifier;
@property (T@"SBFlexibleWindowingAutoLayoutSpace",&,N,V_cachedLastFlexibleWindowingAutoLayoutSpace) cachedLastFlexibleWindowingAutoLayoutSpace;
@property (T@"SBAppLayoutAutoLayoutSpaceCacheKey",&,N,V_cachedLastOverlappingModelKey) cachedLastOverlappingModelKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAppLayout appLayoutWithProtobufRepresentation:layoutAttributesProvider:];
+[SBAppLayout appLibraryAppLayout];
+[SBAppLayout genericAppLayout];
+[SBAppLayout homeScreenAppLayout];
```

## Instance methods

```
-[SBAppLayout containsItem:];
-[SBAppLayout continuousExposeIdentifier];
-[SBAppLayout centerConfiguration];
-[SBAppLayout isAppLibrary];
-[SBAppLayout isFullScreen];
-[SBAppLayout appLayoutByAdjustingCenterWindowItemsForFlexibleWindowing];
-[SBAppLayout anyLeafAppLayout];
-[SBAppLayout initWithItemsForLayoutRoles:centerConfiguration:environment:hidden:preferredDisplayOrdinal:];
-[SBAppLayout leafAppLayoutForRole:];
-[SBAppLayout setCachedLastFlexibleWindowingAutoLayoutSpace:];
-[SBAppLayout appLayoutsBySplittingSingleAppModeIncompatibleAppLayouts];
-[SBAppLayout containsAnyItemFromAppLayout:];
-[SBAppLayout containsItemWithUniqueIdentifier:];
-[SBAppLayout succinctDescriptionBuilder];
-[SBAppLayout compare:];
-[SBAppLayout isAppLayout];
-[SBAppLayout init];
-[SBAppLayout isSplitConfiguration];
-[SBAppLayout appLayout];
-[SBAppLayout cachedLastFlexibleWindowingAutoLayoutSpace];
-[SBAppLayout initWithItemsForLayoutRoles:environment:hidden:preferredDisplayOrdinal:];
-[SBAppLayout isCenterOverSplit];
-[SBAppLayout appLayoutByInsertingItem:inLayoutRole:];
-[SBAppLayout isContainedWithinSet:];
-[SBAppLayout switcherLayoutElementType];
-[SBAppLayout itemsWithoutCenterItem];
-[SBAppLayout protobufRepresentationWithLayoutAttributesMap:layoutAttributesEntries:];
-[SBAppLayout hasSameItemsInLayoutRoles:asAppLayout:];
-[SBAppLayout isCenterOverFull];
-[SBAppLayout itemForLayoutRole:];
-[SBAppLayout leafAppLayouts];
-[SBAppLayout appLayoutByModifyingEnvironment:];
-[SBAppLayout descriptionWithMultilinePrefix:];
-[SBAppLayout setCachedLastOverlappingModelKey:];
-[SBAppLayout appLayoutByRemovingItemInLayoutRole:];
-[SBAppLayout uniqueIdentifier];
-[SBAppLayout appLayoutByInsertingItem:];
-[SBAppLayout initWithItems:centerItem:centerConfiguration:environment:hidden:preferredDisplayOrdinal:];
-[SBAppLayout isOrContainsAppLayout:];
-[SBAppLayout containsAllItemsFromSet:];
-[SBAppLayout appLayoutByModifyingHiddenState:];
-[SBAppLayout succinctDescription];
-[SBAppLayout appLibraryDisplayItem];
-[SBAppLayout isHidden];
-[SBAppLayout appLayoutByInsertingLeafAppLayout:inRole:];
-[SBAppLayout appLayoutByAdjustingFloatingItemsForFlexibleWindowing];
-[SBAppLayout type];
-[SBAppLayout containsAllItemsFromAppLayout:];
-[SBAppLayout leafAppLayoutsFromDisplayItems:];
-[SBAppLayout containsAllItemsFromArray:];
-[SBAppLayout initWithPlistRepresentation:layoutAttributesProvider:];
-[SBAppLayout _preferredWindowScene];
-[SBAppLayout preferredDisplayOrdinal];
-[SBAppLayout leafAppLayoutForItem:];
-[SBAppLayout hash];
-[SBAppLayout containsItemWithBundleIdentifier:];
-[SBAppLayout description];
-[SBAppLayout allItems];
-[SBAppLayout appLayoutWithItemsPassingTest:];
-[SBAppLayout cachedLastOverlappingModelKey];
-[SBAppLayout initWithItemsForLayoutRoles:environment:preferredDisplayOrdinal:];
-[SBAppLayout containsAnyItemFromSet:];
-[SBAppLayout appLayoutByModifyingPreferredDisplayOrdinal:];
-[SBAppLayout plistRepresentationWithLayoutAttributesMap:];
-[SBAppLayout copyWithZone:];
-[SBAppLayout centerItem];
-[SBAppLayout layoutRoleForItem:];
-[SBAppLayout isEqual:];
-[SBAppLayout preferredDisplayIdentity];
-[SBAppLayout _leafAppLayoutForItem:role:];
-[SBAppLayout anyItem];
-[SBAppLayout environment];
-[SBAppLayout enumerate:];
-[SBAppLayout descriptionBuilderWithMultilinePrefix:];
```
