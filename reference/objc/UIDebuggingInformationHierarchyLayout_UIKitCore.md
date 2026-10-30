# `UIDebuggingInformationHierarchyLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- 4 instance variables, 3 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _indexPathsToDelete;
@"<UIDebuggingInformationHierarchyLayoutDelegate>" _delegate;
@"NSDictionary" _allAttributes;
@"NSMutableDictionary" _allLineAttributes;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_allAttributes) allAttributes;
@property (T@"NSMutableDictionary",&,N,V_allLineAttributes) allLineAttributes;
@property (T@"<UIDebuggingInformationHierarchyLayoutDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[UIDebuggingInformationHierarchyLayout layoutAttributesClass];
```

## Instance methods

```
-[UIDebuggingInformationHierarchyLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[UIDebuggingInformationHierarchyLayout shouldInvalidateLayoutForBoundsChange:];
-[UIDebuggingInformationHierarchyLayout collectionViewContentSize];
-[UIDebuggingInformationHierarchyLayout setDelegate:];
-[UIDebuggingInformationHierarchyLayout delegate];
-[UIDebuggingInformationHierarchyLayout prepareForCollectionViewUpdates:];
-[UIDebuggingInformationHierarchyLayout invalidateLayout];
-[UIDebuggingInformationHierarchyLayout prepareLayout];
-[UIDebuggingInformationHierarchyLayout layoutAttributesForItemAtIndexPath:];
-[UIDebuggingInformationHierarchyLayout layoutAttributesForElementsInRect:];
-[UIDebuggingInformationHierarchyLayout _recomputeAttributes];
-[UIDebuggingInformationHierarchyLayout allAttributes];
-[UIDebuggingInformationHierarchyLayout allLineAttributes];
-[UIDebuggingInformationHierarchyLayout indexPathsToDeleteForSupplementaryViewOfKind:];
-[UIDebuggingInformationHierarchyLayout setAllAttributes:];
-[UIDebuggingInformationHierarchyLayout setAllLineAttributes:];
```
