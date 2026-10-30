# `_UIKBRTTouchDrifting`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKBRTKeyboardTouchObserver`
- 25 instance variables, 27 properties, 72 instance methods, 1 class methods

## Instance variables

```
B _supportsDrifting;
B _leftDriftRemovingItems;
B _rightDriftRemovingItems;
@"<_UIKBRTTouchDriftingDelegate>" _delegate;
@"NSArray" _indexSearchOrder;
@"NSMutableDictionary" _touches;
@"_UIKBRTTouchHistory" _fHistory;
@"_UIKBRTTouchHistory" _jHistory;
@"_UIKBRTTouchHistory" _otherHistory;
@"_UIKBRTDecayingObject" _enableLatchObj;
@"_UIKBRTDecayingOffset" _leftHandDriftOffsetObj;
@"_UIKBRTDecayingOffset" _leftHandFixedOffsetObj;
@"_UIKBRTDecayingOffset" _rightHandDriftOffsetObj;
@"_UIKBRTDecayingOffset" _rightHandFixedOffsetObj;
@"_UIKBRTTouchHistoryInfo" _leftIndexFingerInfo;
@"NSMutableSet" _leftDriftLockTouchIDs;
@"_UIKBRTTouchHistoryInfo" _rightIndexFingerInfo;
@"NSMutableSet" _rightDriftLockTouchIDs;
@"UIView" _feedbackParentView;
@"NSTimer" _feedbackTimer;
@"UIView" _leftDriftFeedbackView;
@"UIView" _rightDriftFeedbackView;
@"UIView" _touchHistoryFeedbackView;
@"NSMapTable" _touchHistoryViewMap;
{?="up"d"down"d"left"d"right"d} _touchError;
```

## Properties

```
@property (T@"NSArray",&,N,V_indexSearchOrder) indexSearchOrder;
@property (T@"NSMutableDictionary",&,N,V_touches) touches;
@property (T@"_UIKBRTTouchHistory",&,N,V_fHistory) fHistory;
@property (T@"_UIKBRTTouchHistory",&,N,V_jHistory) jHistory;
@property (T@"_UIKBRTTouchHistory",&,N,V_otherHistory) otherHistory;
@property (T{?=dddd},N,V_touchError) touchError;
@property (TB,N,V_supportsDrifting) supportsDrifting;
@property (T@"_UIKBRTDecayingObject",&,N,V_enableLatchObj) enableLatchObj;
@property (T@"_UIKBRTDecayingOffset",&,N,V_leftHandDriftOffsetObj) leftHandDriftOffsetObj;
@property (T@"_UIKBRTDecayingOffset",&,N,V_leftHandFixedOffsetObj) leftHandFixedOffsetObj;
@property (T@"_UIKBRTDecayingOffset",&,N,V_rightHandDriftOffsetObj) rightHandDriftOffsetObj;
@property (T@"_UIKBRTDecayingOffset",&,N,V_rightHandFixedOffsetObj) rightHandFixedOffsetObj;
@property (T@"_UIKBRTTouchHistoryInfo",&,N,V_leftIndexFingerInfo) leftIndexFingerInfo;
@property (T@"NSMutableSet",&,N,V_leftDriftLockTouchIDs) leftDriftLockTouchIDs;
@property (TB,N,V_leftDriftRemovingItems) leftDriftRemovingItems;
@property (T@"_UIKBRTTouchHistoryInfo",&,N,V_rightIndexFingerInfo) rightIndexFingerInfo;
@property (T@"NSMutableSet",&,N,V_rightDriftLockTouchIDs) rightDriftLockTouchIDs;
@property (TB,N,V_rightDriftRemovingItems) rightDriftRemovingItems;
@property (T@"UIView",W,N,V_feedbackParentView) feedbackParentView;
@property (T@"NSTimer",&,N,V_feedbackTimer) feedbackTimer;
@property (T@"UIView",&,N,V_leftDriftFeedbackView) leftDriftFeedbackView;
@property (T@"UIView",&,N,V_rightDriftFeedbackView) rightDriftFeedbackView;
@property (T@"UIView",&,N,V_touchHistoryFeedbackView) touchHistoryFeedbackView;
@property (T@"NSMapTable",&,N,V_touchHistoryViewMap) touchHistoryViewMap;
@property (T@"<_UIKBRTTouchDriftingDelegate>",N,V_delegate) delegate;
@property (T{CGPoint=dd},R,N) leftHandDriftOffset;
@property (T{CGPoint=dd},R,N) rightHandDriftOffset;
```

## Class methods

```
+[_UIKBRTTouchDrifting isEnabled];
```

## Instance methods

```
-[_UIKBRTTouchDrifting init];
-[_UIKBRTTouchDrifting touches];
-[_UIKBRTTouchDrifting dealloc];
-[_UIKBRTTouchDrifting reset];
-[_UIKBRTTouchDrifting setDelegate:];
-[_UIKBRTTouchDrifting delegate];
-[_UIKBRTTouchDrifting _offsetForPoint:fromPoint:];
-[_UIKBRTTouchDrifting _pinOffset:];
-[_UIKBRTTouchDrifting _pointFromPoint:plusOffset:];
-[_UIKBRTTouchDrifting _resetFeedback];
-[_UIKBRTTouchDrifting _touchDictWithFingerIds:];
-[_UIKBRTTouchDrifting _updateDriftForFingers:leftHand:newestTouch:];
-[_UIKBRTTouchDrifting _updateDriftView];
-[_UIKBRTTouchDrifting _updateDriftViewTimer:];
-[_UIKBRTTouchDrifting _updateDriftWithTouchInfo:];
-[_UIKBRTTouchDrifting _updateHistory];
-[_UIKBRTTouchDrifting addTouchLocation:withRadius:withTouchTime:withIdentifier:];
-[_UIKBRTTouchDrifting enableLatchObj];
-[_UIKBRTTouchDrifting fHistory];
-[_UIKBRTTouchDrifting feedbackParentView];
-[_UIKBRTTouchDrifting feedbackTimer];
-[_UIKBRTTouchDrifting ignoreTouchWithIdentifier:withTouchTime:];
-[_UIKBRTTouchDrifting indexSearchOrder];
-[_UIKBRTTouchDrifting initWithParentView:];
-[_UIKBRTTouchDrifting jHistory];
-[_UIKBRTTouchDrifting leftDriftFeedbackView];
-[_UIKBRTTouchDrifting leftDriftLockTouchIDs];
-[_UIKBRTTouchDrifting leftDriftRemovingItems];
-[_UIKBRTTouchDrifting leftHandDriftOffset];
-[_UIKBRTTouchDrifting leftHandDriftOffsetObj];
-[_UIKBRTTouchDrifting leftHandFixedOffsetObj];
-[_UIKBRTTouchDrifting leftIndexFingerInfo];
-[_UIKBRTTouchDrifting moveTouchWithIdentifier:toLocation:withRadius:atTouchTime:];
-[_UIKBRTTouchDrifting otherHistory];
-[_UIKBRTTouchDrifting removeTouchWithIdentifier:touchCancelled:];
-[_UIKBRTTouchDrifting rightDriftFeedbackView];
-[_UIKBRTTouchDrifting rightDriftLockTouchIDs];
-[_UIKBRTTouchDrifting rightDriftRemovingItems];
-[_UIKBRTTouchDrifting rightHandDriftOffset];
-[_UIKBRTTouchDrifting rightHandDriftOffsetObj];
-[_UIKBRTTouchDrifting rightHandFixedOffsetObj];
-[_UIKBRTTouchDrifting rightIndexFingerInfo];
-[_UIKBRTTouchDrifting setEnableLatchObj:];
-[_UIKBRTTouchDrifting setFHistory:];
-[_UIKBRTTouchDrifting setFeedbackParentView:];
-[_UIKBRTTouchDrifting setFeedbackTimer:];
-[_UIKBRTTouchDrifting setIndexSearchOrder:];
-[_UIKBRTTouchDrifting setJHistory:];
-[_UIKBRTTouchDrifting setLeftDriftFeedbackView:];
-[_UIKBRTTouchDrifting setLeftDriftLockTouchIDs:];
-[_UIKBRTTouchDrifting setLeftDriftRemovingItems:];
-[_UIKBRTTouchDrifting setLeftHandDriftOffsetObj:];
-[_UIKBRTTouchDrifting setLeftHandFixedOffsetObj:];
-[_UIKBRTTouchDrifting setLeftIndexFingerInfo:];
-[_UIKBRTTouchDrifting setOtherHistory:];
-[_UIKBRTTouchDrifting setRightDriftFeedbackView:];
-[_UIKBRTTouchDrifting setRightDriftLockTouchIDs:];
-[_UIKBRTTouchDrifting setRightDriftRemovingItems:];
-[_UIKBRTTouchDrifting setRightHandDriftOffsetObj:];
-[_UIKBRTTouchDrifting setRightHandFixedOffsetObj:];
-[_UIKBRTTouchDrifting setRightIndexFingerInfo:];
-[_UIKBRTTouchDrifting setSupportsDrifting:];
-[_UIKBRTTouchDrifting setTouchError:];
-[_UIKBRTTouchDrifting setTouchHistoryFeedbackView:];
-[_UIKBRTTouchDrifting setTouchHistoryViewMap:];
-[_UIKBRTTouchDrifting setTouches:];
-[_UIKBRTTouchDrifting supportsDrifting];
-[_UIKBRTTouchDrifting touchError];
-[_UIKBRTTouchDrifting touchHistoryFeedbackView];
-[_UIKBRTTouchDrifting touchHistoryViewMap];
-[_UIKBRTTouchDrifting updateTouchWithIdentifier:withTouchTime:resultingError:rowOffsetFromHomeRow:];
-[_UIKBRTTouchDrifting updateWithFCenter:jCenter:keySize:rowOffsets:homeRowOffsetIndex:];
```
