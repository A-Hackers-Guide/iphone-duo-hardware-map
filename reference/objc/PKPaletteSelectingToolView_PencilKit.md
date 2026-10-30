# `PKPaletteSelectingToolView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteToolView`
- Protocols: `PKPaletteInkingTool`, `PKPaletteSelectingTool`
- 1 instance variables, 13 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<PKPaletteInkingTool>" _inkTool;
```

## Properties

```
@property (T@"<PKPaletteInkingTool>",&,N,V_inkTool) inkTool;
@property (T@"PKInk",R,N) ink;
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
-[PKPaletteSelectingToolView setSelected:];
-[PKPaletteSelectingToolView ink];
-[PKPaletteSelectingToolView setInkColor:];
-[PKPaletteSelectingToolView inkTool];
-[PKPaletteSelectingToolView attributeViewController];
-[PKPaletteSelectingToolView initWithToolIdentifier:itemIdentifier:variant:configuration:];
-[PKPaletteSelectingToolView setInkAzimuth:];
-[PKPaletteSelectingToolView setInkTool:];
-[PKPaletteSelectingToolView setInkWeight:];
```
