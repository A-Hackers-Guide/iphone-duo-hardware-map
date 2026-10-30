# `PKShapeDrawingTimerHelper`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKShapeDrawingControllerDelegate`
- 3 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<PKShapeDrawingTimerHelperDelegate>" _delegate;
@"PKShapeDrawingController" _shapeDrawingController;
@"NSTimer" _timer;
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
-[PKShapeDrawingTimerHelper initWithDelegate:];
-[PKShapeDrawingTimerHelper shapeDrawingControllerShapeGestureDetected:isFastGesture:];
-[PKShapeDrawingTimerHelper shapeDrawingControllerRendererController:];
-[PKShapeDrawingTimerHelper teardown];
-[PKShapeDrawingTimerHelper shapeDrawingControllerShapeDetectionCancelled:];
-[PKShapeDrawingTimerHelper addStrokePoint:inputPoint:];
-[PKShapeDrawingTimerHelper beginStrokeAtPoint:];
```
