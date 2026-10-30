# `PKSqueezePaletteDrawingTool`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIPointerInteractionDelegate`
- 13 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"PKPaletteToolView" _toolView;
@"PKPaletteToolViewFactory" _factory;
@"UIView" _clippingView;
d _toolWidth;
d _toolOffsetY;
@"NSLayoutConstraint" _toolTopConstraint;
@"UIPointerInteraction" _pointerInteraction;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastRemoteEffectsFrame;
B _dragging;
B _allowHDR;
@"<PKSqueezePaletteDrawingToolDelegate>" _delegate;
@"PKTool" _tool;
q _colorAppearance;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKSqueezePaletteDrawingTool setSelected:];
-[PKSqueezePaletteDrawingTool pointerInteraction:styleForRegion:];
-[PKSqueezePaletteDrawingTool pointerInteraction:willEnterRegion:animator:];
-[PKSqueezePaletteDrawingTool pointerInteraction:willExitRegion:animator:];
-[PKSqueezePaletteDrawingTool pointerInteraction:regionForRequest:defaultRegion:];
-[PKSqueezePaletteDrawingTool pointInside:withEvent:];
```
