# `PKTool`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 23 instance methods, 4 class methods

## Instance variables

```
@"PKToolConfiguration" _configuration;
@"NSString" _toolPickerItemIdentifier;
@"PKInk" _ink;
@? __barButtonItemsProvider;
```

## Properties

```
@property (T@"NSString",C,N,S_setToolPickerItemIdentifier:,V_toolPickerItemIdentifier) _toolPickerItemIdentifier;
@property (T@"PKInk",R,N,V_ink) ink;
@property (T@"PKToolConfiguration",R,N,V_configuration) _configuration;
@property (T@?,C,N,S_setBarButtonItemsProvider:,V__barButtonItemsProvider) _barButtonItemsProvider;
```

## Class methods

```
+[PKTool _inkIsInkingTool:];
+[PKTool _toolWithInk:];
+[PKTool _toolWithInk:configuration:];
+[PKTool _toolWithTool:color:ignoringOpacity:];
```

## Instance methods

```
-[PKTool _color];
-[PKTool _configuration];
-[PKTool ink];
-[PKTool hash];
-[PKTool copyWithZone:];
-[PKTool isEqual:];
-[PKTool _width];
-[PKTool _copyWithColor:];
-[PKTool _toolPickerItem];
-[PKTool _barButtonItemsProvider];
-[PKTool _copyWithStrokeWeight:];
-[PKTool _defaultItemIdentifier];
-[PKTool _initWithInk:];
-[PKTool _initWithInk:configuration:];
-[PKTool _isEraserTool];
-[PKTool _isHandwritingTool];
-[PKTool _isLassoTool];
-[PKTool _isRulerTool];
-[PKTool _setBarButtonItemsProvider:];
-[PKTool _setToolPickerItemIdentifier:];
-[PKTool _strokeWeight];
-[PKTool _toolPickerItemClass];
-[PKTool _toolPickerItemIdentifier];
```
