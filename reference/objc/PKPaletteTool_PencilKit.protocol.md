# `PKPaletteTool` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) toolIdentifier;
@property (T@"NSString",R,N) itemIdentifier;
@property (T@"NSString",R,N) toolVariant;
@property (T@"PKToolConfiguration",R,N) configuration;
@property (T@"<PKPaletteInkingTool>",R,N) inkingTool;
@property (T@"<PKPaletteErasingTool>",R,N) erasingTool;
@property (T@"<PKPaletteHandwritingTool>",R,N) handwritingTool;
```

## Instance methods

```
-[PKPaletteTool configuration];
-[PKPaletteTool itemIdentifier];
-[PKPaletteTool toolIdentifier];
-[PKPaletteTool handwritingTool];
-[PKPaletteTool erasingTool];
-[PKPaletteTool inkingTool];
-[PKPaletteTool isCustomTool];
-[PKPaletteTool isErasingTool];
-[PKPaletteTool isGenerationTool];
-[PKPaletteTool isHandwritingTool];
-[PKPaletteTool isInkingTool];
-[PKPaletteTool isLassoTool];
-[PKPaletteTool isRulerTool];
-[PKPaletteTool toolVariant];
```
