# `NWURLSessionUploadTask`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWURLSessionDataTask`
- 1 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _resumeURLInternal;
```

## Properties

```
@property (T@"NSURL",R) _resumeURL;
```

## Class methods

```
+[NWURLSessionUploadTask isSubclassOfClass:];
```

## Instance methods

```
-[NWURLSessionUploadTask errorWithResumeData:];
-[NWURLSessionUploadTask _resumeURL];
-[NWURLSessionUploadTask uploadResumeURL];
-[NWURLSessionUploadTask supportsResumableUpload];
-[NWURLSessionUploadTask isKindOfClass:];
-[NWURLSessionUploadTask isUpload];
-[NWURLSessionUploadTask cancelByProducingResumeData:];
```
