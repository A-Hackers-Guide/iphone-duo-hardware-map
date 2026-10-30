# `TUNearbySuggestion`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _identifier;
@"TUNearbyDeviceHandle" _deviceHandle;
@"TUConversationActivity" _activity;
q _type;
```

## Properties

```
@property (T@"NSUUID",R,N,V_identifier) identifier;
@property (T@"TUNearbyDeviceHandle",R,N,V_deviceHandle) deviceHandle;
@property (T@"TUConversationActivity",R,N,V_activity) activity;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[TUNearbySuggestion supportsSecureCoding];
```

## Instance methods

```
-[TUNearbySuggestion identifier];
-[TUNearbySuggestion activity];
-[TUNearbySuggestion type];
-[TUNearbySuggestion encodeWithCoder:];
-[TUNearbySuggestion hash];
-[TUNearbySuggestion description];
-[TUNearbySuggestion initWithCoder:];
-[TUNearbySuggestion isEqual:];
-[TUNearbySuggestion isEqualToSuggestion:];
-[TUNearbySuggestion deviceHandle];
-[TUNearbySuggestion initWithIdentifier:deviceHandle:activity:type:];
-[TUNearbySuggestion isEquivalentToSuggestion:];
```
