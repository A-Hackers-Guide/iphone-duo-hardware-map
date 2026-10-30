# `__NSCFResumableUploadState`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
c _retryCounter;
c _repeatedStreamOpenings;
B _userOverride;
i _state;
i _bodyType;
q _offset;
@"NSURLRequest" _originalRequest;
@"NSData" _uploadData;
@"NSURL" _resumeURL;
@"NSString" _draftVersion;
q _streamLength;
@"NSURL" _uploadFile;
```

## Properties

```
@property (T@"NSURL",C,V_uploadFile) uploadFile;
```

## Class methods

```
+[__NSCFResumableUploadState supportsSecureCoding];
+[__NSCFResumableUploadState rusWithResumeData:originalRequest:];
```

## Instance methods

```
-[__NSCFResumableUploadState uploadFile];
-[__NSCFResumableUploadState setUploadFile:];
-[__NSCFResumableUploadState createResumeDataForTaskInfo];
-[__NSCFResumableUploadState encodeWithCoder:];
-[__NSCFResumableUploadState initWithCoder:];
-[__NSCFResumableUploadState isResumable];
```
