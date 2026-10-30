# `UICollectionViewData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"UICollectionView" _collectionView;
@"UICollectionViewLayout" _layout;
@"_UIMutableFastIndexSet" _globalIndexesOfItemsAwaitingValidation;
@"NSMutableDictionary" _supplementaryLayoutAttributes;
@"NSMutableDictionary" _decorationLayoutAttributes;
@"NSMutableDictionary" _invalidatedSupplementaryIndexPaths;
@"NSMutableDictionary" _invalidatedDecorationIndexPaths;
q _lastSectionTestedForNumberOfItemsBeforeSection;
q _lastResultForNumberOfItemsBeforeSection;
{CGSize="width"d"height"d} _contentSize;
{?="contentSizeIsValid"b1"itemCountsAreValid"b1"layoutIsPreparing"b1"layoutIsPrepared"b1"layoutLocked"b1} _collectionViewDataFlags;
{vector<long, std::allocator<long>>="__begin_"^q"__end_"^q""{?="__cap_"^q}} _sectionItemCounts;
{unordered_map<long, UICollectionViewLayoutAttributes *, std::hash<long>, std::equal_to<long>, std::allocator<std::pair<const long, UICollectionViewLayoutAttributes *>>>="__table_"{__hash_table<std::__hash_value_type<long, UICollectionViewLayoutAttributes *>, std::__unordered_map_hasher<long, std::pair<const long, UICollectionViewLayoutAttributes *>, std::hash<long>, std::equal_to<long>>, std::__unordered_map_equal<long, std::pair<const long, UICollectionViewLayoutAttributes *>, std::equal_to<long>, std::hash<long>>, std::allocator<std::pair<const long, UICollectionViewLayoutAttributes *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, UICollectionViewLayoutAttributes *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, UICollectionViewLayoutAttributes *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, UICollectionViewLayoutAttributes *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<long, UICollectionViewLayoutAttributes *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _globalItemMap;
q _totalItemCount;
@"_UICollectionViewDataAttributesMap" _attributesMap;
Q _preUpdateCachedItemCount;
@"NSArray" _clonedCellAttributes;
@"NSArray" _clonedSupplementaryAttributes;
@"NSArray" _clonedDecorationAttributes;
```

## Instance methods

```
-[UICollectionViewData _TEST_validLayoutRect];
```
