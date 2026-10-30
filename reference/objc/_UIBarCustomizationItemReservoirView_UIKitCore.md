# `_UIBarCustomizationItemReservoirView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDelegate`, `UICollectionViewDataSource`, `UICollectionViewDelegateFlowLayout`
- 11 instance variables, 12 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _computedInitialSize;
B _isEmpty;
B _isExpanded;
@"NSMutableArray" _items;
@"UIView" _arrowView;
@"UIView" _containerView;
@"_UIDiffuseShadowView" _shadowView;
@"UINavigationBar" _topBar;
@"UICollectionView" _collectionView;
@"UILabel" _tipLabel;
@"UILabel" _noContentLabel;
```

## Properties

```
@property (T@"UIView",&,N,V_arrowView) arrowView;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"_UIDiffuseShadowView",&,N,V_shadowView) shadowView;
@property (T@"UINavigationBar",&,N,V_topBar) topBar;
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"UILabel",&,N,V_tipLabel) tipLabel;
@property (T@"UILabel",&,N,V_noContentLabel) noContentLabel;
@property (T@"NSMutableArray",&,N,V_items) items;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIBarCustomizationItemReservoirView setContainerView:];
-[_UIBarCustomizationItemReservoirView collectionView:numberOfItemsInSection:];
-[_UIBarCustomizationItemReservoirView sizeToFit];
-[_UIBarCustomizationItemReservoirView _collectionView:layout:flowLayoutRowAlignmentOptionsForSection:];
-[_UIBarCustomizationItemReservoirView setResetAction:];
-[_UIBarCustomizationItemReservoirView setItems:];
-[_UIBarCustomizationItemReservoirView collectionView:cellForItemAtIndexPath:];
-[_UIBarCustomizationItemReservoirView collectionView];
-[_UIBarCustomizationItemReservoirView layoutSubviews];
-[_UIBarCustomizationItemReservoirView collectionView:layout:referenceSizeForHeaderInSection:];
-[_UIBarCustomizationItemReservoirView items];
-[_UIBarCustomizationItemReservoirView removeItem:];
-[_UIBarCustomizationItemReservoirView collectionView:layout:sizeForItemAtIndexPath:];
-[_UIBarCustomizationItemReservoirView containerView];
-[_UIBarCustomizationItemReservoirView setCollectionView:];
-[_UIBarCustomizationItemReservoirView shadowView];
-[_UIBarCustomizationItemReservoirView addItem:];
-[_UIBarCustomizationItemReservoirView setShadowView:];
-[_UIBarCustomizationItemReservoirView canBecomeFirstResponder];
-[_UIBarCustomizationItemReservoirView setExpanded:animated:];
-[_UIBarCustomizationItemReservoirView scrollViewDidScroll:];
-[_UIBarCustomizationItemReservoirView initWithItems:];
-[_UIBarCustomizationItemReservoirView scrollViewDidChangeContentSize:];
-[_UIBarCustomizationItemReservoirView invalidateLayoutAndForceUpdate:];
-[_UIBarCustomizationItemReservoirView _minimumLineSpacing];
-[_UIBarCustomizationItemReservoirView _popoverCornerRadius];
-[_UIBarCustomizationItemReservoirView _updateArrowColor];
-[_UIBarCustomizationItemReservoirView _updateEmptyState];
-[_UIBarCustomizationItemReservoirView arrowView];
-[_UIBarCustomizationItemReservoirView flowLayout];
-[_UIBarCustomizationItemReservoirView noContentLabel];
-[_UIBarCustomizationItemReservoirView setArrowView:];
-[_UIBarCustomizationItemReservoirView setDoneAction:];
-[_UIBarCustomizationItemReservoirView setNoContentLabel:];
-[_UIBarCustomizationItemReservoirView setTipLabel:];
-[_UIBarCustomizationItemReservoirView setTopBar:];
-[_UIBarCustomizationItemReservoirView tipLabel];
-[_UIBarCustomizationItemReservoirView topBar];
```
