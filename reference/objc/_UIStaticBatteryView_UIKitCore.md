# `_UIStaticBatteryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBatteryView`
- 1 instance variables, 0 properties, 17 instance methods, 10 class methods

## Instance variables

```
q _inflightBoltAnimationCount;
```

## Class methods

```
+[_UIStaticBatteryView _batteryBodyImageWithSize:forScale:batteryRect:cornerRadius:];
+[_UIStaticBatteryView _batteryBodyImageWithSize:forScale:batteryRect:cornerRadius:withBoltCutOutOfSize:inRect:boltFlipped:];
+[_UIStaticBatteryView _batteryBoltImageWithSize:boltSize:forScale:];
+[_UIStaticBatteryView _batteryBoltMaskImageWithSize:boltSize:forScale:];
+[_UIStaticBatteryView _batteryPinImageWithSize:forScale:complexPinPath:];
+[_UIStaticBatteryView _imageByPunchingImage:inRect:flippedHorizontally:outOfImage:inRect:size:scale:];
+[_UIStaticBatteryView _imageWithRenderedBezierPath:size:scale:pathScaleFactor:];
+[_UIStaticBatteryView _percentFillImageWithSize:forScale:batteryRect:cornerRadius:];
+[_UIStaticBatteryView _percentFillImageWithSize:forScale:batteryRect:cornerRadius:withBoltCutOutOfSize:inRect:boltFlipped:];
+[_UIStaticBatteryView _renderedImageOfSize:scale:withActions:];
```

## Instance methods

```
-[_UIStaticBatteryView _batteryBoltLargeScaleFactor];
-[_UIStaticBatteryView _batteryBoltSmallScaleFactor];
-[_UIStaticBatteryView _batteryPathScaleFactor];
-[_UIStaticBatteryView _boltPathSize];
-[_UIStaticBatteryView _boltRectForTraitCollection:boltSize:];
-[_UIStaticBatteryView _createBodyLayers];
-[_UIStaticBatteryView _createBoltLayersWithSize:];
-[_UIStaticBatteryView _createFillLayer];
-[_UIStaticBatteryView _didFinishAnimatingBoltToVisible:];
-[_UIStaticBatteryView _updateBatteryFillColor];
-[_UIStaticBatteryView _updateBodyColors];
-[_UIStaticBatteryView _updateBodyLayers];
-[_UIStaticBatteryView _updateFillLayer];
-[_UIStaticBatteryView _useImagesWithCutoutsForBolt];
-[_UIStaticBatteryView _willBeginAnimatingBoltToVisible:];
-[_UIStaticBatteryView setLowBatteryMode:];
-[_UIStaticBatteryView setShowsPercentage:];
```
