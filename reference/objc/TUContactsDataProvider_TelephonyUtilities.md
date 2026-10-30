# `TUContactsDataProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 36 instance methods, 5 class methods

## Instance variables

```
B _useGivenName;
B _useFamilyNameFirst;
@? _localeSupportsPrefixHintForFetchRequest;
@"<TUContactsDataSource>" _contactsDataSource;
@"TUContactsDataProviderAppleCareHandles" _appleCareHandles;
@"NSDate" _deviceSetupDate;
@"NSUserDefaults" _userDefaults;
```

## Properties

```
@property (TB,N,GshouldUseFamilyNameFirst,V_useFamilyNameFirst) useFamilyNameFirst;
@property (T@?,C,N,V_localeSupportsPrefixHintForFetchRequest) localeSupportsPrefixHintForFetchRequest;
@property (T@"<TUContactsDataSource>",R,N,V_contactsDataSource) contactsDataSource;
@property (T@"TUContactsDataProviderAppleCareHandles",C,N,V_appleCareHandles) appleCareHandles;
@property (T@"NSDate",C,N,V_deviceSetupDate) deviceSetupDate;
@property (T@"NSUserDefaults",&,N,V_userDefaults) userDefaults;
@property (TB,N,GshouldUseGivenName,V_useGivenName) useGivenName;
```

## Class methods

```
+[TUContactsDataProvider numberFormatter];
+[TUContactsDataProvider unsupportedLocalesForPrefixHint];
+[TUContactsDataProvider defaultContactKeyDescriptors];
+[TUContactsDataProvider familyNameFirstLocaleCountryCodes];
+[TUContactsDataProvider keysByCombiningDefaultKeysWithKeysToFetch:];
```

## Instance methods

```
-[TUContactsDataProvider appleCareHandles];
-[TUContactsDataProvider userDefaults];
-[TUContactsDataProvider personIDForContact:];
-[TUContactsDataProvider shouldUseFamilyNameFirst];
-[TUContactsDataProvider setAppleCareHandles:];
-[TUContactsDataProvider localizedCompositeNameForContact:secondContact:];
-[TUContactsDataProvider init];
-[TUContactsDataProvider setDeviceSetupDate:];
-[TUContactsDataProvider setUseGivenName:];
-[TUContactsDataProvider contactsDataSource];
-[TUContactsDataProvider executeBatchFetchRequests:];
-[TUContactsDataProvider setUseFamilyNameFirst:];
-[TUContactsDataProvider contactWithIdentifier:keysToFetch:];
-[TUContactsDataProvider setUserDefaults:];
-[TUContactsDataProvider setLocaleSupportsPrefixHintForFetchRequest:];
-[TUContactsDataProvider nameForContact:];
-[TUContactsDataProvider labeledHandlesForContacts:];
-[TUContactsDataProvider shouldUseGivenName];
-[TUContactsDataProvider isHandleEligibleForScreenSharingRequests:];
-[TUContactsDataProvider prefixHintForFetchRequest:];
-[TUContactsDataProvider compositeNameForFetchRequest:];
-[TUContactsDataProvider localeSupportsPrefixHintForFetchRequest];
-[TUContactsDataProvider initWithContactsDataSource:];
-[TUContactsDataProvider formattedNameForHandle:countryCode:];
-[TUContactsDataProvider compositeNameForContacts:];
-[TUContactsDataProvider deviceSetupDate];
-[TUContactsDataProvider executeFetchRequest:];
-[TUContactsDataProvider ISOCountryCodeForHandle:fetchRequest:];
-[TUContactsDataProvider unifiedContactsForFetchRequest:];
-[TUContactsDataProvider shouldIgnoreHandle:withFetchRequest:];
-[TUContactsDataProvider getDeviceSetupDate];
-[TUContactsDataProvider resultForSingleHandleFetchRequest:fetchedContacts:];
-[TUContactsDataProvider contactLabelForContacts:matchingHandle:countryCode:];
-[TUContactsDataProvider processBatchFetchRequests:];
-[TUContactsDataProvider labeledHandlesForContactWithIdentifier:];
-[TUContactsDataProvider contactsForHandle:countryCode:keysToFetch:prefixHint:];
```
