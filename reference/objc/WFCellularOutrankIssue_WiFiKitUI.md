# `WFCellularOutrankIssue`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFHealthIssue`
- 4 instance variables, 0 properties, 7 instance methods, 4 class methods

## Instance variables

```
B _subtitleOnlyIssue;
@"NSString" _issueShortTitle;
@"NSString" _typeString;
@"NSString" _issueTitle;
```

## Class methods

```
+[WFCellularOutrankIssue cellularOutrankDownload];
+[WFCellularOutrankIssue cellularOutrankPerformance];
+[WFCellularOutrankIssue cellularOutrankPrivateNetwork];
+[WFCellularOutrankIssue cellularOutrankSecurity];
```

## Instance methods

```
-[WFCellularOutrankIssue typeString];
-[WFCellularOutrankIssue issueTitle];
-[WFCellularOutrankIssue issueShortTitle];
-[WFCellularOutrankIssue _cellularOutrankSubTypeToString:];
-[WFCellularOutrankIssue _titleForSubType:];
-[WFCellularOutrankIssue initWithSubType:];
-[WFCellularOutrankIssue subtitleOnlyIssue];
```
