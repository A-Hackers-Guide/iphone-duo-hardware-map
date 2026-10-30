# `NWURLSessionUploadResumeInfo`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWURLSessionResumeInfo`
- 3 instance variables, 3 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSURL" _resumeURL;
@"NSData" _data;
@"NSURL" _fileURL;
```

## Properties

```
@property (T@"NSURL",&,N,V_resumeURL) resumeURL;
@property (T@"NSData",&,N,V_data) data;
@property (T@"NSURL",&,N,V_fileURL) fileURL;
```

## Class methods

```
+[NWURLSessionUploadResumeInfo supportsSecureCoding];
+[NWURLSessionUploadResumeInfo infoWithResumeData:];
+[NWURLSessionUploadResumeInfo infoWithTask:];
```

## Instance methods

```
-[NWURLSessionUploadResumeInfo setFileURL:];
-[NWURLSessionUploadResumeInfo fileURL];
-[NWURLSessionUploadResumeInfo data];
-[NWURLSessionUploadResumeInfo setData:];
-[NWURLSessionUploadResumeInfo encodeWithCoder:];
-[NWURLSessionUploadResumeInfo serialize];
-[NWURLSessionUploadResumeInfo initWithCoder:];
-[NWURLSessionUploadResumeInfo resumeURL];
-[NWURLSessionUploadResumeInfo setResumeURL:];
```
