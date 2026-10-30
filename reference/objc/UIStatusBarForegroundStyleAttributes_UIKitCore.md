# `UIStatusBarForegroundStyleAttributes`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 2 properties, 63 instance methods, 0 class methods

## Instance variables

```
d _height;
q _legibilityStyle;
q _idiom;
@"NSMutableDictionary" _cachedFonts;
B _isTintColorBlack;
B _hasBusyBackground;
@"NSString" _cachedUniqueIdentifier;
B _canShowBreadcrumbs;
@"UIColor" _tintColor;
```

## Properties

```
@property (TB,N,V_canShowBreadcrumbs) canShowBreadcrumbs;
@property (T@"UIColor",R,&,N,V_tintColor) tintColor;
```

## Instance methods

```
-[UIStatusBarForegroundStyleAttributes uniqueIdentifier];
-[UIStatusBarForegroundStyleAttributes scale];
-[UIStatusBarForegroundStyleAttributes legibilityStyle];
-[UIStatusBarForegroundStyleAttributes tintColor];
-[UIStatusBarForegroundStyleAttributes imageNamed:];
-[UIStatusBarForegroundStyleAttributes copyWithZone:];
-[UIStatusBarForegroundStyleAttributes height];
-[UIStatusBarForegroundStyleAttributes idiom];
-[UIStatusBarForegroundStyleAttributes leftEdgePadding];
-[UIStatusBarForegroundStyleAttributes standardPadding];
-[UIStatusBarForegroundStyleAttributes _batteryColorForCapacity:lowCapacity:style:usingTintColor:];
-[UIStatusBarForegroundStyleAttributes _cacheImage:named:];
-[UIStatusBarForegroundStyleAttributes _cacheQueue_cacheImage:named:inTempGroup:groupFullName:tintColor:];
-[UIStatusBarForegroundStyleAttributes _cacheQueue_cachedImageNamed:inTempGroup:groupFullName:];
-[UIStatusBarForegroundStyleAttributes _cachedImageNamed:];
-[UIStatusBarForegroundStyleAttributes _drawText:inRect:withFont:lineBreakMode:letterSpacing:textAlignment:];
-[UIStatusBarForegroundStyleAttributes _roundDimension:];
-[UIStatusBarForegroundStyleAttributes _shouldUseBoldFontForStyle:];
-[UIStatusBarForegroundStyleAttributes accessibilityHUDImageNamed:];
-[UIStatusBarForegroundStyleAttributes activityIndicatorStyleWithSyncActivity:];
-[UIStatusBarForegroundStyleAttributes baselineOffsetForStyle:];
-[UIStatusBarForegroundStyleAttributes batteryAccessoryMargin];
-[UIStatusBarForegroundStyleAttributes batteryColorForCapacity:style:usingTintColor:];
-[UIStatusBarForegroundStyleAttributes bluetoothBatteryColorForCapacity:usingTintColor:];
-[UIStatusBarForegroundStyleAttributes bluetoothBatteryExtraPadding];
-[UIStatusBarForegroundStyleAttributes bluetoothBatteryImageNameWithCapacity:];
-[UIStatusBarForegroundStyleAttributes cacheImage:named:inTempGroup:];
-[UIStatusBarForegroundStyleAttributes cachedImageNamed:inTempGroup:];
-[UIStatusBarForegroundStyleAttributes cachedImageWithText:forWidth:lineBreakMode:letterSpacing:textAlignment:style:itemType:];
-[UIStatusBarForegroundStyleAttributes canShowBreadcrumbs];
-[UIStatusBarForegroundStyleAttributes drawBatteryInsidesWithSize:capacity:style:];
-[UIStatusBarForegroundStyleAttributes drawBatteryInsidesWithSize:capacity:style:usingTintColor:];
-[UIStatusBarForegroundStyleAttributes drawBluetoothBatteryInsidesWithSize:capacity:];
-[UIStatusBarForegroundStyleAttributes drawText:forWidth:lineBreakMode:letterSpacing:textAlignment:style:textSize:textHeight:];
-[UIStatusBarForegroundStyleAttributes drawTextInRect:withColor:withBlock:];
-[UIStatusBarForegroundStyleAttributes edgeInsetsForBatteryInsides];
-[UIStatusBarForegroundStyleAttributes edgeInsetsForBluetoothBatteryInsides];
-[UIStatusBarForegroundStyleAttributes expandedNameForImageName:];
-[UIStatusBarForegroundStyleAttributes generateUniqueIdentifier];
-[UIStatusBarForegroundStyleAttributes imageIdWithText:forWidth:lineBreakMode:letterSpacing:style:];
-[UIStatusBarForegroundStyleAttributes imageNamed:withLegibilityStyle:legibilityStrength:];
-[UIStatusBarForegroundStyleAttributes imageWithText:ofItemType:forWidth:lineBreakMode:letterSpacing:textAlignment:style:withLegibilityStyle:legibilityStrength:];
-[UIStatusBarForegroundStyleAttributes imageWithText:ofItemType:forWidth:lineBreakMode:letterSpacing:textAlignment:style:withLegibilityStyle:legibilityStrength:shouldCache:];
-[UIStatusBarForegroundStyleAttributes initWithHeight:legibilityStyle:tintColor:hasBusyBackground:];
-[UIStatusBarForegroundStyleAttributes initWithHeight:legibilityStyle:tintColor:hasBusyBackground:idiom:];
-[UIStatusBarForegroundStyleAttributes makeTextFontForStyle:];
-[UIStatusBarForegroundStyleAttributes middlePadding];
-[UIStatusBarForegroundStyleAttributes positionForMoonMaskInBounds:];
-[UIStatusBarForegroundStyleAttributes rightEdgePadding];
-[UIStatusBarForegroundStyleAttributes setCanShowBreadcrumbs:];
-[UIStatusBarForegroundStyleAttributes shadowImageForImage:withIdentifier:forStyle:withStrength:];
-[UIStatusBarForegroundStyleAttributes shadowImageForImage:withIdentifier:forStyle:withStrength:inTempGroup:];
-[UIStatusBarForegroundStyleAttributes shadowImageForImage:withIdentifier:forStyle:withStrength:inTempGroup:shouldCache:];
-[UIStatusBarForegroundStyleAttributes shadowPadding];
-[UIStatusBarForegroundStyleAttributes sizeForMoonMaskVisible:];
-[UIStatusBarForegroundStyleAttributes supportsShowingBuildVersion];
-[UIStatusBarForegroundStyleAttributes textColorForStyle:];
-[UIStatusBarForegroundStyleAttributes textFontForStyle:];
-[UIStatusBarForegroundStyleAttributes textForNetworkType:];
-[UIStatusBarForegroundStyleAttributes textOffsetForStyle:];
-[UIStatusBarForegroundStyleAttributes uncachedImageNamed:];
-[UIStatusBarForegroundStyleAttributes untintedImageNamed:];
-[UIStatusBarForegroundStyleAttributes usesVerticalLayout];
```
