# `TUNearbySuggestionAdvertisement`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _suggestionIdentifier;
@"NSString" _deviceIdentifier;
q _type;
```

## Properties

```
@property (T@"NSUUID",R,N,V_suggestionIdentifier) suggestionIdentifier;
@property (T@"NSString",R,N,V_deviceIdentifier) deviceIdentifier;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[TUNearbySuggestionAdvertisement supportsSecureCoding];
```

## Instance methods

```
-[TUNearbySuggestionAdvertisement suggestionIdentifier];
-[TUNearbySuggestionAdvertisement deviceIdentifier];
-[TUNearbySuggestionAdvertisement type];
-[TUNearbySuggestionAdvertisement encodeWithCoder:];
-[TUNearbySuggestionAdvertisement hash];
-[TUNearbySuggestionAdvertisement description];
-[TUNearbySuggestionAdvertisement initWithCoder:];
-[TUNearbySuggestionAdvertisement isEqual:];
-[TUNearbySuggestionAdvertisement initWithSuggestion:];
-[TUNearbySuggestionAdvertisement initWithSuggestionIdentifier:deviceIdentifier:type:];
-[TUNearbySuggestionAdvertisement isEqualToSuggestionAdvertisement:];
```
