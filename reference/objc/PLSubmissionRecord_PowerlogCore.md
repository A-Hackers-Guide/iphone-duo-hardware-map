# `PLSubmissionRecord`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 22 instance methods, 3 class methods

## Instance variables

```
B _inSubmission;
@"NSString" _tagUUID;
@"NSUUID" _configUUID;
@"NSDate" _configDateApplied;
@"NSDate" _configDateReceived;
@"NSString" _filePath;
@"NSString" _ckFileDirPath;
@"NSString" _daFileDirPath;
@"NSDictionary" _tagConfig;
```

## Properties

```
@property (T@"NSString",&,V_tagUUID) tagUUID;
@property (T@"NSUUID",R,N,V_configUUID) configUUID;
@property (T@"NSDate",R,N,V_configDateApplied) configDateApplied;
@property (T@"NSDate",R,N,V_configDateReceived) configDateReceived;
@property (T@"NSString",&,V_filePath) filePath;
@property (T@"NSString",&,V_ckFileDirPath) ckFileDirPath;
@property (T@"NSString",&,V_daFileDirPath) daFileDirPath;
@property (T@"NSDictionary",&,V_tagConfig) tagConfig;
@property (TB,V_inSubmission) inSubmission;
```

## Class methods

```
+[PLSubmissionRecord supportsSecureCoding];
+[PLSubmissionRecord getCKSubmissionDirPathForTag:];
+[PLSubmissionRecord getDASubmissionDirPathForTag:];
```

## Instance methods

```
-[PLSubmissionRecord cleanup];
-[PLSubmissionRecord encodeWithCoder:];
-[PLSubmissionRecord filePath];
-[PLSubmissionRecord initWithCoder:];
-[PLSubmissionRecord setFilePath:];
-[PLSubmissionRecord removeFileAtPath:];
-[PLSubmissionRecord tagUUID];
-[PLSubmissionRecord ckFileDirPath];
-[PLSubmissionRecord configDateApplied];
-[PLSubmissionRecord configDateReceived];
-[PLSubmissionRecord configUUID];
-[PLSubmissionRecord daFileDirPath];
-[PLSubmissionRecord emitAttemptEvent];
-[PLSubmissionRecord emitSuccessEvent];
-[PLSubmissionRecord inSubmission];
-[PLSubmissionRecord initWithCKFilePath:tagUUID:tagConfig:configUUID:configDateReceived:configDateApplied:];
-[PLSubmissionRecord setCkFileDirPath:];
-[PLSubmissionRecord setDaFileDirPath:];
-[PLSubmissionRecord setInSubmission:];
-[PLSubmissionRecord setTagConfig:];
-[PLSubmissionRecord setTagUUID:];
-[PLSubmissionRecord tagConfig];
```
