# `_UIStatusBarRegionAxesLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarRegionLayout`
- 7 instance variables, 13 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"_UIStatusBarRegion" _region;
@"NSArray" _displayItems;
@"<_UIStatusBarRegionAxisLayout>" _horizontalLayout;
@"<_UIStatusBarRegionAxisLayout>" _verticalLayout;
@"NSArray" _horizontalConstraints;
@"NSArray" _verticalConstraints;
@"NSArray" _layoutGuides;
```

## Properties

```
@property (T@"NSArray",C,N,V_horizontalConstraints) horizontalConstraints;
@property (T@"NSArray",C,N,V_verticalConstraints) verticalConstraints;
@property (T@"NSArray",C,N,V_layoutGuides) layoutGuides;
@property (T@"<_UIStatusBarRegionAxisLayout>",&,N,V_horizontalLayout) horizontalLayout;
@property (T@"<_UIStatusBarRegionAxisLayout>",&,N,V_verticalLayout) verticalLayout;
@property (T@"_UIStatusBarRegion",W,N,V_region) region;
@property (T@"NSArray",C,N,V_displayItems) displayItems;
@property (TB,R,N) fitsAllItems;
@property (TB,R,N) canOverflowItems;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarRegionAxesLayout setRegion:];
-[_UIStatusBarRegionAxesLayout region];
-[_UIStatusBarRegionAxesLayout displayItems];
-[_UIStatusBarRegionAxesLayout setVerticalConstraints:];
-[_UIStatusBarRegionAxesLayout invalidate];
-[_UIStatusBarRegionAxesLayout setDisplayItems:];
-[_UIStatusBarRegionAxesLayout verticalConstraints];
-[_UIStatusBarRegionAxesLayout canOverflowItems];
-[_UIStatusBarRegionAxesLayout _updateConstraints];
-[_UIStatusBarRegionAxesLayout fitsAllItems];
-[_UIStatusBarRegionAxesLayout horizontalConstraints];
-[_UIStatusBarRegionAxesLayout horizontalLayout];
-[_UIStatusBarRegionAxesLayout layoutGuides];
-[_UIStatusBarRegionAxesLayout mayFitDisplayItems:inContainerItem:];
-[_UIStatusBarRegionAxesLayout setHorizontalConstraints:];
-[_UIStatusBarRegionAxesLayout setHorizontalLayout:];
-[_UIStatusBarRegionAxesLayout setLayoutGuides:];
-[_UIStatusBarRegionAxesLayout setVerticalLayout:];
-[_UIStatusBarRegionAxesLayout verticalLayout];
```
