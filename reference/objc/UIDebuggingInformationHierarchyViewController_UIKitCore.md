# `UIDebuggingInformationHierarchyViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIDebuggingInformationTouchObserver`, `UICollectionViewDataSource`, `UIDebuggingInformationHierarchyLayoutDelegate`, `UICollectionViewDelegate`, `UIDebuggingInformationHierarchyCellDelegate`, `UIDebuggingInformationViewController`
- 14 instance variables, 16 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _showingOverlayItems;
@"NSArray" _normalItems;
@"NSMutableArray" _keys;
@"NSMutableDictionary" _managedValues;
@"NSMutableDictionary" _observersForKeys;
@"NSMutableDictionary" _controlsForKeys;
@"NSArray" _data;
@"UIView" _rootViewForInspection;
@"UIRefreshControl" _refreshControl;
@"UIView" _highlightedView;
@"UICollectionView" _collectionView;
^{CGColor=} _originalBorderColor;
d _originalBorderWidth;
@"UIDebuggingInformationInspectorDetailViewController" _detail;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_keys) keys;
@property (T@"NSMutableDictionary",&,N,V_managedValues) managedValues;
@property (T@"NSMutableDictionary",&,N,V_observersForKeys) observersForKeys;
@property (T@"NSMutableDictionary",&,N,V_controlsForKeys) controlsForKeys;
@property (T@"NSArray",&,N,V_data) data;
@property (T@"UIView",&,N,V_rootViewForInspection) rootViewForInspection;
@property (T@"UIRefreshControl",&,N,V_refreshControl) refreshControl;
@property (T@"UIView",&,N,V_highlightedView) highlightedView;
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T^{CGColor=},N,V_originalBorderColor) originalBorderColor;
@property (Td,N,V_originalBorderWidth) originalBorderWidth;
@property (T@"UIDebuggingInformationInspectorDetailViewController",&,N,V_detail) detail;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDebuggingInformationHierarchyViewController collectionView:numberOfItemsInSection:];
-[UIDebuggingInformationHierarchyViewController collectionView:didSelectItemAtIndexPath:];
-[UIDebuggingInformationHierarchyViewController viewWillDisappear:];
-[UIDebuggingInformationHierarchyViewController collectionView:cellForItemAtIndexPath:];
-[UIDebuggingInformationHierarchyViewController detail];
-[UIDebuggingInformationHierarchyViewController data];
-[UIDebuggingInformationHierarchyViewController collectionView];
-[UIDebuggingInformationHierarchyViewController setKeys:];
-[UIDebuggingInformationHierarchyViewController viewDidLoad];
-[UIDebuggingInformationHierarchyViewController viewDidLayoutSubviews];
-[UIDebuggingInformationHierarchyViewController initWithNibName:bundle:];
-[UIDebuggingInformationHierarchyViewController keys];
-[UIDebuggingInformationHierarchyViewController setCollectionView:];
-[UIDebuggingInformationHierarchyViewController viewWillAppear:];
-[UIDebuggingInformationHierarchyViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[UIDebuggingInformationHierarchyViewController setData:];
-[UIDebuggingInformationHierarchyViewController collectionView:viewForSupplementaryElementOfKind:atIndexPath:];
-[UIDebuggingInformationHierarchyViewController setDetail:];
-[UIDebuggingInformationHierarchyViewController setRefreshControl:];
-[UIDebuggingInformationHierarchyViewController refresh:];
-[UIDebuggingInformationHierarchyViewController highlightView:];
-[UIDebuggingInformationHierarchyViewController collectionView:didDeselectItemAtIndexPath:];
-[UIDebuggingInformationHierarchyViewController controlsForKeys];
-[UIDebuggingInformationHierarchyViewController highlightedView];
-[UIDebuggingInformationHierarchyViewController _showWindowChange];
-[UIDebuggingInformationHierarchyViewController chooseNewTarget:];
-[UIDebuggingInformationHierarchyViewController collapseBeneathCell:];
-[UIDebuggingInformationHierarchyViewController colorForIndentationLevel:];
-[UIDebuggingInformationHierarchyViewController didReceiveNewView:];
-[UIDebuggingInformationHierarchyViewController displayDetailsForCell:];
-[UIDebuggingInformationHierarchyViewController expandBeneathCell:];
-[UIDebuggingInformationHierarchyViewController getViewsRecursiveWithLevel:forView:];
-[UIDebuggingInformationHierarchyViewController indentationLevelForIndexPath:];
-[UIDebuggingInformationHierarchyViewController managedValues];
-[UIDebuggingInformationHierarchyViewController observersForKeys];
-[UIDebuggingInformationHierarchyViewController originalBorderColor];
-[UIDebuggingInformationHierarchyViewController originalBorderWidth];
-[UIDebuggingInformationHierarchyViewController refreshControl];
-[UIDebuggingInformationHierarchyViewController rootViewForInspection];
-[UIDebuggingInformationHierarchyViewController setControlsForKeys:];
-[UIDebuggingInformationHierarchyViewController setHighlightedView:];
-[UIDebuggingInformationHierarchyViewController setManagedValues:];
-[UIDebuggingInformationHierarchyViewController setObserversForKeys:];
-[UIDebuggingInformationHierarchyViewController setOriginalBorderColor:];
-[UIDebuggingInformationHierarchyViewController setOriginalBorderWidth:];
-[UIDebuggingInformationHierarchyViewController setRootViewForInspection:];
-[UIDebuggingInformationHierarchyViewController shouldCollapseAtIndexPath:];
-[UIDebuggingInformationHierarchyViewController shouldHighlightSelectedCells];
```
