# `_UIButtonBarLayoutMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIButtonBarLayoutMetricsData`, `NSCopying`
- 6 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _locked;
B _allowsViewWrappers;
@"NSLayoutDimension" _verticalSizeGuide;
@"NSLayoutDimension" _minimumSpaceGuide;
@"NSLayoutDimension" _flexibleSpaceGuide;
@"NSLayoutDimension" _groupSizeGuide;
```

## Properties

```
@property (T@"NSLayoutDimension",&,N,V_verticalSizeGuide) verticalSizeGuide;
@property (T@"NSLayoutDimension",&,N,V_minimumSpaceGuide) minimumSpaceGuide;
@property (T@"NSLayoutDimension",&,N,V_flexibleSpaceGuide) flexibleSpaceGuide;
@property (T@"NSLayoutDimension",&,N,V_groupSizeGuide) groupSizeGuide;
@property (TB,N,V_allowsViewWrappers) allowsViewWrappers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIButtonBarLayoutMetrics setAllowsViewWrappers:];
-[_UIButtonBarLayoutMetrics description];
-[_UIButtonBarLayoutMetrics copyWithZone:];
-[_UIButtonBarLayoutMetrics allowsViewWrappers];
-[_UIButtonBarLayoutMetrics _copyWithModifications:];
-[_UIButtonBarLayoutMetrics _upcastIfReadOnly];
-[_UIButtonBarLayoutMetrics flexibleSpaceGuide];
-[_UIButtonBarLayoutMetrics groupSizeGuide];
-[_UIButtonBarLayoutMetrics minimumSpaceGuide];
-[_UIButtonBarLayoutMetrics setFlexibleSpaceGuide:];
-[_UIButtonBarLayoutMetrics setGroupSizeGuide:];
-[_UIButtonBarLayoutMetrics setMinimumSpaceGuide:];
-[_UIButtonBarLayoutMetrics setVerticalSizeGuide:];
-[_UIButtonBarLayoutMetrics verticalSizeGuide];
```
