# `PKSqueezePaletteViewExpandedInkingToolLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_PKColorAlphaSliderDelegate`, `PKSqueezePaletteViewLayout`
- 6 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"PKSqueezePaletteView" _paletteView;
@"NSArray" _strokeWeightButtons;
@"PKSqueezePaletteViewExpandedInkingToolLayoutContext" _context;
@"NSArray" _layoutConstraints;
@"PKSqueezePaletteStrokeWeightButton" _lastTappedStrokeWeightButton;
@"PKAngularOpacitySlider" _opacitySlider;
```

## Properties

```
@property (T@"PKSqueezePaletteViewExpandedInkingToolLayoutContext",&,N,V_context) context;
@property (T@"NSArray",C,N,V_strokeWeightButtons) strokeWeightButtons;
@property (T@"NSArray",&,N,V_layoutConstraints) layoutConstraints;
@property (T@"PKSqueezePaletteStrokeWeightButton",&,N,V_lastTappedStrokeWeightButton) lastTappedStrokeWeightButton;
@property (T@"PKAngularOpacitySlider",&,N,V_opacitySlider) opacitySlider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
```

## Instance methods

```
-[PKSqueezePaletteViewExpandedInkingToolLayout setLayoutConstraints:];
-[PKSqueezePaletteViewExpandedInkingToolLayout setContext:];
-[PKSqueezePaletteViewExpandedInkingToolLayout layoutConstraints];
-[PKSqueezePaletteViewExpandedInkingToolLayout context];
-[PKSqueezePaletteViewExpandedInkingToolLayout setupUI];
-[PKSqueezePaletteViewExpandedInkingToolLayout updateUI];
-[PKSqueezePaletteViewExpandedInkingToolLayout setPaletteView:];
-[PKSqueezePaletteViewExpandedInkingToolLayout _colorAlphaSliderUserDidChangeSlider:];
-[PKSqueezePaletteViewExpandedInkingToolLayout _didTapDrawingTool:];
-[PKSqueezePaletteViewExpandedInkingToolLayout _didTapStrokeWeightButton:];
-[PKSqueezePaletteViewExpandedInkingToolLayout colorAppearanceDidChange];
-[PKSqueezePaletteViewExpandedInkingToolLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewExpandedInkingToolLayout lastTappedStrokeWeightButton];
-[PKSqueezePaletteViewExpandedInkingToolLayout opacitySlider];
-[PKSqueezePaletteViewExpandedInkingToolLayout paletteView];
-[PKSqueezePaletteViewExpandedInkingToolLayout setLastTappedStrokeWeightButton:];
-[PKSqueezePaletteViewExpandedInkingToolLayout setOpacitySlider:];
-[PKSqueezePaletteViewExpandedInkingToolLayout setStrokeWeightButtons:];
-[PKSqueezePaletteViewExpandedInkingToolLayout willTransitionToLayout:];
```
