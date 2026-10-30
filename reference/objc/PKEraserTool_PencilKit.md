# `PKEraserTool`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKTool`
- 0 instance variables, 3 properties, 12 instance methods, 5 class methods

## Properties

```
@property (Td,R,N) _weight;
@property (Tq,R,N) eraserType;
@property (Td,R,N) width;
```

## Class methods

```
+[PKEraserTool _weightForWidth:type:];
+[PKEraserTool _widthForWeight:type:];
+[PKEraserTool defaultWidthForEraserType:];
+[PKEraserTool maximumWidthForEraserType:];
+[PKEraserTool minimumWidthForEraserType:];
```

## Instance methods

```
-[PKEraserTool _weight];
-[PKEraserTool setWidth:];
-[PKEraserTool width];
-[PKEraserTool _width];
-[PKEraserTool _defaultItemIdentifier];
-[PKEraserTool _isEraserTool];
-[PKEraserTool _isFixedWidthBitmap];
-[PKEraserTool _toolPickerItemClass];
-[PKEraserTool eraserType];
-[PKEraserTool initWithEraserType:];
-[PKEraserTool initWithEraserType:weight:];
-[PKEraserTool initWithEraserType:width:];
```
