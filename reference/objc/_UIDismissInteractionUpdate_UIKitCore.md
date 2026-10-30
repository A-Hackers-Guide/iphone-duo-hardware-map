# `_UIDismissInteractionUpdate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSSecureCoding`
- 9 instance variables, 13 properties, 23 instance methods, 2 class methods

## Instance variables

```
B _isTracking;
B _wantsHeightClamping;
d _scale;
d _progressToMinScale;
d _dampingRatio;
d _response;
{CGPoint="x"d"y"d} _originalTrackingViewPosition;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _translation;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
```

## Properties

```
@property (T{CGPoint=dd},N,V_originalTrackingViewPosition) originalTrackingViewPosition;
@property (T{CGAffineTransform=dddddd},N,V_translation) translation;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (Td,N,V_scale) scale;
@property (Td,N,V_progressToMinScale) progressToMinScale;
@property (Td,N,V_dampingRatio) dampingRatio;
@property (Td,N,V_response) response;
@property (TB,N,V_isTracking) isTracking;
@property (TB,N,V_wantsHeightClamping) wantsHeightClamping;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDismissInteractionUpdate supportsBSXPCSecureCoding];
+[_UIDismissInteractionUpdate supportsSecureCoding];
```

## Instance methods

```
-[_UIDismissInteractionUpdate setResponse:];
-[_UIDismissInteractionUpdate setDampingRatio:];
-[_UIDismissInteractionUpdate dampingRatio];
-[_UIDismissInteractionUpdate setScale:];
-[_UIDismissInteractionUpdate setTransform:];
-[_UIDismissInteractionUpdate transform];
-[_UIDismissInteractionUpdate isTracking];
-[_UIDismissInteractionUpdate scale];
-[_UIDismissInteractionUpdate encodeWithCoder:];
-[_UIDismissInteractionUpdate setTranslation:];
-[_UIDismissInteractionUpdate initWithCoder:];
-[_UIDismissInteractionUpdate encodeWithBSXPCCoder:];
-[_UIDismissInteractionUpdate initWithBSXPCCoder:];
-[_UIDismissInteractionUpdate isEqual:];
-[_UIDismissInteractionUpdate translation];
-[_UIDismissInteractionUpdate response];
-[_UIDismissInteractionUpdate originalTrackingViewPosition];
-[_UIDismissInteractionUpdate progressToMinScale];
-[_UIDismissInteractionUpdate setIsTracking:];
-[_UIDismissInteractionUpdate setOriginalTrackingViewPosition:];
-[_UIDismissInteractionUpdate setProgressToMinScale:];
-[_UIDismissInteractionUpdate setWantsHeightClamping:];
-[_UIDismissInteractionUpdate wantsHeightClamping];
```
