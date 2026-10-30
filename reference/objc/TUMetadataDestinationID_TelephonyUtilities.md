# `TUMetadataDestinationID`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 2 properties, 11 instance methods, 4 class methods

## Instance variables

```
@"TUHandle" _handle;
```

## Properties

```
@property (T@"TUHandle",R,N,V_handle) handle;
@property (T@"NSString",R,C,N) isoCountryCode;
```

## Class methods

```
+[TUMetadataDestinationID supportsSecureCoding];
+[TUMetadataDestinationID metadataDestinationIDForCall:];
+[TUMetadataDestinationID metadataDestinationIDsForCHRecentCall:];
+[TUMetadataDestinationID metadataDestinationIDsForCHRecentCalls:];
```

## Instance methods

```
-[TUMetadataDestinationID isoCountryCode];
-[TUMetadataDestinationID initWithHandle:];
-[TUMetadataDestinationID handle];
-[TUMetadataDestinationID encodeWithCoder:];
-[TUMetadataDestinationID hash];
-[TUMetadataDestinationID description];
-[TUMetadataDestinationID initWithCoder:];
-[TUMetadataDestinationID copyWithZone:];
-[TUMetadataDestinationID isEqual:];
-[TUMetadataDestinationID isEqualToMetadataDestinationID:];
-[TUMetadataDestinationID initWithDestinationID:isoCountryCode:];
```
