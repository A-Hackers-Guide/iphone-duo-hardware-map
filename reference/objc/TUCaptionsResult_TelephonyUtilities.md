# `TUCaptionsResult`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _utteranceComplete;
I _utteranceNumber;
I _updateNumber;
@"NSArray" _tokens;
@"NSString" _text;
d _utteranceStartTimestamp;
d _utteranceDuration;
```

## Properties

```
@property (TB,R,N,V_utteranceComplete) utteranceComplete;
@property (T@"NSArray",R,N,V_tokens) tokens;
@property (T@"NSString",R,N,V_text) text;
@property (TI,R,N,V_utteranceNumber) utteranceNumber;
@property (TI,R,N,V_updateNumber) updateNumber;
@property (Td,R,N,V_utteranceStartTimestamp) utteranceStartTimestamp;
@property (Td,R,N,V_utteranceDuration) utteranceDuration;
```

## Class methods

```
+[TUCaptionsResult supportsSecureCoding];
```

## Instance methods

```
-[TUCaptionsResult text];
-[TUCaptionsResult tokens];
-[TUCaptionsResult encodeWithCoder:];
-[TUCaptionsResult hash];
-[TUCaptionsResult description];
-[TUCaptionsResult initWithCoder:];
-[TUCaptionsResult copyWithZone:];
-[TUCaptionsResult isEqual:];
-[TUCaptionsResult utteranceNumber];
-[TUCaptionsResult initWithAVCCaptionsResult:];
-[TUCaptionsResult initWithText:utteranceComplete:tokens:utteranceNumber:updateNumber:utteranceStartTimestamp:utteranceDuration:];
-[TUCaptionsResult isEqualToCaptionsResult:];
-[TUCaptionsResult updateNumber];
-[TUCaptionsResult utteranceComplete];
-[TUCaptionsResult utteranceDuration];
-[TUCaptionsResult utteranceStartTimestamp];
```
