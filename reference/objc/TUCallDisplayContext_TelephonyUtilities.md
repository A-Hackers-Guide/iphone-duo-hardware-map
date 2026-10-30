# `TUCallDisplayContext`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 18 instance variables, 20 properties, 50 instance methods, 1 class methods

## Instance variables

```
i _legacyAddressBookIdentifier;
@"NSString" _name;
@"NSPersonNameComponents" _personNameComponents;
@"NSString" _suggestedName;
@"NSString" _suggestedNameOriginBundleID;
@"NSString" _label;
@"NSString" _companyName;
@"NSString" _companyDepartment;
@"NSURL" _companyLogoURL;
@"NSString" _mapName;
@"NSString" _location;
@"NSString" _contactName;
@"NSString" _contactLabel;
@"NSString" _callDirectoryLabel;
@"NSString" _callDirectoryLocalizedExtensionContainingAppName;
@"NSString" _callDirectoryExtensionIdentifier;
q _callDirectoryIdentityType;
@"NSArray" _contactIdentifiers;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSPersonNameComponents",C,N,V_personNameComponents) personNameComponents;
@property (T@"NSString",C,N,V_suggestedName) suggestedName;
@property (T@"NSString",C,N,V_suggestedNameOriginBundleID) suggestedNameOriginBundleID;
@property (T@"NSString",C,N,V_label) label;
@property (T@"NSString",C,N,V_companyName) companyName;
@property (T@"NSString",C,N,V_companyDepartment) companyDepartment;
@property (T@"NSURL",C,N,V_companyLogoURL) companyLogoURL;
@property (T@"NSString",C,N,V_mapName) mapName;
@property (T@"NSString",C,N,V_location) location;
@property (T@"NSString",C,N,V_contactName) contactName;
@property (T@"NSString",C,N,V_contactLabel) contactLabel;
@property (T@"NSString",C,N,V_callDirectoryLabel) callDirectoryLabel;
@property (T@"NSString",C,N,V_callDirectoryLocalizedExtensionContainingAppName) callDirectoryLocalizedExtensionContainingAppName;
@property (T@"NSString",C,N,V_callDirectoryExtensionIdentifier) callDirectoryExtensionIdentifier;
@property (Tq,N,V_callDirectoryIdentityType) callDirectoryIdentityType;
@property (T@"NSString",C,N) contactIdentifier;
@property (T@"NSArray",C,N,V_contactIdentifiers) contactIdentifiers;
@property (Ti,N,V_legacyAddressBookIdentifier) legacyAddressBookIdentifier;
@property (T@"NSString",R,C,N) firstName;
```

## Class methods

```
+[TUCallDisplayContext supportsSecureCoding];
```

## Instance methods

```
-[TUCallDisplayContext callDirectoryIdentityType];
-[TUCallDisplayContext contactIdentifier];
-[TUCallDisplayContext setSuggestedNameOriginBundleID:];
-[TUCallDisplayContext setCompanyName:];
-[TUCallDisplayContext mutableCopyWithZone:];
-[TUCallDisplayContext personNameComponents];
-[TUCallDisplayContext setCallDirectoryIdentityType:];
-[TUCallDisplayContext suggestedNameOriginBundleID];
-[TUCallDisplayContext init];
-[TUCallDisplayContext label];
-[TUCallDisplayContext companyLogoURL];
-[TUCallDisplayContext setLabel:];
-[TUCallDisplayContext location];
-[TUCallDisplayContext setCallDirectoryLocalizedExtensionContainingAppName:];
-[TUCallDisplayContext setPersonNameComponents:];
-[TUCallDisplayContext mapName];
-[TUCallDisplayContext setCallDirectoryExtensionIdentifier:];
-[TUCallDisplayContext contactLabel];
-[TUCallDisplayContext setContactName:];
-[TUCallDisplayContext setContactLabel:];
-[TUCallDisplayContext setCompanyLogoURL:];
-[TUCallDisplayContext callDirectoryExtensionIdentifier];
-[TUCallDisplayContext companyDepartment];
-[TUCallDisplayContext setFirstName:];
-[TUCallDisplayContext setCompanyDepartment:];
-[TUCallDisplayContext setCallDirectoryLabel:];
-[TUCallDisplayContext setLegacyAddressBookIdentifier:];
-[TUCallDisplayContext setMapName:];
-[TUCallDisplayContext updatePredictedNameFromReceptionist:];
-[TUCallDisplayContext setSuggestedName:];
-[TUCallDisplayContext callDirectoryLabel];
-[TUCallDisplayContext contactName];
-[TUCallDisplayContext suggestedName];
-[TUCallDisplayContext setContactIdentifiers:];
-[TUCallDisplayContext legacyAddressBookIdentifier];
-[TUCallDisplayContext companyName];
-[TUCallDisplayContext callDirectoryLocalizedExtensionContainingAppName];
-[TUCallDisplayContext setLocation:];
-[TUCallDisplayContext encodeWithCoder:];
-[TUCallDisplayContext displayContextByMergingWithDisplayContext:];
-[TUCallDisplayContext hash];
-[TUCallDisplayContext description];
-[TUCallDisplayContext setContactIdentifier:];
-[TUCallDisplayContext setName:];
-[TUCallDisplayContext contactIdentifiers];
-[TUCallDisplayContext initWithCoder:];
-[TUCallDisplayContext copyWithZone:];
-[TUCallDisplayContext isEqual:];
-[TUCallDisplayContext firstName];
-[TUCallDisplayContext name];
```
