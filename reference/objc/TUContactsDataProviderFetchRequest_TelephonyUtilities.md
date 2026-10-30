# `TUContactsDataProviderFetchRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _useNetworkCountryCode;
B _emergency;
B _callerIDBlocked;
B _conversation;
B _verified;
B _incoming;
B _supportsDynamicSystemUI;
@"NSString" _contactIdentifier;
@"NSArray" _auxiliaryKeysToFetch;
@"NSString" _phoneNumberPrefixHint;
@"NSString" _isoCountryCode;
@"NSArray" _handles;
```

## Properties

```
@property (TB,R,N,GisEmergency,V_emergency) emergency;
@property (TB,R,N,GisCallerIDBlocked,V_callerIDBlocked) callerIDBlocked;
@property (TB,R,N,GisConversation,V_conversation) conversation;
@property (TB,R,N,GisVerified,V_verified) verified;
@property (TB,R,N,GisIncoming,V_incoming) incoming;
@property (TB,R,N,V_supportsDynamicSystemUI) supportsDynamicSystemUI;
@property (T@"NSString",R,C,N,V_isoCountryCode) isoCountryCode;
@property (T@"NSArray",C,N,V_handles) handles;
@property (T@"NSString",C,N,V_contactIdentifier) contactIdentifier;
@property (T@"NSArray",C,N,V_auxiliaryKeysToFetch) auxiliaryKeysToFetch;
@property (T@"NSString",C,N,V_phoneNumberPrefixHint) phoneNumberPrefixHint;
@property (TB,N,V_useNetworkCountryCode) useNetworkCountryCode;
```

## Instance methods

```
-[TUContactsDataProviderFetchRequest isoCountryCode];
-[TUContactsDataProviderFetchRequest isVerified];
-[TUContactsDataProviderFetchRequest contactIdentifier];
-[TUContactsDataProviderFetchRequest initWithHandle:];
-[TUContactsDataProviderFetchRequest isCallerIDBlocked];
-[TUContactsDataProviderFetchRequest isEmergency];
-[TUContactsDataProviderFetchRequest initWithHandles:];
-[TUContactsDataProviderFetchRequest init];
-[TUContactsDataProviderFetchRequest setHandles:];
-[TUContactsDataProviderFetchRequest phoneNumberPrefixHint];
-[TUContactsDataProviderFetchRequest auxiliaryKeysToFetch];
-[TUContactsDataProviderFetchRequest useNetworkCountryCode];
-[TUContactsDataProviderFetchRequest setPhoneNumberPrefixHint:];
-[TUContactsDataProviderFetchRequest supportsDynamicSystemUI];
-[TUContactsDataProviderFetchRequest isConversation];
-[TUContactsDataProviderFetchRequest isIncoming];
-[TUContactsDataProviderFetchRequest initWithHandles:isConversation:];
-[TUContactsDataProviderFetchRequest description];
-[TUContactsDataProviderFetchRequest setContactIdentifier:];
-[TUContactsDataProviderFetchRequest handles];
-[TUContactsDataProviderFetchRequest setUseNetworkCountryCode:];
-[TUContactsDataProviderFetchRequest removePsuedHandles];
-[TUContactsDataProviderFetchRequest setAuxiliaryKeysToFetch:];
-[TUContactsDataProviderFetchRequest initWithCall:];
```
