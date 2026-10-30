# `CBAssetHelper`

- Image: [`/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`](../userland/System__Library__PrivateFrameworks__CoreBluetoothUI.framework__CoreBluetoothUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 7 instance methods, 10 class methods

## Instance variables

```
@"NSMutableDictionary" mDictCache;
```

## Class methods

```
+[CBAssetHelper strFromColorID:];
+[CBAssetHelper findLocalizedStringForKey:];
+[CBAssetHelper findLocalizedStringForKey:default:];
+[CBAssetHelper getAssetPathsFilenames];
+[CBAssetHelper loadAllAssets];
+[CBAssetHelper loadAssetsFromFile:];
+[CBAssetHelper resourcePathFromBundle:withResourceNamed:];
+[CBAssetHelper sharedAssetHelper];
+[CBAssetHelper strFromProductID:];
+[CBAssetHelper strFromVendorID:andProductID:];
```

## Instance methods

```
-[CBAssetHelper init];
-[CBAssetHelper getDeviceNameForAppleProductID:];
-[CBAssetHelper getAssetDictForAppleProductID:];
-[CBAssetHelper getCustomInfoForVID:andPID:];
-[CBAssetHelper getDeviceDisplayName:];
-[CBAssetHelper getImageURLForAppleProductID:andColor:];
-[CBAssetHelper getImageURLFromImageName:];
```
