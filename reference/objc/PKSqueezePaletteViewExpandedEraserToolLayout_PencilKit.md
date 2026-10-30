# `PKSqueezePaletteViewExpandedEraserToolLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSqueezePaletteViewLayout`
- 5 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"PKSqueezePaletteView" _paletteView;
@"NSArray" _attributeButtons;
@"PKSqueezePaletteViewExpandedEraserToolLayoutContext" _context;
@"NSArray" _layoutConstraints;
@"PKSqueezePaletteRoundedButton" _lastTappedAttributeButton;
```

## Properties

```
@property (T@"PKSqueezePaletteViewExpandedEraserToolLayoutContext",&,N,V_context) context;
@property (T@"NSArray",&,N,V_layoutConstraints) layoutConstraints;
@property (T@"PKSqueezePaletteRoundedButton",W,N,V_lastTappedAttributeButton) lastTappedAttributeButton;
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKSqueezePaletteViewExpandedEraserToolLayout setLayoutConstraints:];
-[PKSqueezePaletteViewExpandedEraserToolLayout setContext:];
-[PKSqueezePaletteViewExpandedEraserToolLayout layoutConstraints];
-[PKSqueezePaletteViewExpandedEraserToolLayout context];
-[PKSqueezePaletteViewExpandedEraserToolLayout setupUI];
-[PKSqueezePaletteViewExpandedEraserToolLayout updateUI];
-[PKSqueezePaletteViewExpandedEraserToolLayout setPaletteView:];
-[PKSqueezePaletteViewExpandedEraserToolLayout _didTapAttributeButton:];
-[PKSqueezePaletteViewExpandedEraserToolLayout _didTapDrawingTool:];
-[PKSqueezePaletteViewExpandedEraserToolLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewExpandedEraserToolLayout lastTappedAttributeButton];
-[PKSqueezePaletteViewExpandedEraserToolLayout paletteView];
-[PKSqueezePaletteViewExpandedEraserToolLayout setLastTappedAttributeButton:];
-[PKSqueezePaletteViewExpandedEraserToolLayout willTransitionToLayout:];
```
