# `FBSProcessTerminationRequest`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 6 instance variables, 10 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<FBSProcess>" _process;
@"NSString" _label;
Q _options;
q _reportType;
q _exceptionCode;
@"NSString" _explanation;
```

## Properties

```
@property (T@"NSString",C,N,V_label) label;
@property (T@"<FBSProcess>",W,N,V_process) process;
@property (TQ,N,V_options) options;
@property (Tq,N,V_reportType) reportType;
@property (Tq,N,V_exceptionCode) exceptionCode;
@property (T@"NSString",C,N,V_explanation) explanation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSProcessTerminationRequest requestForProcess:withLabel:];
```

## Instance methods

```
-[FBSProcessTerminationRequest reportType];
-[FBSProcessTerminationRequest setProcess:];
-[FBSProcessTerminationRequest setExceptionCode:];
-[FBSProcessTerminationRequest setOptions:];
-[FBSProcessTerminationRequest setExplanation:];
-[FBSProcessTerminationRequest succinctDescriptionBuilder];
-[FBSProcessTerminationRequest label];
-[FBSProcessTerminationRequest explanation];
-[FBSProcessTerminationRequest setLabel:];
-[FBSProcessTerminationRequest process];
-[FBSProcessTerminationRequest exceptionCode];
-[FBSProcessTerminationRequest descriptionWithMultilinePrefix:];
-[FBSProcessTerminationRequest setReportType:];
-[FBSProcessTerminationRequest execute];
-[FBSProcessTerminationRequest succinctDescription];
-[FBSProcessTerminationRequest description];
-[FBSProcessTerminationRequest options];
-[FBSProcessTerminationRequest copyWithZone:];
-[FBSProcessTerminationRequest descriptionBuilderWithMultilinePrefix:];
```
