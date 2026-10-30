# `UIStatusBarBatteryItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarItemView`
- 11 instance variables, 7 properties, 24 instance methods, 0 class methods

## Instance variables

```
i _capacity;
i _state;
B _batterySaverModeActive;
@"UIView" _accessoryView;
B _cachedImageHasAccessoryImage;
i _cachedCapacity;
i _cachedAXHUDCapacity;
@"_UILegibilityImageSet" _cachedImageSet;
Q _cachedBatteryStyle;
Q _cachedAXHUDStyle;
@"UIImage" _cachedAXHUDImage;
```

## Properties

```
@property (T@"_UILegibilityImageSet",&,N,V_cachedImageSet) cachedImageSet;
@property (Ti,N,V_cachedCapacity) cachedCapacity;
@property (TB,N,V_cachedImageHasAccessoryImage) cachedImageHasAccessoryImage;
@property (TQ,N,V_cachedBatteryStyle) cachedBatteryStyle;
@property (Ti,N,V_cachedAXHUDCapacity) cachedAXHUDCapacity;
@property (TQ,N,V_cachedAXHUDStyle) cachedAXHUDStyle;
@property (T@"UIImage",&,N,V_cachedAXHUDImage) cachedAXHUDImage;
```

## Instance methods

```
-[UIStatusBarBatteryItemView accessibilityHUDRepresentation];
-[UIStatusBarBatteryItemView contentsImage];
-[UIStatusBarBatteryItemView legibilityStrength];
-[UIStatusBarBatteryItemView _accessoryImage];
-[UIStatusBarBatteryItemView _batteryOffsetWithBackground:];
-[UIStatusBarBatteryItemView _contentsImage];
-[UIStatusBarBatteryItemView _needsAccessoryImage];
-[UIStatusBarBatteryItemView _updateAccessoryImage];
-[UIStatusBarBatteryItemView cachedAXHUDCapacity];
-[UIStatusBarBatteryItemView cachedAXHUDImage];
-[UIStatusBarBatteryItemView cachedAXHUDStyle];
-[UIStatusBarBatteryItemView cachedBatteryStyle];
-[UIStatusBarBatteryItemView cachedCapacity];
-[UIStatusBarBatteryItemView cachedImageHasAccessoryImage];
-[UIStatusBarBatteryItemView cachedImageSet];
-[UIStatusBarBatteryItemView extraRightPadding];
-[UIStatusBarBatteryItemView setCachedAXHUDCapacity:];
-[UIStatusBarBatteryItemView setCachedAXHUDImage:];
-[UIStatusBarBatteryItemView setCachedAXHUDStyle:];
-[UIStatusBarBatteryItemView setCachedBatteryStyle:];
-[UIStatusBarBatteryItemView setCachedCapacity:];
-[UIStatusBarBatteryItemView setCachedImageHasAccessoryImage:];
-[UIStatusBarBatteryItemView setCachedImageSet:];
-[UIStatusBarBatteryItemView updateForNewData:actions:];
```
