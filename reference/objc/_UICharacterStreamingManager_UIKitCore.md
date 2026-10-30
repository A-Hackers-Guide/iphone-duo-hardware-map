# `_UICharacterStreamingManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"UITextView" _textView;
@"CADisplayLink" _streamingAnimationDisplayLink;
B _streamingAnimationActive;
d _lastAnimationUpdateTimeStamp;
B _committingFinalResults;
B _discardNextHypothesis;
@"NSString" _previousHypothesis;
@"NSString" _lastHypothesis;
@"NSString" _targetHypothesis;
@"NSMutableArray" _pendingEdits;
d _streamingCharacterInsertionRate;
d _minDurationBetweenHypotheses;
```

## Properties

```
@property (T@"NSString",C,N,V_previousHypothesis) previousHypothesis;
@property (T@"NSString",C,N,V_lastHypothesis) lastHypothesis;
@property (T@"NSString",C,N,V_targetHypothesis) targetHypothesis;
@property (T@"NSMutableArray",&,N,V_pendingEdits) pendingEdits;
@property (Td,N,V_streamingCharacterInsertionRate) streamingCharacterInsertionRate;
@property (Td,N,V_minDurationBetweenHypotheses) minDurationBetweenHypotheses;
@property (TB,N,V_discardNextHypothesis) discardNextHypothesis;
```

## Instance methods

```
-[_UICharacterStreamingManager _displayLinkFired:];
-[_UICharacterStreamingManager pendingEdits];
-[_UICharacterStreamingManager _startStreamingAnimations];
-[_UICharacterStreamingManager previousHypothesis];
-[_UICharacterStreamingManager initWithTextView:];
-[_UICharacterStreamingManager setTargetHypothesis:];
-[_UICharacterStreamingManager setLastHypothesis:];
-[_UICharacterStreamingManager targetHypothesis];
-[_UICharacterStreamingManager _stopStreamingAnimation];
-[_UICharacterStreamingManager setPendingEdits:];
-[_UICharacterStreamingManager setPreviousHypothesis:];
-[_UICharacterStreamingManager setDiscardNextHypothesis:];
-[_UICharacterStreamingManager setupToInsertResultForNewHypothesis:];
-[_UICharacterStreamingManager discardNextHypothesis];
-[_UICharacterStreamingManager lastHypothesis];
-[_UICharacterStreamingManager streamingCharacterInsertionRate];
-[_UICharacterStreamingManager commitFinalResults];
-[_UICharacterStreamingManager minDurationBetweenHypotheses];
-[_UICharacterStreamingManager setMinDurationBetweenHypotheses:];
-[_UICharacterStreamingManager setStreamingCharacterInsertionRate:];
-[_UICharacterStreamingManager setWords:];
```
