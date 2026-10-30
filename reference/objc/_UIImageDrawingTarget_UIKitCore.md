# `_UIImageDrawingTarget`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIImageContentRenderEnvironment`, `_UIImageContentLayoutTarget`
- 2 instance variables, 11 properties, 13 instance methods, 0 class methods

## Instance variables

```
d _preferredContentScaleFactor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"UITraitCollection",R,N) traitCollection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) semanticContentAttribute;
@property (Tq,R,N) contentMode;
@property (TB,R,N) _hasContentGravity;
@property (TB,R,N) _supportsContents;
@property (Td,R,N,V_preferredContentScaleFactor) preferredContentScaleFactor;
@property (TB,R,N) _layoutShouldFlipHorizontalOrientations;
```

## Instance methods

```
-[_UIImageDrawingTarget semanticContentAttribute];
-[_UIImageDrawingTarget contentMode];
-[_UIImageDrawingTarget traitCollection];
-[_UIImageDrawingTarget _effectsForRenderingSource:size:renditionContext:];
-[_UIImageDrawingTarget _additionalAlignmentRectInsetsForRenderingSource:];
-[_UIImageDrawingTarget _renderEnvironmentForSource:];
-[_UIImageDrawingTarget preferredContentScaleFactor];
-[_UIImageDrawingTarget _hasContentGravity];
-[_UIImageDrawingTarget _effectiveRenderingModeForSource:symbolConfiguration:];
-[_UIImageDrawingTarget _supportsContents];
-[_UIImageDrawingTarget _renditionForSource:effects:size:withContentProvider:renditionContext:];
-[_UIImageDrawingTarget _layoutShouldFlipHorizontalOrientations];
-[_UIImageDrawingTarget _symbolConfigurationForSource:];
```
