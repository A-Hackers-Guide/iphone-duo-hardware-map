# `BKUICurvesView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `NSXMLParserDelegate`, `CAAnimationDelegate`
- 21 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _pathLayers;
@"UIColor" _color;
d _lineWidth;
@"NSString" _lineCap;
Q _currentLayer;
Q _preEstimateLayer;
f _progress;
B _estimateFailed;
B _estimating;
@"CABasicAnimation" _lastAnimation;
d _lastRatio;
{CGSize="width"d"height"d} _lastFrameSize;
@"NSCondition" _initCondition;
B _inited;
@"NSXMLParser" _parser;
@"UIBezierPath" _wholePath;
@"NSMutableArray" _paths;
@"CAShapeLayer" _fingerLayer;
@"NSNumber" _speed;
@"NSObject<OS_os_log>" _log;
{CGSize="width"d"height"d} _sublayerSize;
```

## Properties

```
@property (T{CGSize=dd},N,V_sublayerSize) sublayerSize;
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (T@"NSNumber",&,V_speed) speed;
@property (Tf) progress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKUICurvesView setLog:];
-[BKUICurvesView setSpeed:];
-[BKUICurvesView animationDidStop:finished:];
-[BKUICurvesView setProgress:];
-[BKUICurvesView speed];
-[BKUICurvesView dealloc];
-[BKUICurvesView progress];
-[BKUICurvesView log];
-[BKUICurvesView parser:didStartElement:namespaceURI:qualifiedName:attributes:];
-[BKUICurvesView _resetEstimate:];
-[BKUICurvesView _addEstimateWatchDog];
-[BKUICurvesView _animateEstimateFailure];
-[BKUICurvesView _animateFromLayer:toLayer:withColor:];
-[BKUICurvesView _animateFromLayer:toProgress:withColor:];
-[BKUICurvesView _checkEstimateFailedAfterAnimation:];
-[BKUICurvesView _getPoint:];
-[BKUICurvesView _path:drawCurveToPoint:controlPoint1:controlPoint2:];
-[BKUICurvesView _path:drawLineToPoint:];
-[BKUICurvesView _removeEstimateWatchDog];
-[BKUICurvesView _resetLayers];
-[BKUICurvesView _startAnimation:withColor:isLast:];
-[BKUICurvesView _waitForInit];
-[BKUICurvesView estimateFailed];
-[BKUICurvesView estimateProgress:];
-[BKUICurvesView loadDataFromXML:name:color:];
-[BKUICurvesView newQuartzPath:transform:];
-[BKUICurvesView setSublayerSize:];
-[BKUICurvesView setSublayersSize:];
-[BKUICurvesView sublayerSize];
```
