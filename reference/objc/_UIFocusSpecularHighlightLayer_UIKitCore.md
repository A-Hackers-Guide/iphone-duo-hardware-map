# `_UIFocusSpecularHighlightLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _appliesFocusDirectionToContentsRect;
d _focusSpecularDepth;
d _focusScaleFactor;
d _legacyVerticalPositionOffset;
{CGVector="dx"d"dy"d} _focusBaseScaleAmounts;
{CGVector="dx"d"dy"d} _focusSensitivity;
```

## Properties

```
@property (Td,N,V_focusSpecularDepth) focusSpecularDepth;
@property (T{CGVector=dd},N,V_focusBaseScaleAmounts) focusBaseScaleAmounts;
@property (Td,N,V_focusScaleFactor) focusScaleFactor;
@property (T{CGVector=dd},N,V_focusSensitivity) focusSensitivity;
@property (TB,N,V_appliesFocusDirectionToContentsRect) appliesFocusDirectionToContentsRect;
@property (Td,N,V_legacyVerticalPositionOffset) legacyVerticalPositionOffset;
```

## Instance methods

```
-[_UIFocusSpecularHighlightLayer init];
-[_UIFocusSpecularHighlightLayer setContentsScale:];
-[_UIFocusSpecularHighlightLayer _effectiveFocusSensitivity];
-[_UIFocusSpecularHighlightLayer _updateSpecularLayerContents];
-[_UIFocusSpecularHighlightLayer appliesFocusDirectionToContentsRect];
-[_UIFocusSpecularHighlightLayer focusBaseScaleAmounts];
-[_UIFocusSpecularHighlightLayer focusScaleFactor];
-[_UIFocusSpecularHighlightLayer focusSensitivity];
-[_UIFocusSpecularHighlightLayer focusSpecularDepth];
-[_UIFocusSpecularHighlightLayer legacyVerticalPositionOffset];
-[_UIFocusSpecularHighlightLayer setAppliesFocusDirectionToContentsRect:];
-[_UIFocusSpecularHighlightLayer setFocusBaseScaleAmounts:];
-[_UIFocusSpecularHighlightLayer setFocusScaleFactor:];
-[_UIFocusSpecularHighlightLayer setFocusSensitivity:];
-[_UIFocusSpecularHighlightLayer setFocusSpecularDepth:];
-[_UIFocusSpecularHighlightLayer setLegacyVerticalPositionOffset:];
-[_UIFocusSpecularHighlightLayer updateForFocusDirection:isFocused:];
-[_UIFocusSpecularHighlightLayer updateTransformWithFocused:];
```
