# `_UIKBRTFingerDetectionFingerFeedbackView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _framelocation;
d _radiusInt;
B _unknownSeen;
@"UILabel" _fingerLabel;
@"_UIKBRTFingerDetectionFingerCircleView" _fingerDot;
```

## Properties

```
@property (T@"UILabel",&,N,V_fingerLabel) fingerLabel;
@property (T@"_UIKBRTFingerDetectionFingerCircleView",&,N,V_fingerDot) fingerDot;
@property (TB,N,V_unknownSeen) unknownSeen;
```

## Instance methods

```
-[_UIKBRTFingerDetectionFingerFeedbackView setNeedsDisplay];
-[_UIKBRTFingerDetectionFingerFeedbackView layoutSubviews];
-[_UIKBRTFingerDetectionFingerFeedbackView radius];
-[_UIKBRTFingerDetectionFingerFeedbackView initWithFrame:];
-[_UIKBRTFingerDetectionFingerFeedbackView setFingerLabel:];
-[_UIKBRTFingerDetectionFingerFeedbackView setUnknownSeen:];
-[_UIKBRTFingerDetectionFingerFeedbackView centerOn:withRadius:andIdentifier:];
-[_UIKBRTFingerDetectionFingerFeedbackView fingerDot];
-[_UIKBRTFingerDetectionFingerFeedbackView fingerLabel];
-[_UIKBRTFingerDetectionFingerFeedbackView setFingerDot:];
-[_UIKBRTFingerDetectionFingerFeedbackView unknownSeen];
```
