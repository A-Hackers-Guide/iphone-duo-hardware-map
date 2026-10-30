# `BKDisplayAnnotationRenderer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _shouldReapplyStyles;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"BKDisplayAnnotation" _annotation;
@"CALayer" _layer;
```

## Properties

```
@property (TB,R,N) shouldRenderWithSupernode;
@property (T@"BKDisplayAnnotation",W,N,V_annotation) annotation;
@property (T@"CALayer",&,N,V_layer) layer;
```

## Instance methods

```
-[BKDisplayAnnotationRenderer layer];
-[BKDisplayAnnotationRenderer annotation];
-[BKDisplayAnnotationRenderer displayRenderSpace];
-[BKDisplayAnnotationRenderer setAnnotation:];
-[BKDisplayAnnotationRenderer setLayer:];
-[BKDisplayAnnotationRenderer locationDidChange];
-[BKDisplayAnnotationRenderer didAddAnnotation];
-[BKDisplayAnnotationRenderer didRemoveAnnotation];
-[BKDisplayAnnotationRenderer didRemoveSubannotations];
-[BKDisplayAnnotationRenderer initWithDisplayRenderSpace:];
-[BKDisplayAnnotationRenderer regenerateLayerTree];
-[BKDisplayAnnotationRenderer shouldRenderWithSupernode];
-[BKDisplayAnnotationRenderer sizeLayerToFitAtScale:];
-[BKDisplayAnnotationRenderer styleSheetDidChange];
```
