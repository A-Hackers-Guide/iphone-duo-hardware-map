# `PKStrokeSpatialCache`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
B _hasValidOnscreenVisibleStrokes;
@"<PKStrokeSpatialCacheDelegate>" _delegate;
@"NSArray" _onscreenVisibleStrokes;
@? _generateOnscreenVisibleStrokesBlock;
@"NSObject<OS_dispatch_queue>" _onscreenVisibleStrokesQueue;
q _currentGenerationCount;
@"PKDrawing" _cachedDrawing;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedBounds;
```

## Instance methods

```
-[PKStrokeSpatialCache init];
-[PKStrokeSpatialCache dealloc];
```
