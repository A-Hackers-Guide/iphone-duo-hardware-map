# `_UICollectionViewListCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewListCell`
- 1 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
q __backgroundViewConfigurationGrouping;
```

## Properties

```
@property (T@"NSArray",C,N) leadingAccessoryConfigurations;
@property (T@"NSArray",C,N) trailingAccessoryConfigurations;
@property (T@"NSArray",C,N) leadingEditingAccessoryConfigurations;
@property (T@"NSArray",C,N) trailingEditingAccessoryConfigurations;
@property (TB,N) indentsLeadingAccessories;
@property (T@"UILayoutGuide",R,N) _separatorLayoutGuide;
@property (Tq,D,N) selectionStyle;
@property (Tq,N,S_setBackgroundViewConfigurationGrouping:,V__backgroundViewConfigurationGrouping) _backgroundViewConfigurationGrouping;
@property (TB,D,N) expanded;
```

## Instance methods

```
-[_UICollectionViewListCell setExpanded:];
-[_UICollectionViewListCell expanded];
-[_UICollectionViewListCell _backgroundViewConfigurationGrouping];
-[_UICollectionViewListCell _configurationForListAccessoryType:];
-[_UICollectionViewListCell _customViewForAccessoryConfiguration:];
-[_UICollectionViewListCell _maskedCornersForSystemBackgroundView];
-[_UICollectionViewListCell _separatorLayoutGuide];
-[_UICollectionViewListCell _setAccessoryConfigurations:forAxis:];
-[_UICollectionViewListCell _setBackgroundViewConfigurationGrouping:];
-[_UICollectionViewListCell accessoryTypeForAxis:];
-[_UICollectionViewListCell accessoryViewForAxis:];
-[_UICollectionViewListCell indentsLeadingAccessories];
-[_UICollectionViewListCell setAccessoryType:forAxis:];
-[_UICollectionViewListCell setAccessoryView:forAxis:];
-[_UICollectionViewListCell setIndentsLeadingAccessories:];
```
