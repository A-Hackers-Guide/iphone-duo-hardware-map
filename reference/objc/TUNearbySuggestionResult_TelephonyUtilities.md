# `TUNearbySuggestionResult`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"TUNearbySuggestion" _suggestion;
@"TUConversationActivity" _selectedActivity;
q _type;
```

## Properties

```
@property (T@"TUNearbySuggestion",R,N,V_suggestion) suggestion;
@property (T@"TUConversationActivity",R,N,V_selectedActivity) selectedActivity;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[TUNearbySuggestionResult supportsSecureCoding];
```

## Instance methods

```
-[TUNearbySuggestionResult suggestion];
-[TUNearbySuggestionResult type];
-[TUNearbySuggestionResult encodeWithCoder:];
-[TUNearbySuggestionResult description];
-[TUNearbySuggestionResult initWithCoder:];
-[TUNearbySuggestionResult initWithSuggestion:selectedActivity:type:];
-[TUNearbySuggestionResult selectedActivity];
```
