# `WFPrivacyIssue`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFHealthIssue`
- 5 instance variables, 0 properties, 11 instance methods, 6 class methods

## Instance variables

```
@"NSString" _issueShortTitle;
@"NSString" _issueTitle;
@"NSString" _issueDescription;
@"NSString" _issueRecommendation;
@"NSString" _typeString;
```

## Class methods

```
+[WFPrivacyIssue carrierNetworkIssue];
+[WFPrivacyIssue dnsFilteredNetworkIssue];
+[WFPrivacyIssue privateAddressDisabledByCarrierIssueWithCarrierName:];
+[WFPrivacyIssue privateAddressDisabledByProfileIssueWithOrganizationName:profileName:profileUUID:];
+[WFPrivacyIssue privateAddressDisabledBySystemIssue];
+[WFPrivacyIssue privateAddressDisabledByUserIssue];
```

## Instance methods

```
-[WFPrivacyIssue typeString];
-[WFPrivacyIssue issueTitle];
-[WFPrivacyIssue issueDescription];
-[WFPrivacyIssue issueRecommendation];
-[WFPrivacyIssue issueShortTitle];
-[WFPrivacyIssue _descriptionForSubType:organizationName:profileName:];
-[WFPrivacyIssue _healthIssueTypeForSubType:];
-[WFPrivacyIssue _privateAddressTypeToString:];
-[WFPrivacyIssue _recommendationForSubType:organizationName:];
-[WFPrivacyIssue _titleForSubType:];
-[WFPrivacyIssue initWithPrivacyType:organizationName:profileName:profileUUID:];
```
