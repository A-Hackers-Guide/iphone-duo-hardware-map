# `_UICollectionViewListAccessoryDisclosure`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIMenuForcedAutomaticSelectionDelegate`, `_UICollectionViewListAccessoryDisclosureView`
- 10 instance variables, 14 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _imageView;
B _accessoryUsesMonochromaticTreatment;
B _rotated;
@"UIImage" _image;
@"<UITableConstants>" _constants;
@"UIColor" _accessoryTintColor;
@? _actionHandler;
d _rotationAngle;
@"UIMenu" _menu;
@? _selectedElementDidChangeHandler;
```

## Properties

```
@property (T@"UIMenu",&,N,V_menu) menu;
@property (T@?,C,N,V_selectedElementDidChangeHandler) selectedElementDidChangeHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIControl",R,N) control;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"<UITableConstants>",&,N,V_constants) constants;
@property (T@"UIColor",&,N,V_accessoryTintColor) accessoryTintColor;
@property (TB,N,V_accessoryUsesMonochromaticTreatment) accessoryUsesMonochromaticTreatment;
@property (T@?,C,N,V_actionHandler) actionHandler;
@property (TB,N,V_rotated) rotated;
@property (Td,N,V_rotationAngle) rotationAngle;
```

## Instance methods

```
-[_UICollectionViewListAccessoryDisclosure menu];
-[_UICollectionViewListAccessoryDisclosure _controlEventsForActionTriggered];
-[_UICollectionViewListAccessoryDisclosure _executeActionHandler];
-[_UICollectionViewListAccessoryDisclosure setAccessoryUsesMonochromaticTreatment:];
-[_UICollectionViewListAccessoryDisclosure setConstants:];
-[_UICollectionViewListAccessoryDisclosure rotationAngle];
-[_UICollectionViewListAccessoryDisclosure _updateRotation];
-[_UICollectionViewListAccessoryDisclosure contextMenuInteraction:configurationForMenuAtLocation:];
-[_UICollectionViewListAccessoryDisclosure setActionHandler:];
-[_UICollectionViewListAccessoryDisclosure _minimumSizeForHitTesting];
-[_UICollectionViewListAccessoryDisclosure viewForLastBaselineLayout];
-[_UICollectionViewListAccessoryDisclosure layoutSubviews];
-[_UICollectionViewListAccessoryDisclosure setSelectedElementDidChangeHandler:];
-[_UICollectionViewListAccessoryDisclosure setBounds:];
-[_UICollectionViewListAccessoryDisclosure initWithConstants:handlesOwnAction:];
-[_UICollectionViewListAccessoryDisclosure actionHandler];
-[_UICollectionViewListAccessoryDisclosure sizeThatFits:];
-[_UICollectionViewListAccessoryDisclosure _enforcedWidthForWidth:];
-[_UICollectionViewListAccessoryDisclosure viewForFirstBaselineLayout];
-[_UICollectionViewListAccessoryDisclosure setFrame:];
-[_UICollectionViewListAccessoryDisclosure accessoryUsesMonochromaticTreatment];
-[_UICollectionViewListAccessoryDisclosure control];
-[_UICollectionViewListAccessoryDisclosure setRotationAngle:];
-[_UICollectionViewListAccessoryDisclosure accessoryTintColor];
-[_UICollectionViewListAccessoryDisclosure rotated];
-[_UICollectionViewListAccessoryDisclosure setRotated:];
-[_UICollectionViewListAccessoryDisclosure forcedSelectionOfMenu:willChangeTo:];
-[_UICollectionViewListAccessoryDisclosure image];
-[_UICollectionViewListAccessoryDisclosure setAccessoryTintColor:];
-[_UICollectionViewListAccessoryDisclosure constants];
-[_UICollectionViewListAccessoryDisclosure selectedElementDidChangeHandler];
-[_UICollectionViewListAccessoryDisclosure setMenu:];
-[_UICollectionViewListAccessoryDisclosure setImage:];
```
