# `PKInkingTool`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKTool`
- 0 instance variables, 7 properties, 14 instance methods, 18 class methods

## Properties

```
@property (T@"NSString",R,N) localizedName;
@property (T@"NSString",R,N) inkType;
@property (T@"UIColor",R,N) color;
@property (Td,R,N) width;
@property (Td,R,N) azimuth;
@property (T@"PKInk",R,D,N) ink;
@property (Tq,R,N) requiredContentVersion;
```

## Class methods

```
+[PKInkingTool _calculateEdgeWidthForWeight:type:];
+[PKInkingTool _calculateWidthForWeight:type:];
+[PKInkingTool _computeWeightInfoMapFor:in:];
+[PKInkingTool _contextForStroke:weight:type:];
+[PKInkingTool _convertColorFromLight:toAppearance:];
+[PKInkingTool _isPureBlackOrWhite:];
+[PKInkingTool _isUsingSystemColorPicker];
+[PKInkingTool _weightForWidth:type:];
+[PKInkingTool _weightInfoMap];
+[PKInkingTool _widthForWeight:type:];
+[PKInkingTool behaviorForInkType:];
+[PKInkingTool convertColor:fromUserInterfaceStyle:to:];
+[PKInkingTool defaultColorForIdentifier:];
+[PKInkingTool defaultLocalizedNameForIdentifier:];
+[PKInkingTool defaultWidthForInkType:];
+[PKInkingTool invertColor:];
+[PKInkingTool maximumWidthForInkType:];
+[PKInkingTool minimumWidthForInkType:];
```

## Instance methods

```
-[PKInkingTool initWithInkType:color:];
-[PKInkingTool localizedName];
-[PKInkingTool requiredContentVersion];
-[PKInkingTool color];
-[PKInkingTool inkType];
-[PKInkingTool description];
-[PKInkingTool width];
-[PKInkingTool _width];
-[PKInkingTool azimuth];
-[PKInkingTool _defaultItemIdentifier];
-[PKInkingTool _toolPickerItemClass];
-[PKInkingTool initWithInk:width:];
-[PKInkingTool initWithInkType:color:width:];
-[PKInkingTool initWithInkType:color:width:azimuth:];
```
