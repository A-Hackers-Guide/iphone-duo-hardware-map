# `_UIKBRTFingerDetection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKBRTKeyboardTouchObserver`
- 6 instance variables, 6 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"UIView" _feedbackParentView;
@"_UIKBRTFingerDetectionView" _feedbackView;
@"NSMapTable" _fingerFeedbackViewMap;
@"NSMutableDictionary" _touches;
@"_UIKBRTFingerInfo" _fakeLeftIndex;
@"_UIKBRTFingerInfo" _fakeRightIndex;
```

## Properties

```
@property (T@"UIView",N,V_feedbackParentView) feedbackParentView;
@property (T@"_UIKBRTFingerDetectionView",&,N,V_feedbackView) feedbackView;
@property (T@"NSMapTable",&,N,V_fingerFeedbackViewMap) fingerFeedbackViewMap;
@property (T@"NSMutableDictionary",&,N,V_touches) touches;
@property (T@"_UIKBRTFingerInfo",&,N,V_fakeLeftIndex) fakeLeftIndex;
@property (T@"_UIKBRTFingerInfo",&,N,V_fakeRightIndex) fakeRightIndex;
```

## Instance methods

```
-[_UIKBRTFingerDetection init];
-[_UIKBRTFingerDetection touches];
-[_UIKBRTFingerDetection dealloc];
-[_UIKBRTFingerDetection reset];
-[_UIKBRTFingerDetection feedbackView];
-[_UIKBRTFingerDetection fingerIdForTouchWithIdentifier:];
-[_UIKBRTFingerDetection _linkTouchesInArray:withIndexes:opposingHandIndexes:unassignedIndexes:thumb:];
-[_UIKBRTFingerDetection _updateFingerFeedback];
-[_UIKBRTFingerDetection _updateFingerFeedback:];
-[_UIKBRTFingerDetection _updateTouchInfoForFingerID:];
-[_UIKBRTFingerDetection _updateTouchInfoFromOutsideInWithArray:indexes:newIdentityDict:fakeIndex:];
-[_UIKBRTFingerDetection addTouchLocation:withRadius:withTouchTime:withIdentifier:];
-[_UIKBRTFingerDetection fakeLeftIndex];
-[_UIKBRTFingerDetection fakeRightIndex];
-[_UIKBRTFingerDetection feedbackParentView];
-[_UIKBRTFingerDetection fingerFeedbackViewMap];
-[_UIKBRTFingerDetection fingerIdsRelatedToTouchWithIdentifier:sinceTimestamp:includeThumbs:];
-[_UIKBRTFingerDetection initWithParentView:];
-[_UIKBRTFingerDetection moveTouchWithIdentifier:toLocation:withRadius:atTouchTime:];
-[_UIKBRTFingerDetection removeTouchWithIdentifier:touchCancelled:];
-[_UIKBRTFingerDetection setFakeLeftIndex:];
-[_UIKBRTFingerDetection setFakeRightIndex:];
-[_UIKBRTFingerDetection setFeedbackParentView:];
-[_UIKBRTFingerDetection setFeedbackView:];
-[_UIKBRTFingerDetection setFingerFeedbackViewMap:];
-[_UIKBRTFingerDetection setTouches:];
-[_UIKBRTFingerDetection touchIdentifiersForFingerId:];
-[_UIKBRTFingerDetection touchLocationForFingerId:];
-[_UIKBRTFingerDetection updateWithFCenter:jCenter:keySize:rowOffsets:homeRowOffsetIndex:];
```
