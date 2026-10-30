# `NWURLSessionDownloadResumeInfo`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWURLSessionResumeInfo`
- 3 instance variables, 3 properties, 9 instance methods, 3 class methods

## Instance variables

```
B __keepDownloadTaskFile;
@"NSURL" _fileURL;
@"NSString" _tempFileName;
```

## Properties

```
@property (T@"NSURL",&,N,V_fileURL) fileURL;
@property (T@"NSString",&,N,V_tempFileName) tempFileName;
@property (TB,N,V__keepDownloadTaskFile) _keepDownloadTaskFile;
```

## Class methods

```
+[NWURLSessionDownloadResumeInfo supportsSecureCoding];
+[NWURLSessionDownloadResumeInfo infoWithResumeData:];
+[NWURLSessionDownloadResumeInfo infoWithTask:];
```

## Instance methods

```
-[NWURLSessionDownloadResumeInfo set_keepDownloadTaskFile:];
-[NWURLSessionDownloadResumeInfo setFileURL:];
-[NWURLSessionDownloadResumeInfo fileURL];
-[NWURLSessionDownloadResumeInfo _keepDownloadTaskFile];
-[NWURLSessionDownloadResumeInfo encodeWithCoder:];
-[NWURLSessionDownloadResumeInfo serialize];
-[NWURLSessionDownloadResumeInfo initWithCoder:];
-[NWURLSessionDownloadResumeInfo setTempFileName:];
-[NWURLSessionDownloadResumeInfo tempFileName];
```
