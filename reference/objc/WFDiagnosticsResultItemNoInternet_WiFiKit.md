# `WFDiagnosticsResultItemNoInternet`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFDiagnosticsResultItem`
- 5 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _didPassTest;
@"NSArray" _results;
@"NSString" _title;
@"NSString" _suggestion;
@"NSArray" _failedTests;
```

## Properties

```
@property (T@"NSArray",&,N,V_results) results;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_suggestion) suggestion;
@property (TB,N,V_didPassTest) didPassTest;
@property (T@"NSArray",&,N,V_failedTests) failedTests;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFDiagnosticsResultItemNoInternet suggestion];
-[WFDiagnosticsResultItemNoInternet setSuggestion:];
-[WFDiagnosticsResultItemNoInternet title];
-[WFDiagnosticsResultItemNoInternet setTitle:];
-[WFDiagnosticsResultItemNoInternet results];
-[WFDiagnosticsResultItemNoInternet setResults:];
-[WFDiagnosticsResultItemNoInternet failedTests];
-[WFDiagnosticsResultItemNoInternet initWithResults:];
-[WFDiagnosticsResultItemNoInternet setDidPassTest:];
-[WFDiagnosticsResultItemNoInternet setFailedTests:];
-[WFDiagnosticsResultItemNoInternet didPassTest];
```
