# `PLSubmissionFile`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _iCloudUploadEnabled;
@"PLSubmissionConfig" _taskingConfig;
@"NSString" _directory;
@"NSString" _fileName;
```

## Properties

```
@property (T@"PLSubmissionConfig",&,V_taskingConfig) taskingConfig;
@property (T@"NSString",&,V_directory) directory;
@property (T@"NSString",&,V_fileName) fileName;
@property (TB,V_iCloudUploadEnabled) iCloudUploadEnabled;
```

## Instance methods

```
-[PLSubmissionFile fileExtension];
-[PLSubmissionFile initWithConfig:];
-[PLSubmissionFile submit];
-[PLSubmissionFile directory];
-[PLSubmissionFile filePath];
-[PLSubmissionFile fileName];
-[PLSubmissionFile fileType];
-[PLSubmissionFile setFileName:];
-[PLSubmissionFile setDirectory:];
-[PLSubmissionFile createTagFileWithPath:withInfo:];
-[PLSubmissionFile submitLogToiCloud:WithCompress:];
-[PLSubmissionFile cleanupTmpDirectory];
-[PLSubmissionFile createTagFileWithPath:];
-[PLSubmissionFile decorateFile];
-[PLSubmissionFile decorateFileAtPath:];
-[PLSubmissionFile iCloudUploadEnabled];
-[PLSubmissionFile logSubmissionResultToCAWithErrorType:withFileType:withOverrideKeys:];
-[PLSubmissionFile setFileNameWithSubmissionType:withID:];
-[PLSubmissionFile setICloudUploadEnabled:];
-[PLSubmissionFile setTaskingConfig:];
-[PLSubmissionFile submitLogToDAWithBugType:];
-[PLSubmissionFile submitLogToiCloudWithCompress:];
-[PLSubmissionFile taskingConfig];
```
