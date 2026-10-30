# `_UICollectionViewListAccessoryControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UICollectionViewListDetailAccessoryView`
- 10 instance variables, 6 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _imageView;
@"UIView" _backgroundView;
B _needsImageViewUpdate;
B _nextImageViewUpdateShouldAnimate;
B _accessoryUsesMonochromaticTreatment;
q _type;
@"<UITableConstants>" _constants;
@? _actionHandler;
@"UIColor" _accessoryTintColor;
@"UIColor" _accessoryBackgroundColor;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"<UITableConstants>",&,N,V_constants) constants;
@property (T@"UIColor",&,N,V_accessoryTintColor) accessoryTintColor;
@property (T@"UIColor",&,N,V_accessoryBackgroundColor) accessoryBackgroundColor;
@property (TB,N,V_accessoryUsesMonochromaticTreatment) accessoryUsesMonochromaticTreatment;
@property (T@?,C,N,V_actionHandler) actionHandler;
```

## Instance methods

```
-[_UICollectionViewListAccessoryControl _controlEventsForActionTriggered];
-[_UICollectionViewListAccessoryControl _executeActionHandler];
-[_UICollectionViewListAccessoryControl setAccessoryUsesMonochromaticTreatment:];
-[_UICollectionViewListAccessoryControl setConstants:];
-[_UICollectionViewListAccessoryControl setSelected:];
-[_UICollectionViewListAccessoryControl _renderedImage];
-[_UICollectionViewListAccessoryControl setActionHandler:];
-[_UICollectionViewListAccessoryControl viewForLastBaselineLayout];
-[_UICollectionViewListAccessoryControl layoutSubviews];
-[_UICollectionViewListAccessoryControl actionHandler];
-[_UICollectionViewListAccessoryControl sizeThatFits:];
-[_UICollectionViewListAccessoryControl setHighlighted:];
-[_UICollectionViewListAccessoryControl setType:];
-[_UICollectionViewListAccessoryControl _updateImageViewIfNeeded];
-[_UICollectionViewListAccessoryControl type];
-[_UICollectionViewListAccessoryControl accessoryBackgroundColor];
-[_UICollectionViewListAccessoryControl _updateBackgroundViewIfNeeded];
-[_UICollectionViewListAccessoryControl viewForFirstBaselineLayout];
-[_UICollectionViewListAccessoryControl setSelected:isUserInitiated:];
-[_UICollectionViewListAccessoryControl accessoryUsesMonochromaticTreatment];
-[_UICollectionViewListAccessoryControl initWithType:constants:];
-[_UICollectionViewListAccessoryControl _setNeedsImageViewUpdate];
-[_UICollectionViewListAccessoryControl accessoryTintColor];
-[_UICollectionViewListAccessoryControl setAccessoryBackgroundColor:];
-[_UICollectionViewListAccessoryControl setAccessoryTintColor:];
-[_UICollectionViewListAccessoryControl constants];
```
