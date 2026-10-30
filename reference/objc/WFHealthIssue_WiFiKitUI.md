# `WFHealthIssue`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 30 instance methods, 3 class methods

## Instance variables

```
B _overrideIssue;
B _subtitleOnlyIssue;
B _chinaDevice;
Q _type;
Q _category;
@"NSString" _issueShortTitle;
@"NSString" _issueTitle;
@"NSString" _issueDescription;
@"NSString" _issueRecommendation;
@"NSString" _typeString;
```

## Properties

```
@property (T@"NSString",C,N,V_issueShortTitle) issueShortTitle;
@property (T@"NSString",C,N,V_issueTitle) issueTitle;
@property (T@"NSString",C,N,V_issueDescription) issueDescription;
@property (T@"NSString",C,N,V_issueRecommendation) issueRecommendation;
@property (TQ,N,V_type) type;
@property (TQ,N,V_category) category;
@property (TB,N,V_chinaDevice) chinaDevice;
@property (T@"NSString",R,N) issueDetailText;
@property (T@"NSString",R,C,N,V_typeString) typeString;
@property (TB,N,V_overrideIssue) overrideIssue;
@property (TB,R,N,V_subtitleOnlyIssue) subtitleOnlyIssue;
```

## Class methods

```
+[WFHealthIssue highestPriorityIssueFromIssues:];
+[WFHealthIssue healthIssueSortComparator];
+[WFHealthIssue issueWithType:];
```

## Instance methods

```
-[WFHealthIssue _categoryForType:];
-[WFHealthIssue setCategory:];
-[WFHealthIssue category];
-[WFHealthIssue initWithType:];
-[WFHealthIssue chinaDevice];
-[WFHealthIssue setType:];
-[WFHealthIssue type];
-[WFHealthIssue hash];
-[WFHealthIssue description];
-[WFHealthIssue typeString];
-[WFHealthIssue setChinaDevice:];
-[WFHealthIssue isEqual:];
-[WFHealthIssue _descriptionForType:];
-[WFHealthIssue issueTitle];
-[WFHealthIssue setIssueTitle:];
-[WFHealthIssue issueDescription];
-[WFHealthIssue setIssueDescription:];
-[WFHealthIssue issueRecommendation];
-[WFHealthIssue setOverrideIssue:];
-[WFHealthIssue issueDetailText];
-[WFHealthIssue issueShortTitle];
-[WFHealthIssue _recommendationForType:];
-[WFHealthIssue _shortTitleForType:];
-[WFHealthIssue _titleForType:];
-[WFHealthIssue _typeStringForType:];
-[WFHealthIssue isEqualToHealthIssue:];
-[WFHealthIssue overrideIssue];
-[WFHealthIssue setIssueRecommendation:];
-[WFHealthIssue setIssueShortTitle:];
-[WFHealthIssue subtitleOnlyIssue];
```
