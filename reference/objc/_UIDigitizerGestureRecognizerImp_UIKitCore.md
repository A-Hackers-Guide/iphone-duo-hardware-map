# `_UIDigitizerGestureRecognizerImp`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"<_UIDigitizerGestureRecognizerImpDelegate>" _delegate;
d _minimumPressDuration;
d _maximumPressDuration;
q _numberOfActiveTouches;
d _pressEndToTouchBeginDuration;
d _touchEndToPressEndDuration;
d _touchEndTime;
d _pressBeginTime;
d _pressEndTime;
d _lastRecognitionTime;
@"NSTimer" _minimumPressDurationTimer;
@"NSTimer" _waitingForTouchesAfterPressTimer;
{CGPoint="x"d"y"d} _digitizerLocation;
```

## Properties

```
@property (T@"<_UIDigitizerGestureRecognizerImpDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_minimumPressDuration) minimumPressDuration;
@property (Td,N,V_maximumPressDuration) maximumPressDuration;
@property (T{CGPoint=dd},N,V_digitizerLocation) digitizerLocation;
@property (Tq,N,V_numberOfActiveTouches) numberOfActiveTouches;
@property (Td,N,V_pressEndToTouchBeginDuration) pressEndToTouchBeginDuration;
@property (Td,N,V_touchEndToPressEndDuration) touchEndToPressEndDuration;
@property (Td,N,V_touchEndTime) touchEndTime;
@property (Td,N,V_pressBeginTime) pressBeginTime;
@property (Td,N,V_pressEndTime) pressEndTime;
@property (Td,N,V_lastRecognitionTime) lastRecognitionTime;
@property (T@"NSTimer",W,N,V_minimumPressDurationTimer) minimumPressDurationTimer;
@property (T@"NSTimer",W,N,V_waitingForTouchesAfterPressTimer) waitingForTouchesAfterPressTimer;
```

## Instance methods

```
-[_UIDigitizerGestureRecognizerImp touchesEnded:withEvent:];
-[_UIDigitizerGestureRecognizerImp touchesCancelled:withEvent:];
-[_UIDigitizerGestureRecognizerImp maximumPressDuration];
-[_UIDigitizerGestureRecognizerImp pressesCancelled:withEvent:];
-[_UIDigitizerGestureRecognizerImp pressesEnded:withEvent:];
-[_UIDigitizerGestureRecognizerImp reset];
-[_UIDigitizerGestureRecognizerImp touchesBegan:withEvent:];
-[_UIDigitizerGestureRecognizerImp touchesMoved:withEvent:];
-[_UIDigitizerGestureRecognizerImp pressesBegan:withEvent:];
-[_UIDigitizerGestureRecognizerImp pressesChanged:withEvent:];
-[_UIDigitizerGestureRecognizerImp setDelegate:];
-[_UIDigitizerGestureRecognizerImp setMaximumPressDuration:];
-[_UIDigitizerGestureRecognizerImp delegate];
-[_UIDigitizerGestureRecognizerImp minimumPressDuration];
-[_UIDigitizerGestureRecognizerImp setMinimumPressDuration:];
-[_UIDigitizerGestureRecognizerImp _minimumPressDurationTimerFired:];
-[_UIDigitizerGestureRecognizerImp _senderOfPressesHasTouchSurface:withEvent:];
-[_UIDigitizerGestureRecognizerImp _senderOfPressesIsSoftwareRemoteWithEvent:];
-[_UIDigitizerGestureRecognizerImp _shouldReportDigitizerLocation];
-[_UIDigitizerGestureRecognizerImp _waitingForTouchesAfterPressTimerFired:];
-[_UIDigitizerGestureRecognizerImp defaultDigitizerLocation];
-[_UIDigitizerGestureRecognizerImp digitizerLocation];
-[_UIDigitizerGestureRecognizerImp lastRecognitionTime];
-[_UIDigitizerGestureRecognizerImp minimumPressDurationTimer];
-[_UIDigitizerGestureRecognizerImp numberOfActiveTouches];
-[_UIDigitizerGestureRecognizerImp pressBeginTime];
-[_UIDigitizerGestureRecognizerImp pressEndTime];
-[_UIDigitizerGestureRecognizerImp pressEndToTouchBeginDuration];
-[_UIDigitizerGestureRecognizerImp setDigitizerLocation:];
-[_UIDigitizerGestureRecognizerImp setLastRecognitionTime:];
-[_UIDigitizerGestureRecognizerImp setMinimumPressDurationTimer:];
-[_UIDigitizerGestureRecognizerImp setNumberOfActiveTouches:];
-[_UIDigitizerGestureRecognizerImp setPressBeginTime:];
-[_UIDigitizerGestureRecognizerImp setPressEndTime:];
-[_UIDigitizerGestureRecognizerImp setPressEndToTouchBeginDuration:];
-[_UIDigitizerGestureRecognizerImp setTouchEndTime:];
-[_UIDigitizerGestureRecognizerImp setTouchEndToPressEndDuration:];
-[_UIDigitizerGestureRecognizerImp setWaitingForTouchesAfterPressTimer:];
-[_UIDigitizerGestureRecognizerImp touchEndTime];
-[_UIDigitizerGestureRecognizerImp touchEndToPressEndDuration];
-[_UIDigitizerGestureRecognizerImp waitingForTouchesAfterPressTimer];
```
