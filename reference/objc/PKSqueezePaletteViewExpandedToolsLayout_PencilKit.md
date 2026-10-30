# `PKSqueezePaletteViewExpandedToolsLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSqueezePaletteViewLayout`
- 11 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
d _interToolSpace;
d _toolWidth;
@"PKFloatArray" _toolAngles;
@"NSArray" _toolCenterXConstraints;
@"NSArray" _toolCenterYConstraints;
@"PKSqueezePaletteView" _paletteView;
@"<PKSqueezePaletteViewExpandedToolsLayoutDelegate>" _delegate;
@"PKSqueezePaletteViewExpandedToolsLayoutContext" _context;
@"NSArray" _drawingTools;
Q _selectedToolIndex;
Q _visibleToolsCount;
```

## Properties

```
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKSqueezePaletteViewExpandedToolsLayout setupUI];
-[PKSqueezePaletteViewExpandedToolsLayout updateUI];
-[PKSqueezePaletteViewExpandedToolsLayout setPaletteView:];
-[PKSqueezePaletteViewExpandedToolsLayout _didTapDrawingTool:];
-[PKSqueezePaletteViewExpandedToolsLayout colorAppearanceDidChange];
-[PKSqueezePaletteViewExpandedToolsLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewExpandedToolsLayout paletteView];
-[PKSqueezePaletteViewExpandedToolsLayout willTransitionToLayout:];
```
