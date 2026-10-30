# `WFDiagnosticsResultItem` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",&,N) results;
@property (T@"NSString",C,N) title;
@property (T@"NSString",C,N) suggestion;
@property (TB,N) didPassTest;
@property (T@"NSArray",&,N) failedTests;
```

## Instance methods

```
-[WFDiagnosticsResultItem suggestion];
-[WFDiagnosticsResultItem setSuggestion:];
-[WFDiagnosticsResultItem title];
-[WFDiagnosticsResultItem setTitle:];
-[WFDiagnosticsResultItem results];
-[WFDiagnosticsResultItem setResults:];
-[WFDiagnosticsResultItem failedTests];
-[WFDiagnosticsResultItem setDidPassTest:];
-[WFDiagnosticsResultItem setFailedTests:];
-[WFDiagnosticsResultItem didPassTest];
```
