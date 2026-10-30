# `_UIStatusBarRegionAxisSquishyLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarRegionAxisLayout`
- 9 instance variables, 14 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _compressItems;
q _alignment;
d _interspace;
q _maxNumberOfItems;
q _maxNumberOfVisibleItems;
d _itemDynamicScale;
d _minItemDynamicScale;
d _minInterspaceDynamicScale;
@"<_UIStatusBarRegionAxisSquishyLayoutDynamicHidingDelegate>" _dynamicHidingDelegate;
```

## Properties

```
@property (Tq,N,V_alignment) alignment;
@property (TB,N,V_compressItems) compressItems;
@property (Td,N,V_interspace) interspace;
@property (Tq,N,V_maxNumberOfItems) maxNumberOfItems;
@property (Tq,N,V_maxNumberOfVisibleItems) maxNumberOfVisibleItems;
@property (Td,N,V_itemDynamicScale) itemDynamicScale;
@property (Td,N,V_minItemDynamicScale) minItemDynamicScale;
@property (Td,N,V_minInterspaceDynamicScale) minInterspaceDynamicScale;
@property (T@"<_UIStatusBarRegionAxisSquishyLayoutDynamicHidingDelegate>",W,N,V_dynamicHidingDelegate) dynamicHidingDelegate;
@property (TB,R,N) canOverflowItems;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarRegionAxisSquishyLayout maxNumberOfItems];
-[_UIStatusBarRegionAxisSquishyLayout interspace];
-[_UIStatusBarRegionAxisSquishyLayout init];
-[_UIStatusBarRegionAxisSquishyLayout setMinItemDynamicScale:];
-[_UIStatusBarRegionAxisSquishyLayout setMinInterspaceDynamicScale:];
-[_UIStatusBarRegionAxisSquishyLayout setAlignment:];
-[_UIStatusBarRegionAxisSquishyLayout setInterspace:];
-[_UIStatusBarRegionAxisSquishyLayout alignment];
-[_UIStatusBarRegionAxisSquishyLayout setItemDynamicScale:];
-[_UIStatusBarRegionAxisSquishyLayout setCompressItems:];
-[_UIStatusBarRegionAxisSquishyLayout minItemDynamicScale];
-[_UIStatusBarRegionAxisSquishyLayout minInterspaceDynamicScale];
-[_UIStatusBarRegionAxisSquishyLayout canOverflowItems];
-[_UIStatusBarRegionAxisSquishyLayout setMaxNumberOfVisibleItems:];
-[_UIStatusBarRegionAxisSquishyLayout compressItems];
-[_UIStatusBarRegionAxisSquishyLayout mayFitDisplayItems:inContainerItem:axis:];
-[_UIStatusBarRegionAxisSquishyLayout dynamicHidingDelegate];
-[_UIStatusBarRegionAxisSquishyLayout setMaxNumberOfItems:];
-[_UIStatusBarRegionAxisSquishyLayout setDynamicHidingDelegate:];
-[_UIStatusBarRegionAxisSquishyLayout itemDynamicScale];
-[_UIStatusBarRegionAxisSquishyLayout constraintsForDisplayItems:layoutGuides:inContainerItem:axis:];
-[_UIStatusBarRegionAxisSquishyLayout maxNumberOfVisibleItems];
```
