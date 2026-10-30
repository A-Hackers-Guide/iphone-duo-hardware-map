# `TUCallModel`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _supportsHolding;
B _supportsGrouping;
B _supportsUngrouping;
B _supportsDTMF;
B _supportsUnambiguousMultiPartyState;
B _supportsAddCall;
B _supportsSendingToVoicemail;
```

## Properties

```
@property (TB,N,V_supportsHolding) supportsHolding;
@property (TB,N,V_supportsGrouping) supportsGrouping;
@property (TB,N,V_supportsUngrouping) supportsUngrouping;
@property (TB,N,V_supportsDTMF) supportsDTMF;
@property (TB,N,V_supportsUnambiguousMultiPartyState) supportsUnambiguousMultiPartyState;
@property (TB,N,V_supportsAddCall) supportsAddCall;
@property (TB,N,V_supportsSendingToVoicemail) supportsSendingToVoicemail;
```

## Class methods

```
+[TUCallModel supportsSecureCoding];
```

## Instance methods

```
-[TUCallModel setSupportsSendingToVoicemail:];
-[TUCallModel supportsSendingToVoicemail];
-[TUCallModel setSupportsGrouping:];
-[TUCallModel supportsGrouping];
-[TUCallModel supportsUngrouping];
-[TUCallModel encodeWithCoder:];
-[TUCallModel supportsAddCall];
-[TUCallModel hash];
-[TUCallModel supportsHolding];
-[TUCallModel description];
-[TUCallModel initWithCoder:];
-[TUCallModel setSupportsUngrouping:];
-[TUCallModel setSupportsHolding:];
-[TUCallModel supportsUnambiguousMultiPartyState];
-[TUCallModel supportsDTMF];
-[TUCallModel copyWithZone:];
-[TUCallModel isEqual:];
-[TUCallModel setSupportsUnambiguousMultiPartyState:];
-[TUCallModel setSupportsDTMF:];
-[TUCallModel setSupportsAddCall:];
```
