# `PPSSubmissionRecord`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _isExpedited;
@"NSDictionary" _contextDictionary;
@"NSURL" _filePath;
@"NSString" _fileType;
@"NSString" _issueCategory;
@"NSString" _issueDescription;
@"NSString" _recordType;
@"NSString" _targetContainer;
```

## Properties

```
@property (T@"NSDictionary",&,V_contextDictionary) contextDictionary;
@property (T@"NSURL",&,V_filePath) filePath;
@property (T@"NSString",&,V_fileType) fileType;
@property (T@"NSString",&,V_issueCategory) issueCategory;
@property (T@"NSString",&,V_issueDescription) issueDescription;
@property (TB,V_isExpedited) isExpedited;
@property (TB,R) isValid;
@property (T@"NSString",&,V_recordType) recordType;
@property (T@"NSString",&,V_targetContainer) targetContainer;
```

## Instance methods

```
-[PPSSubmissionRecord cleanup];
-[PPSSubmissionRecord recordType];
-[PPSSubmissionRecord setRecordType:];
-[PPSSubmissionRecord isValid];
-[PPSSubmissionRecord description];
-[PPSSubmissionRecord filePath];
-[PPSSubmissionRecord fileType];
-[PPSSubmissionRecord setFilePath:];
-[PPSSubmissionRecord setFileType:];
-[PPSSubmissionRecord contextDictionary];
-[PPSSubmissionRecord setContextDictionary:];
-[PPSSubmissionRecord targetContainer];
-[PPSSubmissionRecord setTargetContainer:];
-[PPSSubmissionRecord issueDescription];
-[PPSSubmissionRecord setIssueDescription:];
-[PPSSubmissionRecord setIsExpedited:];
-[PPSSubmissionRecord isExpedited];
-[PPSSubmissionRecord issueCategory];
-[PPSSubmissionRecord setIssueCategory:];
```
