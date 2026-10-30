# `WFLimitedNetworkIssue`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFHealthIssue`
- 6 instance variables, 0 properties, 8 instance methods, 2 class methods

## Instance variables

```
B _subtitleOnlyIssue;
@"NSString" _issueShortTitle;
@"NSString" _typeString;
@"NSString" _issueTitle;
@"NSString" _issueRecommendation;
@"NSString" _issueDescription;
```

## Class methods

```
+[WFLimitedNetworkIssue limitedNetwork];
+[WFLimitedNetworkIssue limitedNetwork_CH];
```

## Instance methods

```
-[WFLimitedNetworkIssue typeString];
-[WFLimitedNetworkIssue issueTitle];
-[WFLimitedNetworkIssue issueDescription];
-[WFLimitedNetworkIssue issueRecommendation];
-[WFLimitedNetworkIssue issueShortTitle];
-[WFLimitedNetworkIssue _RecommendationForChinaDevice:];
-[WFLimitedNetworkIssue initWithChinaDevice:];
-[WFLimitedNetworkIssue subtitleOnlyIssue];
```
