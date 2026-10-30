# `_UIStatusBarStaticBatteryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarBatteryView`
- 1 instance variables, 0 properties, 17 instance methods, 11 class methods

## Instance variables

```
q _inflightBoltAnimationCount;
```

## Class methods

```
+[_UIStatusBarStaticBatteryView _batteryBodyImageWithSize:forScale:batteryRect:cornerRadius:lineWidth:filled:];
+[_UIStatusBarStaticBatteryView _batteryBodyImageWithSize:forScale:batteryRect:cornerRadius:lineWidth:withBoltCutOutOfSize:inRect:boltFlipped:];
+[_UIStatusBarStaticBatteryView _batteryBoltImageWithSize:boltSize:forScale:];
+[_UIStatusBarStaticBatteryView _batteryBoltMaskImageWithSize:boltSize:forScale:];
+[_UIStatusBarStaticBatteryView _batteryFillImageWithSize:forScale:cornerRadius:];
+[_UIStatusBarStaticBatteryView _batteryFillImageWithSize:forScale:cornerRadius:withBoltCutOutOfSize:inRect:boltFlipped:];
+[_UIStatusBarStaticBatteryView _batteryPinImageWithSize:forScale:complexPinPath:];
+[_UIStatusBarStaticBatteryView _imageByPunchingImage:inRect:flippedHorizontally:outOfImage:inRect:size:scale:];
+[_UIStatusBarStaticBatteryView _imageWithRenderedBezierPath:size:scale:pathScaleFactor:stroke:fill:];
+[_UIStatusBarStaticBatteryView _percentFillImageWithSize:forScale:batteryRect:cornerRadius:lineWidth:];
+[_UIStatusBarStaticBatteryView _renderedImageOfSize:scale:withActions:];
```

## Instance methods

```
-[_UIStatusBarStaticBatteryView _batteryBoltLargeScaleFactor];
-[_UIStatusBarStaticBatteryView _batteryBoltSmallScaleFactor];
-[_UIStatusBarStaticBatteryView _batteryPathScaleFactor];
-[_UIStatusBarStaticBatteryView _boltPathSize];
-[_UIStatusBarStaticBatteryView _boltRectForTraitCollection:boltSize:];
-[_UIStatusBarStaticBatteryView _createBodyLayers];
-[_UIStatusBarStaticBatteryView _createBoltLayersWithSize:];
-[_UIStatusBarStaticBatteryView _createFillLayer];
-[_UIStatusBarStaticBatteryView _didFinishAnimatingBoltToVisible:];
-[_UIStatusBarStaticBatteryView _updateBatteryFillColor];
-[_UIStatusBarStaticBatteryView _updateBodyColors];
-[_UIStatusBarStaticBatteryView _updateBodyLayers];
-[_UIStatusBarStaticBatteryView _updateFillLayer];
-[_UIStatusBarStaticBatteryView _useImagesWithCutoutsForBolt];
-[_UIStatusBarStaticBatteryView _willBeginAnimatingBoltToVisible:];
-[_UIStatusBarStaticBatteryView setLowBatteryMode:];
-[_UIStatusBarStaticBatteryView setShowsPercentage:];
```
