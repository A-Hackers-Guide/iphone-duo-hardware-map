# `UIKBRecentInputsView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBKeyView`
- Protocols: `UICollectionViewDataSource`, `UICollectionViewDelegate`
- 4 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _verticalLayout;
@"UICollectionView" _collectionView;
@"NSArray" _recentInputStrings;
@"UICollectionViewFlowLayout" _flowLayout;
```

## Properties

```
@property (T@"UICollectionViewFlowLayout",&,N,V_flowLayout) flowLayout;
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"NSArray",&,N,V_recentInputStrings) recentInputStrings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBRecentInputsView initWithFrame:keyplane:key:];
-[UIKBRecentInputsView displayLayer:];
-[UIKBRecentInputsView collectionView:numberOfItemsInSection:];
-[UIKBRecentInputsView collectionView:cellForItemAtIndexPath:];
-[UIKBRecentInputsView collectionView];
-[UIKBRecentInputsView collectionView:layout:sizeForItemAtIndexPath:];
-[UIKBRecentInputsView setCollectionView:];
-[UIKBRecentInputsView scrollViewDidChangeContentSize:];
-[UIKBRecentInputsView flowLayout];
-[UIKBRecentInputsView focusableVariantCount];
-[UIKBRecentInputsView recentInputStrings];
-[UIKBRecentInputsView refreshSelectedRecent];
-[UIKBRecentInputsView selectedRecentInputString];
-[UIKBRecentInputsView setFlowLayout:];
-[UIKBRecentInputsView setRecentInputStrings:];
-[UIKBRecentInputsView setRecentInputs:];
-[UIKBRecentInputsView setVerticalLayout:];
-[UIKBRecentInputsView setupCollectionView];
```
