# `_UIDebugIssue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDebugIssueReporting`
- 3 instance variables, 7 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSString" _description;
@"NSString" _prefix;
@"_UIDebugIssueReport" _subissueReport;
```

## Properties

```
@property (T@"_UIDebugIssueReport",R,N,G_subissueReport,V_subissueReport) subissueReport;
@property (T@"NSString",C,N,V_prefix) prefix;
@property (T@"NSString",C,N,V_description) description;
@property (T@"NSArray",R,C,N) subissues;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDebugIssue issueWithDescription:];
+[_UIDebugIssue issueWithFormat:];
```

## Instance methods

```
-[_UIDebugIssue init];
-[_UIDebugIssue setPrefix:];
-[_UIDebugIssue description];
-[_UIDebugIssue prefix];
-[_UIDebugIssue _subissueReport];
-[_UIDebugIssue setDescription:];
-[_UIDebugIssue addIssue:];
-[_UIDebugIssue subissues];
```
