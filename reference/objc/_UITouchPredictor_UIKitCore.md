# `_UITouchPredictor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _predictions;
B _predictionsValid;
@"_UIValuePredictor" _xValuePredictor;
@"_UIValuePredictor" _yValuePredictor;
@"_UIValuePredictor" _angleValuePredictor;
@"_UIValuePredictor" _azimuthValuePredictor;
@"_UIValuePredictor" _forceValuePredictor;
d _averageTouchInterval;
d _lastTouchTimestamp;
[5d] _numPredictionsBuffer;
q _numPredictionsBufferCount;
@"_UITouchPredictorConfiguration" _configuration;
```

## Instance methods

```
-[_UITouchPredictor initWithConfiguration:];
-[_UITouchPredictor descriptionFromIndex:toIndex:includeHeader:includeDetailedConfidence:];
-[_UITouchPredictor predictedTouchesForTouch:];
-[_UITouchPredictor addTouch:];
-[_UITouchPredictor description];
-[_UITouchPredictor copyWithZone:];
-[_UITouchPredictor _dampenedNumPredictionsAtIndex:];
-[_UITouchPredictor _angleValuePredictor];
-[_UITouchPredictor _azimuthValuePredictor];
-[_UITouchPredictor _forceValuePredictor];
-[_UITouchPredictor _numPredictionsAtIndex:hardLimit:];
-[_UITouchPredictor _predictedTouchesAtIndex:forTouch:];
-[_UITouchPredictor _updatePredictionsForTouch:weight:];
-[_UITouchPredictor _xValuePredictor];
-[_UITouchPredictor _yValuePredictor];
-[_UITouchPredictor initWithTouchPredictor:];
```
