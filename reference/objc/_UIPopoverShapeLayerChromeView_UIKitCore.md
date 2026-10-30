# `_UIPopoverShapeLayerChromeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIPopoverStandardChromeView`
- 10 instance variables, 1 properties, 36 instance methods, 4 class methods

## Instance variables

```
@"UIVisualEffectView" _effectView;
@"_UIPopoverGlassBackground" _glassView;
@"UIView" _glassContentView;
q _requestedBackgroundStyle;
q _backgroundStyle;
B _popoverBackgroundColorIsOpaque;
B _arrowVisible;
@"_UIPopoverShapeLayerView" _shapeLayerMaskView;
@"_UIPopoverShapeLayerView" _shapeLayerStrokeView;
@"<_UIPopoverShapeLayerChromeViewDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIPopoverShapeLayerChromeViewDelegate>",W,N,V_delegate) _delegate;
```

## Class methods

```
+[_UIPopoverShapeLayerChromeView arrowBase];
+[_UIPopoverShapeLayerChromeView visualEffectGroupName];
+[_UIPopoverShapeLayerChromeView cornerRadius];
+[_UIPopoverShapeLayerChromeView arrowHeight];
```

## Instance methods

```
-[_UIPopoverShapeLayerChromeView _shadowRadius];
-[_UIPopoverShapeLayerChromeView didMoveToWindow];
-[_UIPopoverShapeLayerChromeView _shadowOpacity];
-[_UIPopoverShapeLayerChromeView setArrowDirection:];
-[_UIPopoverShapeLayerChromeView layoutSubviews];
-[_UIPopoverShapeLayerChromeView _delegate];
-[_UIPopoverShapeLayerChromeView backgroundStyle];
-[_UIPopoverShapeLayerChromeView _configureBackgroundView];
-[_UIPopoverShapeLayerChromeView set_delegate:];
-[_UIPopoverShapeLayerChromeView setArrowOffset:];
-[_UIPopoverShapeLayerChromeView setPopoverBackgroundColor:];
-[_UIPopoverShapeLayerChromeView initWithFrame:];
-[_UIPopoverShapeLayerChromeView setBackgroundStyle:];
-[_UIPopoverShapeLayerChromeView _traitCollectionForGlassContent];
-[_UIPopoverShapeLayerChromeView _pathParameters];
-[_UIPopoverShapeLayerChromeView _createStrokeView];
-[_UIPopoverShapeLayerChromeView _disableGlassForProcess];
-[_UIPopoverShapeLayerChromeView _effectiveBackgroundEffect];
-[_UIPopoverShapeLayerChromeView _loadNecessaryViews];
-[_UIPopoverShapeLayerChromeView _pinnedArrowSide];
-[_UIPopoverShapeLayerChromeView _removeBackgroundView];
-[_UIPopoverShapeLayerChromeView _resolvedBackgroundStyle];
-[_UIPopoverShapeLayerChromeView _setGlassContentView:];
-[_UIPopoverShapeLayerChromeView _setGlassContentViewFrame:];
-[_UIPopoverShapeLayerChromeView _shadowInsets];
-[_UIPopoverShapeLayerChromeView _shadowOffset];
-[_UIPopoverShapeLayerChromeView _shadowPath];
-[_UIPopoverShapeLayerChromeView _shouldUseGlassBackground];
-[_UIPopoverShapeLayerChromeView _updateBackgroundStyle];
-[_UIPopoverShapeLayerChromeView _updateShapeLayerPath];
-[_UIPopoverShapeLayerChromeView _updateStrokeViewColor];
-[_UIPopoverShapeLayerChromeView createShapeLayerPath];
-[_UIPopoverShapeLayerChromeView legacyBackgroundEffect];
-[_UIPopoverShapeLayerChromeView maxNonPinnedOffset];
-[_UIPopoverShapeLayerChromeView minNonPinnedOffset];
-[_UIPopoverShapeLayerChromeView usesImagesForShapeMasking];
```
