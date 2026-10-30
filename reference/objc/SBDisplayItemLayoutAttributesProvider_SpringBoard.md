# `SBDisplayItemLayoutAttributesProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayItemLayoutAttributesProviding`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayItemLayoutAttributesStorage" _storage;
B _isPerformingWithoutUpdating;
@"<BSInvalidatable>" _stateCaptureBlockInvalidatable;
@"NSMutableDictionary" _splitIdentifiersToDisplayItems;
@"<SBDisplayItemLayoutAttributesProviderDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBDisplayItemLayoutAttributesProviderDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayItemLayoutAttributesProvider init];
-[SBDisplayItemLayoutAttributesProvider dealloc];
-[SBDisplayItemLayoutAttributesProvider displayItemsForSplitIdentifier:];
-[SBDisplayItemLayoutAttributesProvider setDelegate:];
-[SBDisplayItemLayoutAttributesProvider delegate];
-[SBDisplayItemLayoutAttributesProvider _shouldUpdateForDisplayOrdinal:];
-[SBDisplayItemLayoutAttributesProvider _layoutAttributesForDisplayItem:displayOrdinal:orientation:];
-[SBDisplayItemLayoutAttributesProvider lastInteractedDisplayItemInAppLayout:orientation:passingTest:];
-[SBDisplayItemLayoutAttributesProvider lastInteractedDisplayItemsInAppLayout:orientation:];
-[SBDisplayItemLayoutAttributesProvider layoutAttributesEntriesForAppLayout:];
-[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:displayOrdinal:orientation:];
-[SBDisplayItemLayoutAttributesProvider layoutAttributesMapForAppLayout:displayOrdinal:orientation:];
-[SBDisplayItemLayoutAttributesProvider performBlockWithoutUpdating:];
-[SBDisplayItemLayoutAttributesProvider updateEntriesWithBlock:];
-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:forKey:];
-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:];
-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributesMap:forDisplayOrdinal:orientation:];
-[SBDisplayItemLayoutAttributesProvider zOrderedItemsInAppLayout:orientation:];
```
