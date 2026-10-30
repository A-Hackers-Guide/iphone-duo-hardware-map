# `_UIFeedbackBackBoardHIDPattern`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackBackBoardServicesPlayable`
- 5 instance variables, 7 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"BKSHIDHapticFeedbackRequest" _hidRequest;
q _deviceType;
Q _senderID;
@"NSNumber" _powerSourceID;
@"NSString" _patternName;
```

## Properties

```
@property (T@"NSString",R,N,V_patternName) patternName;
@property (T@"BKSHIDHapticFeedbackRequest",R,N) hidRequest;
@property (TB,R,N,GisHighPriority) highPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFeedbackBackBoardHIDPattern supportsSecureCoding];
+[_UIFeedbackBackBoardHIDPattern type];
+[_UIFeedbackBackBoardHIDPattern feedbackPatternWithName:deviceType:];
+[_UIFeedbackBackBoardHIDPattern feedbackPatternWithName:deviceType:senderID:];
```

## Instance methods

```
-[_UIFeedbackBackBoardHIDPattern isHighPriority];
-[_UIFeedbackBackBoardHIDPattern _effectivePlayableFeedbackTypes];
-[_UIFeedbackBackBoardHIDPattern initWithDictionaryRepresentation:];
-[_UIFeedbackBackBoardHIDPattern _playableProtocol];
-[_UIFeedbackBackBoardHIDPattern copyWithZone:];
-[_UIFeedbackBackBoardHIDPattern hidRequest];
-[_UIFeedbackBackBoardHIDPattern isEqual:];
-[_UIFeedbackBackBoardHIDPattern dictionaryRepresentation];
-[_UIFeedbackBackBoardHIDPattern completeFeedbackPatternWithPowerSourceID:];
-[_UIFeedbackBackBoardHIDPattern completeFeedbackPatternWithSenderID:];
-[_UIFeedbackBackBoardHIDPattern initWithName:deviceType:];
-[_UIFeedbackBackBoardHIDPattern initWithName:deviceType:powerSourceID:];
-[_UIFeedbackBackBoardHIDPattern initWithName:deviceType:senderID:];
-[_UIFeedbackBackBoardHIDPattern initWithName:deviceType:senderID:powerSourceID:];
-[_UIFeedbackBackBoardHIDPattern patternName];
```
