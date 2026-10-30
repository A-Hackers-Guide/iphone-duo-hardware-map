# `_UICollectionViewTypeSelectController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITypeSelectInteractionDelegate`
- 6 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="preferredItemsRange"{_NSRange="location"Q"length"Q}"numberOfItems"Q} _currentTypeSelectMetadata;
@"_UITypeSelectInteraction" _typeSelectInteraction;
@"_UITypeSelectResult" _typeSelectResult;
B _shouldApplyTypeSelectResultToCell;
B _enabled;
@"UICollectionView" _collectionView;
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
-[_UICollectionViewTypeSelectController _itemsForTypeSelectInteraction:forRange:];
-[_UICollectionViewTypeSelectController _metadataForTypeSelectInteraction:];
-[_UICollectionViewTypeSelectController _typeSelectInteraction:didUpdateResult:animator:];
```
