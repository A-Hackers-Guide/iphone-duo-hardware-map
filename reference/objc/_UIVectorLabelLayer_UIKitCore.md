# `_UIVectorLabelLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `CALayerDelegate`, `CAAnimationDelegate`
- 3 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _currentLayers;
@"_UIVectorTextLayout" _currentTextLayout;
Q _maxRenderedMoveDistance;
```

## Properties

```
@property (T@"_UIVectorTextLayout",C,D,N) textLayout;
@property (TQ,N,V_maxRenderedMoveDistance) maxRenderedMoveDistance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIVectorLabelLayer initialize];
```

## Instance methods

```
-[_UIVectorLabelLayer actionForLayer:forKey:];
-[_UIVectorLabelLayer didChangeValueForKey:];
-[_UIVectorLabelLayer init];
-[_UIVectorLabelLayer willChangeValueForKey:];
-[_UIVectorLabelLayer _applyTextLayoutChangeFrom:to:];
-[_UIVectorLabelLayer _cleanupUnusedLayers];
-[_UIVectorLabelLayer _findSimilarLayer:inLayers:];
-[_UIVectorLabelLayer _isPathCompatible:with:];
-[_UIVectorLabelLayer _layersForTextLayout:];
-[_UIVectorLabelLayer _transitionWithSetup:target:];
-[_UIVectorLabelLayer maxRenderedMoveDistance];
-[_UIVectorLabelLayer setMaxRenderedMoveDistance:];
```
