# `BWAutoSuggestTracker`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 12 properties, 26 instance methods, 0 class methods

## Instance variables

```
i _objectType;
q _combinedTrackerID;
i _validObjectCounter;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
@"NSMutableArray" _centersIn;
@"NSMutableArray" _ObjectAreaIn;
@"NSMutableArray" _centerVx;
@"NSMutableArray" _centerVy;
@"NSMutableArray" _centerDx;
@"NSMutableArray" _centerDy;
i _trackerID;
I _confidenceLevel;
@"NSMutableArray" _objectAreaIn;
```

## Properties

```
@property (Ti,N,V_objectType) objectType;
@property (Ti,N,V_trackerID) trackerID;
@property (Tq,N,V_combinedTrackerID) combinedTrackerID;
@property (TI,N,V_confidenceLevel) confidenceLevel;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
@property (Ti,N,V_validObjectCounter) validObjectCounter;
@property (T@"NSMutableArray",&,N,V_centersIn) centersIn;
@property (T@"NSMutableArray",&,N,V_objectAreaIn) objectAreaIn;
@property (T@"NSMutableArray",&,N,V_centerVx) centerVx;
@property (T@"NSMutableArray",&,N,V_centerVy) centerVy;
@property (T@"NSMutableArray",&,N,V_centerDx) centerDx;
@property (T@"NSMutableArray",&,N,V_centerDy) centerDy;
```

## Instance methods

```
-[BWAutoSuggestTracker objectType];
-[BWAutoSuggestTracker init];
-[BWAutoSuggestTracker dealloc];
-[BWAutoSuggestTracker setConfidenceLevel:];
-[BWAutoSuggestTracker confidenceLevel];
-[BWAutoSuggestTracker rect];
-[BWAutoSuggestTracker setRect:];
-[BWAutoSuggestTracker setObjectType:];
-[BWAutoSuggestTracker centerDx];
-[BWAutoSuggestTracker centerDy];
-[BWAutoSuggestTracker centerVx];
-[BWAutoSuggestTracker centerVy];
-[BWAutoSuggestTracker centersIn];
-[BWAutoSuggestTracker combinedTrackerID];
-[BWAutoSuggestTracker objectAreaIn];
-[BWAutoSuggestTracker setCenterDx:];
-[BWAutoSuggestTracker setCenterDy:];
-[BWAutoSuggestTracker setCenterVx:];
-[BWAutoSuggestTracker setCenterVy:];
-[BWAutoSuggestTracker setCentersIn:];
-[BWAutoSuggestTracker setCombinedTrackerID:];
-[BWAutoSuggestTracker setObjectAreaIn:];
-[BWAutoSuggestTracker setTrackerID:];
-[BWAutoSuggestTracker setValidObjectCounter:];
-[BWAutoSuggestTracker trackerID];
-[BWAutoSuggestTracker validObjectCounter];
```
