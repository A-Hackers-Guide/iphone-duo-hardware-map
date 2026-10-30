# `TUCaption`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 21 instance methods, 5 class methods

## Instance variables

```
d _confidence;
@"NSString" _text;
@"NSNumber" _utteranceStartTimestamp;
@"NSNumber" _utteranceDuration;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (Td,N,V_confidence) confidence;
@property (T@"NSString",C,N,V_text) text;
@property (T{_NSRange=QQ},R,N,V_range) range;
@property (T@"NSNumber",R,N,V_utteranceStartTimestamp) utteranceStartTimestamp;
@property (T@"NSNumber",R,N,V_utteranceDuration) utteranceDuration;
```

## Class methods

```
+[TUCaption supportsSecureCoding];
+[TUCaption unarchivedObjectClasses];
+[TUCaption unarchivedObjectFromData:error:];
+[TUCaption averageConfidenceOverCaptions:];
+[TUCaption combinedStringFromCaptions:];
```

## Instance methods

```
-[TUCaption range];
-[TUCaption text];
-[TUCaption archivedDataWithError:];
-[TUCaption setConfidence:];
-[TUCaption encodeWithCoder:];
-[TUCaption hash];
-[TUCaption description];
-[TUCaption initWithCoder:];
-[TUCaption setText:];
-[TUCaption copyWithZone:];
-[TUCaption isEqual:];
-[TUCaption confidence];
-[TUCaption initWithCaption:];
-[TUCaption initWithCaptionsToken:];
-[TUCaption initWithCaptionsToken:utteranceStartTimestamp:utteranceDuration:];
-[TUCaption initWithConfidence:text:];
-[TUCaption initWithConfidence:text:utteranceStartTimestamp:utteranceDuration:];
-[TUCaption initWithText:confidence:range:];
-[TUCaption isEqualToCaption:];
-[TUCaption utteranceDuration];
-[TUCaption utteranceStartTimestamp];
```
