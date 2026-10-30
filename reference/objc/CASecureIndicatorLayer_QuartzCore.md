# `CASecureIndicatorLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 4 properties, 13 instance methods, 3 class methods

## Properties

```
@property (T@"NSString",C) privacyIndicatorType;
@property (Td) glyphScale;
@property (T@"NSArray",R) validPositions;
@property (T@"NSArray",R) validDynamicPositions;
```

## Class methods

```
+[CASecureIndicatorLayer defaultValueForKey:];
+[CASecureIndicatorLayer _hasRenderLayerSubclass];
+[CASecureIndicatorLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CASecureIndicatorLayer didChangeValueForKey:];
-[CASecureIndicatorLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CASecureIndicatorLayer _renderLayerDefinesProperty:];
-[CASecureIndicatorLayer setGlyphScale:];
-[CASecureIndicatorLayer glyphScale];
-[CASecureIndicatorLayer privacyIndicatorType];
-[CASecureIndicatorLayer remainingTimeAsSteadyForDisplay:];
-[CASecureIndicatorLayer remainingTimeToSteadyForDisplay:];
-[CASecureIndicatorLayer setPrivacyIndicatorType:];
-[CASecureIndicatorLayer validDynamicPositions];
-[CASecureIndicatorLayer validDynamicPositionsForDisplay:];
-[CASecureIndicatorLayer validPositions];
-[CASecureIndicatorLayer validPositionsForDisplay:];
```
