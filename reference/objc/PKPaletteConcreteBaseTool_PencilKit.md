# `PKPaletteConcreteBaseTool`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKPaletteTool`
- 2 instance variables, 11 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"PKToolConfiguration" _cachedConfiguration;
@"NSString" _toolVariant;
```

## Properties

```
@property (T@"NSString",R,N) toolIdentifier;
@property (T@"NSString",R,N) itemIdentifier;
@property (T@"NSString",R,N,V_toolVariant) toolVariant;
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
-[PKPaletteConcreteBaseTool configuration];
-[PKPaletteConcreteBaseTool itemIdentifier];
-[PKPaletteConcreteBaseTool toolIdentifier];
-[PKPaletteConcreteBaseTool handwritingTool];
-[PKPaletteConcreteBaseTool erasingTool];
-[PKPaletteConcreteBaseTool inkingTool];
-[PKPaletteConcreteBaseTool isCustomTool];
-[PKPaletteConcreteBaseTool isErasingTool];
-[PKPaletteConcreteBaseTool isGenerationTool];
-[PKPaletteConcreteBaseTool isHandwritingTool];
-[PKPaletteConcreteBaseTool isInkingTool];
-[PKPaletteConcreteBaseTool isLassoTool];
-[PKPaletteConcreteBaseTool isRulerTool];
-[PKPaletteConcreteBaseTool toolVariant];
```
