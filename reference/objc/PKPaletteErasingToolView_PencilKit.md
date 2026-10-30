# `PKPaletteErasingToolView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteToolView`
- Protocols: `PKPaletteErasingTool`, `PKPaletteErasingAttributesViewControllerDelegate`
- 2 instance variables, 13 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _bitmapEraser;
@"PKPaletteAttributeViewController" _attributeViewController;
```

## Properties

```
@property (Td,R,N) weight;
@property (TB,N,GisBitmapEraser,V_bitmapEraser) bitmapEraser;
@property (T@"NSString",R,N) toolIdentifier;
@property (T@"NSString",R,N) itemIdentifier;
@property (T@"NSString",R,N) toolVariant;
@property (T@"PKToolConfiguration",R,N) configuration;
@property (T@"<PKPaletteInkingTool>",R,N) inkingTool;
@property (T@"<PKPaletteErasingTool>",R,N) erasingTool;
@property (T@"<PKPaletteHandwritingTool>",R,N) handwritingTool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteErasingToolView weight];
-[PKPaletteErasingToolView toolIdentifier];
-[PKPaletteErasingToolView _updateAttributesViewController];
-[PKPaletteErasingToolView _updateAttributesViewControllerWeight];
-[PKPaletteErasingToolView attributeViewController];
-[PKPaletteErasingToolView erasingAttributesViewControllerDidChangeErasingType:];
-[PKPaletteErasingToolView erasingAttributesViewControllerDidChangeInkThickness:];
-[PKPaletteErasingToolView initWithToolIdentifier:itemIdentifier:variant:configuration:];
-[PKPaletteErasingToolView isBitmapEraser];
-[PKPaletteErasingToolView setBitmapEraser:];
-[PKPaletteErasingToolView setToolProperties:];
-[PKPaletteErasingToolView setToolProperties:updateUI:];
```
