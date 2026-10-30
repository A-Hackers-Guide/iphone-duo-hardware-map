# `AVMediaSelection`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 1 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"AVMediaSelectionInternal" _mediaSelection;
```

## Properties

```
@property (T@"AVAsset",R,W,N) asset;
```

## Instance methods

```
-[AVMediaSelection _internal];
-[AVMediaSelection asset];
-[AVMediaSelection mutableCopyWithZone:];
-[AVMediaSelection propertyList];
-[AVMediaSelection dealloc];
-[AVMediaSelection hash];
-[AVMediaSelection description];
-[AVMediaSelection copyWithZone:];
-[AVMediaSelection isEqual:];
-[AVMediaSelection initWithAsset:propertyList:];
-[AVMediaSelection _initWithAsset:];
-[AVMediaSelection _createDefaultMediaSelectionOptions];
-[AVMediaSelection _dictionaryGroupsWithSelectedOption];
-[AVMediaSelection _groupDictionaries];
-[AVMediaSelection _initWithAsset:mediaSelectionGroupDictionaries:selectedMediaArray:];
-[AVMediaSelection _initWithAsset:selectedMediaArray:];
-[AVMediaSelection _initWithAssetWithoutGroupDictionaries:];
-[AVMediaSelection _initWithDeferredLoadingOfAsset:selectedMediaArray:];
-[AVMediaSelection _loadiVarsIfNeeded];
-[AVMediaSelection _propertyListForSelectedMediaOptionInMediaSelectionGroup:];
-[AVMediaSelection _selectedMediaArray];
-[AVMediaSelection mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:];
-[AVMediaSelection selectedMediaOptionInMediaSelectionGroup:];
```
